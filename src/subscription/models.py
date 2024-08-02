from django.db import models
from django.contrib.auth.models import Group, Permission
from django.conf import settings
# Create your models here.

User =  settings.AUTH_USER_MODEL

SUBSCRIPTION_PERMISSIONS = [
            ("advanced", "Advanced Perm"),
            ("pro", "Pro Perm"),
            ("Basic", "Basic Perm"),
            ("basic_ai", "Basic AI Perm"),

        ]

class Subscription(models.Model):
    name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group)
    permissions = models.ManyToManyField(Permission, limit_choices_to = {"content_type__app_label":"subscription", "codename__in":["Basic","advanced","pro"]})


    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS

    def __str__(self):
        return f"{self.name}"


class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null = True, blank=True)
    active = models.BooleanField(default=True)
