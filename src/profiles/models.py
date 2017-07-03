from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    description = models.TextField(default='default text')
    location = models.CharField(max_length=120, null=True, blank=True)
    job = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str("%s: %s" %(self.user.username, self.stripe_id))
        else:
            return str(self.user.username)

def stripeCallback(sender, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print("*****Profile created for user: %s" %(user.username))
    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()

def profileCallback(sender, user, **kwargs):
    userProfile, is_created = profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()

user_logged_in.connect(stripeCallback)
user_logged_in.connect(profileCallback)

# request_finished.connect(my_callback)   - Signal callback