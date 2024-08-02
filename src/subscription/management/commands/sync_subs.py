from typing import Any
from django.core.management.base import BaseCommand

from subscription.models import Subscription


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("hello world")
        qs = Subscription.objects.filter(active=True)
        for obj in qs:
            # print(obj.groups.all())
            super_perams = obj.permissions.all()
            for group in obj.groups.all():
                group.permissions.set(super_perams)
                # for per in obj.permissions.all():
                    # group.permissions.add(per)
            # print(obj.permissions.all())