from rest_framework.mixins import (
    RetrieveModelMixin, ListModelMixin, CreateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .models import Link
from .serializers import LinkSerializer
from string import ascii_letters
from random import choice
from django.shortcuts import redirect, get_object_or_404


class LinkViewset(
    GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin
):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer: LinkSerializer):
        # Not good I know I know) There should be some checks obviously
        random_slug = ''.join(choice(ascii_letters) for _ in range(10))

        return serializer.save(
            slug=random_slug,
            fake_url='http://127.0.0.1:8000/link/'+random_slug
        )


def redirect_to_original_url(request, slug):
    link = get_object_or_404(Link, slug=slug)
    return redirect(link.original_url)
