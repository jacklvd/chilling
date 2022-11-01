from rest_framework import serializers
from django.forms import ValidationError
from .models import Book

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_pages = serializers.IntegerField()
#     published_date = serializers.DateField()
#     quantity = serializers.IntegerField()
    
#     def create(self, data):
#         return Book.objects.create(**data)
    
#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_pages = data.get('number_pages', instance.number_pages)
#         instance.published_date = data.get('published_date', instance.published_date)
#         instance.quantity = data.get('quantity', instance.quantity)
        
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_title(self, value):
        if value == 'Diet Coke':
            raise ValidationError('No diet coke please')
        return value
    
    def validated(self, data):
        if data["number_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("too heavy for inventory")
        return data        