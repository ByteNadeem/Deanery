from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import NewsletterSubscriber
from .forms import NewsletterSignupForm


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'


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
        return JsonResponse({'success': False, 'message': 'Invalid submission'})
    
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
            'message': 'Thank you! Please check your email to confirm your subscription.'
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
    message = f"""
    Hello {subscriber.get_full_name()},

    Thank you for subscribing to our newsletter!

    Please click the link below to confirm your subscription:
    {confirmation_url}

    If you didn't sign up for this newsletter, you can safely ignore this email.

    Best regards,
    The Deanery Team
    """
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [subscriber.email],
        fail_silently=False,
    )

def newsletter_confirm(request, token):
    """Confirm newsletter subscription"""
    subscriber = get_object_or_404(NewsletterSubscriber, confirmation_token=token)
    
    if not subscriber.is_confirmed:
        subscriber.is_confirmed = True
        subscriber.confirmed_at = timezone.now()
        subscriber.save()
        
        message = "Your subscription has been confirmed! Thank you for joining our newsletter."
    else:
        message = "Your subscription was already confirmed."
    
    return render(request, 'newsletter/confirmation.html', {
        'message': message,
        'subscriber': subscriber
    })

def newsletter_unsubscribe(request, token):
    """Unsubscribe from newsletter"""
    subscriber = get_object_or_404(NewsletterSubscriber, confirmation_token=token)
    
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
