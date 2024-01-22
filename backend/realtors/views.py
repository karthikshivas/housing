from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer

# Create your views here.

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()
    pagination_class = None

class RealtorView(RetrieveAPIView):
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None



