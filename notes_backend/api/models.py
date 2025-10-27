from django.db import models
import uuid


class TimeStampedModel(models.Model):
    """Abstract base model with created_at and updated_at timestamp fields."""
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the object was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the object was last updated.")

    class Meta:
        abstract = True


class Note(TimeStampedModel):
    """
    Note model representing an individual note entry.

    Fields:
    - id: UUID primary key (ensures uniqueness and is API-friendly)
    - title: short text title for the note (required, max_length=255)
    - content: long text content (optional but recommended)
    - created_at / updated_at inherited from TimeStampedModel
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["-updated_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.title} ({self.id})"
