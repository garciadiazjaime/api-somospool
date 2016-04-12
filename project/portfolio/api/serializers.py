from rest_framework import serializers

from ..models import Category, Project, Block, Image

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'order')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'subtitle', 'order', 'status', 'cover', 'categories')

class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        depth = 1
        many = True
        fields = ('id', 'type', 'text', 'order', 'image_set')
