from django.urls import path, include
from .views import *

from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', home, name = "home"),

    #__About Us
    path('aboutus/', about_us, name = "aboutus"),

    #__Feature
    # path('features/', features, name = "features"),
    path('features/', FeaturesList.as_view(), name = "features"),
    path('featuresCreate/', FeaturesCreate.as_view(), name = "featuresCreate"),
    path('featuresUpdate/<int:pk>/', FeaturesUpdate.as_view(), name = "featuresUpdate"),
    path('featuresDelete/<int:pk>/', FeaturesDelete.as_view(), name = "featuresDelete"),

    #__Subscribe
    # path('subscribe/', subscribe, name = "subscribe"),   
    path('subscribe/', SubscribeList.as_view(), name = "subscribe"),
    path('subscribeCreate/', SubscribeCreate.as_view(), name = "subscribeCreate"),
    path('subscribeUpdate/<int:pk>/', SubscribeUpdate.as_view(), name = "subscribeUpdate"),
    path('subscribeDelete/<int:pk>/', SubscribeDelete.as_view(), name = "subscribeDelete"),
    
        #__ Search subscribe
    path('searchsubscribe/', searchSubscribe, name= "searchsubscribe" ), 
    path('findsearch/', findSearch, name= "findsearch" ), 

    #__Review
    path('review/', review, name = "review"),
    path('reviewForm/', reviewForm, name = "reviewForm"),
    path('reviewUpdate/<id_review>/', reviewUpdate, name = "reviewUpdate"),
    path('reviewDelete/<id_review>/', reviewDelete, name = "reviewDelete"),

    #__Contact Us
    # path('contact_us/', contact_us, name = "contact_us"),
    path('contact_us/', Contact_UsList.as_view(), name = "contact_us"),
    path('contact_usCreate/', Contact_UsCreate.as_view(), name = "contact_usCreate"),
    path('contact_usUpdate/<int:pk>/', Contact_UsUpdate.as_view(), name = "contact_usUpdate"),
    path('contact_usDelete/<int:pk>/', Contact_UsDelete.as_view(), name = "contact_usDelete"),


    #__LogIn, Logout, Register
    path('login/', loginRequest, name = "login"),
    path('logout/', LogoutView.as_view(template_name="Walkly/logout.html"), name="logout"),
    path('register/', register, name = "register"), 

    #___ Edit Profile - Avatar
    path('profile/', editProfile, name= "profile"),
    path('<int:pk>/password/', ChangePassword.as_view(), name="change_password"),
    path('addAvatar/', addAvatar, name= "addAvatar"),


]   
