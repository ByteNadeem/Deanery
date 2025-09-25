from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @property
    def _is_staff(self):
        return self.is_staff or self.user.is_staff


# NewsletterSubscription model

class NewsletterSubscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Subscription status
    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # GDPR compliance
    consent_given = models.BooleanField(default=False)
    consent_timestamp = models.DateTimeField(null=True, blank=True)
    consent_ip_address = models.GenericIPAddressField(null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    # Confirmation token
    confirmation_token = models.UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.email} - {'Confirmed' if self.is_confirmed else 'Pending'}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
