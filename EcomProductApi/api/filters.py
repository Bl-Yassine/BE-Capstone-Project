import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category__name': ['exact', 'icontains'],  # Allow case-insensitive matching
            'price': ['exact', 'gte', 'lte', 'range'],
            'stock_quantity': ['exact', 'gte', 'lte', 'range'],
        }

