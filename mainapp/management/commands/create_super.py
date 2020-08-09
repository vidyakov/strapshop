from django.core.management.base import BaseCommand
from authapp.models import StrapUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        StrapUser.objects.create_superuser(
            username='sasha',
            email=None,
            password='secret_password',
            age=None
        )
