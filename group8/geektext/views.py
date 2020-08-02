from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BookSerializer
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers


#Get books and display them
@api_view(['GET'])
def index(request):
    books = Books.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre(request):
    requested_genre = json.loads(request.body)["genre"]
    try:
        books = Books.objects.filter(genre=requested_genre)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("No books matching that genre exist")

@api_view(['GET'])
def bestsellers(request):
    try:
        books = list(Books.objects.order_by('-number_sold')[:10])
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response('No books in the database')

@api_view(['GET'])
def rating_sort(request):
    better_than = json.loads(request.body)["rating"] 
    try:
        books = list(Books.objects.filter(rating__gte=better_than))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("No books better than that rating are available")

@api_view(['GET'])
def random_list(request):
    num_books = json.loads(request.body)["amount"]
    try:
        books = list(Books.objects.order_by('?')[:num_books])
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response("No books found in the database")