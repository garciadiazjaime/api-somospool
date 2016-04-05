from rest_framework import viewsets

from ..models import Category, Project, Block, Image
from .serializers import CategorySerializer, ProjectSerializer, BlockSerializer

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get_queryset(self):
    queryset = Category.objects.all()
    return queryset.order_by('order', 'id')

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

  def get_queryset(self):
    queryset = Project.objects.all()
    return queryset.order_by('order', 'id')

class BlockViewSet(viewsets.ModelViewSet):
  queryset = Block.objects.none()
  serializer_class = BlockSerializer

  def get_queryset(self):
    queryset = Block.objects.none()
    project_id = self.request.query_params.get('project_id', None)
    if project_id is not None:
        queryset = Block.objects.filter(project=project_id)
    return queryset.order_by('order', 'id')
