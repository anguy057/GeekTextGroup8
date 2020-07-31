from rest_framework import serializers
from users.models import Account, CreditCard

class RegistrationSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Account
        fields = ['email','username','password','address','name']
        #extra_kwargs= {
        #    'password': {'write_only': True}
        #}

    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        account.address = self.validated_data['address']
        account.name = self.validated_data['name']
        account.set_password(password)
        account.save()
        return account

'''class AccountUsernameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username']'''


class CardRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditCard
        fields = ['cardnumber','owner']

    def save(self):
        creditcard = CreditCard(
            cardnumber = self.validated_data['cardnumber'],
            owner = self.validated_data['owner']    
        )
        creditcard.save()
        return creditcard
        


class CreditCardSerializer(serializers.ModelSerializer):



    class Meta:
        model = CreditCard
        fields = ['cardnumber','owner']
    
class AccountInfoSerializer(serializers.ModelSerializer):



    class Meta:
        model = Account
        fields = ['username','address','name','email']


class AccountInfoChangerSerializer(serializers.ModelSerializer):



    class Meta:
        model = Account
        fields = ['username','address','name']

    '''def save(self):
        account = Account(
           username = self.validated_data['username'],
        )
        account.address = self.validated_data['address']
        account.name = self.validated_data['name']
        account.save()
        return account'''

class PasswordChangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['old_password','new_password']
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
