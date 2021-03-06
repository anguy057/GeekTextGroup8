from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.api.serializers import RegistrationSerializer, AccountInfoSerializer, AccountInfoChangerSerializer,PasswordChangerSerializer, CreditCardSerializer,CardRegistrationSerializer
from users.models import Account, CreditCard
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "New user created within database"
            data['email'] = account.email
            data['username'] = account.username
            data['address'] = account.address
            data['name'] = account.name
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST', ])
def card_registration_view(request):
    if request.method == 'POST':
        serializer = CardRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            creditcard = serializer.save()
            data['response'] = "New Credit Card entered in database"
            data['cardnumber'] = creditcard.cardnumber
            return Response(data=data)
        else:
            data = serializer.errors
        return Response(data=data)

'''@api_view(['GET', ])
def account_info(request):

    #if account does not exist give error
    try:
        account =  request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AccountInfoSerializer(account)
        return Response(serializer.data)'''


class PropertiesView(generics.ListAPIView):
    serializer_class = AccountInfoSerializer
    def get_queryset(self):
        queryset = Account.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class CardView(ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    filter_backends = (SearchFilter, )
    search_fields = ['owner__username']

@api_view(['PUT', ])
def account_update_view(request, username):
    account = Account.objects.get(username=username)
    if request.method == 'PUT':
        serializer = AccountInfoChangerSerializer(account, data = request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Updated'
            data['username'] = account.username
            data['address'] = account.address
            data['name'] = account.name
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
def account_info_view(request,username):
    account = Account.objects.get(username=username)
    if request.method == 'GET':
        serializer = AccountInfoSerializer(account)
        return Response(serializer.data)

@api_view(['GET', ])
def credit_card_view(request,username):
    owner = CreditCard.objects.get(username=username)
    if request.method == 'GET':
        serializer = CreditCardSerializer(owner,data = request.data)
        return Response(serializer.data)

@api_view(['PUT', ])
def password_changer_view(request,username):
    account = Account.objects.get(username=username)
    if request.method == 'PUT':
        serializer = PasswordChangerSerializer(account,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Password Changed'
            account.set_password(serializer.data.get("new_password"))
            account.save()
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
