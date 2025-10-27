from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """Simple health check endpoint."""
    return Response({"message": "Server is up!"})


class NotePagination(PageNumberPagination):
    """Basic pagination for Note list endpoints."""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# PUBLIC_INTERFACE
class NoteViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    NoteViewSet provides full CRUD operations for notes.

    Endpoints:
    - GET /api/notes/            -> list notes (paginated)
    - POST /api/notes/           -> create note
    - GET /api/notes/{id}/       -> retrieve note by id
    - PUT /api/notes/{id}/       -> update entire note
    - PATCH /api/notes/{id}/     -> partial update
    - DELETE /api/notes/{id}/    -> delete note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = NotePagination

    @swagger_auto_schema(
        operation_summary="List notes",
        operation_description="Return a paginated list of notes ordered by most recently updated first.",
        responses={200: NoteSerializer(many=True)},
        tags=["notes"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create note",
        operation_description="Create a new note with a title and optional content.",
        responses={201: NoteSerializer()},
        tags=["notes"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve note",
        operation_description="Retrieve a note by its UUID.",
        responses={200: NoteSerializer()},
        tags=["notes"],
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_PATH,
                description="UUID of the note",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update note",
        operation_description="Replace all fields of a note.",
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update note",
        operation_description="Update one or more fields of a note.",
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete note",
        operation_description="Delete a note by its UUID.",
        responses={204: "No Content"},
        tags=["notes"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
