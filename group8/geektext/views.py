from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Books
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers


#Get books and display them
def index(request):
    books_json = serializers.serialize("json", Books.objects.all())
    data = {"all_books": books_json}
    return JsonResponse(data)

def genre(request):
    requested_genre = json.loads(request.body)["genre"]
    try:
        books_json = serializers.serialize("json", list(Books.objects.filter(genre=requested_genre)))
        data = {requested_genre + " books": books_json}
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponse("No books matching that genre exist")

def bestsellers(request):
    try:
        books_json = serializers.serialize("json", list(Books.objects.order_by('-number_sold')[:10]))
        data = {"Bestsellers": books_json}
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponse('No books in the database')

def rating_sort(request):
    better_than = json.loads(request.body)["rating"] 
    try:
        books_json = serializers.serialize("json", list(Books.objects.filter(rating__gte=better_than)))
        data = {str(better_than) + " or better books" : books_json}
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponse("No books better than that rating are available")

def random_list(request):
    num_books = json.loads(request.body)["amount"]
    try:
        books_json = serializers.serialize("json", list(Books.objects.order_by('?')[:num_books]))
        data = {str(num_books) + " random books" : books_json}
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponse("No books found in the database")