# bookshelf/management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create user groups and assign permissions for Book model'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        permissions = {
            "can_view": Permission.objects.get(codename="can_view"),
            "can_create": Permission.objects.get(codename="can_create"),
            "can_edit": Permission.objects.get(codename="can_edit"),
            "can_delete": Permission.objects.get(codename="can_delete"),
        }

        # Create groups
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        editors, _ = Group.objects.get_or_create(name="Editors")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Assign permissions to groups
        viewers.permissions.set([permissions["can_view"]])
        editors.permissions.set([
            permissions["can_view"],
            permissions["can_create"],
            permissions["can_edit"],
        ])
        admins.permissions.set(permissions.values())

        self.stdout.write(self.style.SUCCESS("Groups and permissions successfully created."))
