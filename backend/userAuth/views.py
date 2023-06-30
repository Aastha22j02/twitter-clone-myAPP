from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


from userAuth.models import userAuthModal
from userAuth.serilizers import userAuthSerializers


# Create your views here.

class userAuthViewSet(viewsets.ModelViewSet):
    queryset = userAuthModal.objects.all()
    serializer_class = userAuthSerializers
    
    
class CheckEmailViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        email = request.GET.get('email')
        is_unique = not userAuthModal.objects.filter(email=email).exists()
        response_data = {'is_unique': is_unique}
        return Response(response_data, status=status.HTTP_200_OK)


class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(f"Your enterd mail is {email}")
        print(f"Your enterd password is {password}")
        
        users = userAuthModal.objects.values('email', 'password')
        
        for user in users:
            print(f"{user}")

        for user in users:
            if user['email'] == email and user['password'] == password:
                return Response({'message': 'Login successful'})
                
        
        return Response({'message': 'Invalid credentials'}, status=400)
                
        # user = authenticate(request, email=email, password=password)
        # if user is not None:
        #     login(request, user)
        #     return Response({'message': 'Login successful'})
        # else:
        #     return Response({'message': 'Invalid credentials'}, status=400)
        
        
        
        
        
        