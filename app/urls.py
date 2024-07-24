from django.urls import path
from app.views import Home_b, Home, Home_s, Checkout, LogoutView, SigninView, SignupView, SellerView
urlpatterns = [
    path("", Home.as_view(), name="home"),
    
    path('home_b/', Home_b.as_view(), name="home_buying"),
    path("home_s/", Home_s.as_view(), name="home_selling"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path("seller_view/", SellerView.as_view(), name="Seller Home view"),
    path("signin/", SigninView.as_view(), name="Signin"),
    path("signup/", SignupView.as_view(), name="Signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
]