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
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id','name']
        fields = '__all__'
        # exclude = ['id']
        
    def create(self, validated_data):
        # total_number = Category.objects.filter(name = validated_data.get('name')).count()
        total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if total_number > 0:
            raise serializers.ValidationError("Already exist")
        
        category = self.Meta.model(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        