from django.urls import path, re_path

# from shorter.api.endpoints import ShortUrl, ShortUrlsList
from shorter.routers import router
# from shorter.api.endpoints import ShortUrl


urlpatterns = [
    # path('', ShortUrl.as_view()),
    # path('all-urls/', ShortUrlsList.as_view()),
    # path('<str:short>/', ShortUrl.as_view()),

]

