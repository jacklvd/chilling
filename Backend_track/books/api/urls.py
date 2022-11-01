from django.contrib import admin
from django.urls import path
# from api.views import book_list, book_add, book
from .views import BookList, BookCreate, BookDetails

# urlpatterns = [
#     path('', book_add),
#     path('list/', book_list),
#     path('<int:pk>', book)
# ]


urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('', BookCreate.as_view(), name='create'),
    path('<int:pk>', BookDetails.as_view()),    
]
