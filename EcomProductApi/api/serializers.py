from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Product ,Order

#Registration Serializers
class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password' ,]
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

#Category serializers
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


#Product serializers 
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user'] # The user field sould be read-Only

#oredre Serializers
class OrderSerializers(serializers.ModelSerializer):
     class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user']

        def validate_product(self, value):
            if value.stock_quantity <= 0:
                raise serializers.ValidationError("Not enough stock available for this product.")
            return value

        






        
