from rest_framework.generics import (
                            ListCreateAPIView,    
                            RetrieveUpdateDestroyAPIView,)
from ducks.models import duck 
from .serializers import DuckSerializer    
from .permissions import IsOwnerOrReadOnly            

class SnackListView(ListCreateAPIView):
    queryset = duck.objects.all()
    serializer_class = DuckSerializer
    


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = duck.objects.all()
    serializer_class = DuckSerializer
    permission_classes = (IsOwnerOrReadOnly,)