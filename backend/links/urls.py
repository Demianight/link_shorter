from rest_framework.routers import SimpleRouter
from .views import LinkViewset, redirect_to_original_url
from django.urls import path, include


router = SimpleRouter()

router.register('links', LinkViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('link/<str:slug>', redirect_to_original_url, name='link_redirect'),
]
