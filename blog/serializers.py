from rest_framework import serializers
from .models import Article


class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128, required=True, allow_null=False, allow_blank=False)
    cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2254)
    created_at = serializers.DateTimeField(required=True, allow_null=False)