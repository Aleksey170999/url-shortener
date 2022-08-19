from rest_framework.routers import DefaultRouter

from shorter.api.endpoints import ShortUrls

router = DefaultRouter()

router.register('shorter', ShortUrls, basename='Shorter')
