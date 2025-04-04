from rest_framework import serializers
from .models import *

# class CategorySerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name =serializers.CharField(max_length=100)
    
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
    
#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.save()
#         return instance
class CataegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id','name']
        fields = '__all__'
        # exclude = ['id']
        
    # def save(self, validated_data):
    def save(self, **kwargs):
        validated_data = self.validated_data
        # total_number = Category.objects.filter(name = validated_data.get('name')).count()
        total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if total_number > 0:
            raise serializers.ValidationError("Already exist")
        
        category = self.Meta.model(**validated_data)
        category.save()
        return category

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
        
    # for food category
    
class FoodSerializers(serializers.ModelSerializer):
    pricetax = serializers.SerializerMethodField()
    category_id = serializers.StringRelatedField()
    class Meta:
        model = Food
        # fields = ['id','name']
        # fields = '__all__'
        fields = ["id", "name", "describe", "price", "pricetax", "category_id"]
        # exclude = ['id']
    def get_pricetax(self, food:Food):
        return food.price*2+food.price