"""
Type stubs for Django User model with custom related fields.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser
    from django.db.models import QuerySet

    from notes.models import Note

    class User(AbstractUser):
        """Extended User type with notes relationship."""

        notes: "QuerySet[Note]"
