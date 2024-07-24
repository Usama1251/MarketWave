from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

class Home(APIView):
    def get(self, request):
        return render(request, 'home.html')

class Home_b(APIView):
    def get(self, request):
        return render(request, 'buyer.html')
    
class Checkout(APIView):
    def get(self, request):
        return render(request, 'checkout.html')
        
class Home_s(APIView):
    def get(self, request):
        return render(request, 'seller.html')
    
class SellerView(APIView):
    def get(self, request):
        return render(request, "seller_view.html")

class SigninView(APIView):
    def get(self, request):
        return render(request, 'signin.html')
    
class SignupView(APIView):
    def get(self, request):
        return render(request, 'signup.html')
    
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html', {'user': User})
