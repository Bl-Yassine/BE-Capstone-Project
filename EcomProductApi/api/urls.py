from django.urls import path ,include
from .views import register , login_view , CategotyViewSet ,ProductViewSet ,OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategotyViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('',include(router.urls)),
]