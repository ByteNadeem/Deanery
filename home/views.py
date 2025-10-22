# from multiprocessing import context
import os
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView, FormView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# from requests import request
from .models import NewsletterSubscriber, Church, Event
from .forms import NewsletterSignupForm, ContactForm


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add upcoming events (next 3)
        context['upcoming_events'] = Event.objects.filter(
            start_time__gte=timezone.now()
        ).order_by('start_time')[:3]

        # Add featured events
        context['featured_events'] = Event.objects.filter(
            is_featured=True, 
            start_time__gte=timezone.now()
        )[:2]

        return context


def get_client_ip(request):
    """Utility function to get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@require_http_methods(["POST"])
@csrf_protect
def newsletter_signup(request):
    # Anti-bot check
    if request.POST.get('website'):  # Honeypot field
        return JsonResponse({
            'success': False,
            'message': 'Invalid submission'
        })

    form = NewsletterSignupForm(request.POST)

    if form.is_valid():
        subscriber = form.save(commit=False)
        subscriber.consent_given = True
        subscriber.consent_timestamp = timezone.now()
        subscriber.consent_ip_address = get_client_ip(request)
        subscriber.save()

        # Send confirmation email
        send_confirmation_email(request, subscriber)

        return JsonResponse({
            'success': True,
            'message': (
                'Thank you! Please check your email to confirm your '
                'subscription.'
            )
        })
    else:
        errors = []
        for field, field_errors in form.errors.items():
            for error in field_errors:
                errors.append(f"{field}: {error}")

        return JsonResponse({
            'success': False,
            'message': ' '.join(errors)
        })


def send_confirmation_email(request, subscriber):
    """Send double opt-in confirmation email"""
    confirmation_url = request.build_absolute_uri(
        reverse('newsletter_confirm', args=[subscriber.confirmation_token])
    )

    subject = 'Confirm your newsletter subscription'
    message = (
        f"Hello {subscriber.get_full_name()},\n\n"
        "Thank you for subscribing to our newsletter!\n\n"
        "Please click the link below to confirm your subscription:\n"
        f"{confirmation_url}\n\n"
        "If you didn't sign up for this newsletter, you can safely ignore this email.\n\n"
        "Best regards,\n"
        "The Deanery Team"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [subscriber.email],
        fail_silently=False,
    )


def newsletter_confirm(request, token):
    """Confirm newsletter subscription"""
    subscriber = get_object_or_404(
        NewsletterSubscriber, confirmation_token=token
    )

    if not subscriber.is_confirmed:
        subscriber.is_confirmed = True
        subscriber.confirmed_at = timezone.now()
        subscriber.save()

        message = (
            "Your subscription has been confirmed! "
            "Thank you for joining our newsletter."
        )
    else:
        message = "Your subscription was already confirmed."

    return render(request, 'newsletter/confirmation.html', {
        'message': message,
        'subscriber': subscriber
    })


def newsletter_unsubscribe(request, token):
    """Unsubscribe from newsletter"""
    subscriber = get_object_or_404(
        NewsletterSubscriber,
        confirmation_token=token
    )

    if request.method == 'POST':
        subscriber.is_active = False
        subscriber.unsubscribed_at = timezone.now()
        subscriber.save()

        return render(request, 'newsletter/unsubscribed.html', {
            'subscriber': subscriber
        })

    return render(request, 'newsletter/unsubscribe_confirm.html', {
        'subscriber': subscriber
    })


class ContactView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        # Process the form data here (e.g., send an email)
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        telephone = form.cleaned_data['telephone']
        message = form.cleaned_data['message']

        # send email
        send_mail(
            subject=(
                f"Contact Form Submission from: "
                f"{form.cleaned_data['name']}"
            ),
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )
        # Remove me before production
        print("contact form submitted:", form.cleaned_data)

        return super().form_valid(form)


class AboutPage(TemplateView):
    """
    Displays about page"
    """
    template_name = 'home/about.html'


def churches(request):
    churches = Church.objects.all()
    return render(request, "home/churches.html", {"churches": churches})


# Event Views

class StaffRequiredMixin(UserPassesTestMixin):
    """Mixin to require staff or superuser access"""
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class EventListView(ListView):
    model = Event
    template_name = 'home/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(is_featured=True, start_time__gte=timezone.now())
        context['past_events'] = Event.objects.filter(end_time__lt=timezone.now()).order_by('-start_time')[:5]
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'home/event_detail.html'


class EventCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Event
    template_name = 'home/event_form.html'
    fields = ['title', 'description', 'location', 'church', 'start_time', 'end_time', 'image', 'is_featured']
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Event
    template_name = 'home/event_form.html'
    fields = ['title', 'description', 'location', 'church', 'start_time', 'end_time', 'image', 'is_featured']
    success_url = reverse_lazy('events')


class EventDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Event
    template_name = 'home/event_confirm_delete.html'
    success_url = reverse_lazy('events')


def event_like(request, pk):
    """Toggle like status for an event"""
    if not request.user.is_authenticated:
        return JsonResponse(
            {'status': 'error', 'message': 'Login required'},
            status=401
        )

    event = get_object_or_404(Event, pk=pk)

    if request.user in event.likes.all():
        event.likes.remove(request.user)
        liked = False
    else:
        event.likes.add(request.user)
        liked = True

    return JsonResponse({
        'status': 'success',
        'liked': liked,
        'likes': event.like_count
    })