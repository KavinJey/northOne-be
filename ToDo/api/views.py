from rest_framework import viewsets, mixins
from .serializers import TodoItemSerializer
from .models import TodoItem


# Create your views here.
class TodoViewSet(mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin, 
                  mixins.CreateModelMixin, 
                  mixins.ListModelMixin, 
                  viewsets.GenericViewSet):

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = ()
    authorization_classes = []