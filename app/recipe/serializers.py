from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.Serializer):
    """serializers for tag models"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
