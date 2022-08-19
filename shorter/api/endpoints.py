from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from cfg.settings import SITE_URL
from rest_framework.response import Response

from shorter.models import URL
from shorter.utils import create_random_code

from ..serializers import ShortenerSerializer


class ShortUrls(ModelViewSet):
    serializer_class = ShortenerSerializer
    queryset = URL.objects.all()
    lookup_field = 'short_url'

    def create(self, request, *args, **kwargs):
        try:
            existing_short = URL.objects.get(long_url=request.data['long_url']).short_url
            return Response(data={"short": SITE_URL + "/" + existing_short + "/"})
        except:
            new_short = create_random_code()
            instance = URL(long_url=request.data['long_url'],
                           short_url=new_short)
            instance.save()
            return Response(data={"short": SITE_URL + "/" + new_short + "/"})

    def retrieve(self, request, *args, **kwargs):
        url_instance = URL.objects.get(short_url=kwargs['short_url'])
        url_instance.times_followed_incr()
        url_instance.save()

        serializer = ShortenerSerializer(url_instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = URL.objects.all()
        serializer = ShortenerSerializer(queryset, many=True)
        return Response(serializer.data)

#
# class ShortUrl(APIView):
#     def post(self, request):
#         try:
#             existing_short = URL.objects.get(long_url=request.data['long']).short_url
#             return Response(data={"short": SITE_URL + "/" + existing_short + "/"})
#         except:
#             new_short = create_random_code()
#             instance = URL(long_url=request.data['long'],
#                            short_url=new_short)
#             instance.save()
#             return Response(data={"short": SITE_URL + "/" + new_short + "/"})
#
#     def get(self, request, short):
#         url_instance = URL.objects.get(short_url=short)
#         url_instance.times_followed_incr()
#         url_instance.save()
#
#         serializer = ShortenerSerializer(url_instance)
#         return Response(serializer.data)
#
#
# class ShortUrlsList(APIView):
#     def get(self, request):
#         queryset = URL.objects.all()
#         serializer = ShortenerSerializer(queryset, many=True)
#         return Response(serializer.data)
