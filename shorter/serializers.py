from rest_framework.serializers import ModelSerializer

from shorter.models import URL


class ShortenerSerializer(ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'created_at', 'times_followed', 'long_url', 'short_url']
