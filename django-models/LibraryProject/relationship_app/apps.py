from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

def ready(self):
    import relationship_app.signals

from django.urls import path
from . import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view.librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view.member_view, name='member_view'),
]

