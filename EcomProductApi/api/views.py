from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
#user Registartion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .serializers import RegisterSerializers, CategorySerializers, ProductSerializers , OrderSerializers
from .models import Category, Product, Order
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#login view
from django.contrib.auth import authenticate
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username = username , password = password)
    if user :
        return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


#CRUD
from rest_framework import viewsets

#Caregory CRUD use ViewSet
class CategotyViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


from .permissions import ProductPermission
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
#Prudact CRUD use ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProductPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

#Order CRUD 
from rest_framework import serializers
from rest_framework.decorators import action
from .permissions import OrderPermission
class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OrderPermission]
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        #check if the product object fron the validated data
        if product.stock_quantity <= 0:
            raise serializers.ValidationError("Not enough stock available for this product.")
        # Reduce the product stock by 1 (or adjust this logic as needed)
        product.stock_quantity -= 1
        product.save()
        # Save the order with the associated user
        serializer.save(user = self.request.user)
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
