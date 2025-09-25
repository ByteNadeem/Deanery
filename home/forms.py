from django import forms
from django.core.exceptions import ValidationError
from .models import NewsletterSubscription

#  Newsletter Signup form here


class NewsLetterSignupForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        error_messages={
            'required': 'Please provide consent to receive our newsletter.'
            }
    )

    class Meta:
        model = NewsletterSubscription
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'your.email@example.com'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NewsletterSubscription.objects.filter(
            email=email, is_active=True
        ).exists():
            raise ValidationError(
                'This email is already subscribed to the newsletter.'
                )
        return email
