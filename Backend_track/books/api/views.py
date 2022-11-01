from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from .models import Book
from .serializer import BookSerializer


# @api_view(['GET'])
# def book_list(request):
#     model = Book.objects.all() # complex data
#     serializer = BookSerializer(model, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def book_add(request):
#     serializer = BookSerializer(data=request.data) # convert from JSON to complex
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])    
# def book(request, pk):   
#     try:
#         model = Book.objects.get(pk=pk) # complex data
#     except:
#         return Response({
#             'error' : 'book does not exist',
#         }, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'GET':
#         serializer = BookSerializer(model)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = BookSerializer(model, data=request.data)
#         # validate data
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

        
# Second way: Using class        
class BookList(APIView):
    def get(self, request):
        model = Book.objects.all() # complex data
        serializer = BookSerializer(model, many=True)
        return Response(serializer.data)
    
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data) # convert from JSON to complex
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


class BookDetails(APIView):
    def get_book(self, pk):
        try:
            return Book.objects.get(pk=pk) # complex data
        except:
            return Response({
                'error' : 'book does not exist',
            }, status=status.HTTP_404_NOT_FOUND)
            
    def get(self, request, pk):
        model = self.get_book(pk)
        serializer = BookSerializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk):
        model = self.get_book(pk)
        serializer = BookSerializer(model, data=request.data)
        # validate data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        model = self.get_book(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                    