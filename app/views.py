from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from .models import Product
from django.conf import settings
from .serializers import SigninSerializer, SignupSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

class Home(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'home.html')

class Home_b(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = Product.objects.all()  # Fetch all products from the database
        return render(request, 'buyer.html', {'products': products})
 
class Checkout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return render(request, 'checkout.html')
        
class Home_s(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return render(request, 'seller.html')

    def post(self, request):
        # Handle the uploaded image
        image = request.FILES['product-image']
        
        # Handle the description and price
        description = request.POST.get('product-description')
        price = request.POST.get('product-price')
        
        # Save to database
        product = Product( image=image, description=description, price=price)
        product.save()
        
        # Generate the image URL
        image_url = settings.MEDIA_URL + product.image.name
        
        # Render the template with the submitted data
        return render(request, 'seller.html', {
            'image_url': image_url,
            'description': description,
            'price': price
        })
        
class SellerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = Product.objects.all()  # Fetch all products from the database

        return render(request, 'seller_view.html', {'products': products})

class SigninView(APIView):
    def get(self, request):
        return render(request, 'signin.html')
    def post(self, request):
        data = request.data
        serializer = SigninSerializer(data=data)
        
        if serializer.is_valid():
            user = authenticate(username= data["username"], password=data["password"])

            if user is not None:
                login(request, user)  # Log in the user
                return redirect('/')
            else:
                return redirect('/signin/')

class SignupView(APIView):
    def get(self, request):
        return render(request, 'signup.html', {'errors': {}})
    
    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')  
        errors = serializer.errors
        return render(request, 'signup.html', {'errors': errors})
           
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        logout(request)
        return render(request, 'logout.html', {'user': User})
