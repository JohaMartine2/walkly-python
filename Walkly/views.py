from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin #class
from django.contrib.auth.decorators import login_required #function


#__ Home
def home(request):
    return render(request, "Walkly/index.html")

#__ About Us
def about_us(request):
    return render(request, "Walkly/aboutus.html")


#__ Features
def features(request):
    contexto = {"object_list": Features.objects.all()}
    return render(request, "Walkly/features.html", contexto)

class FeaturesList(LoginRequiredMixin, ListView):
    model= Features

class FeaturesCreate(LoginRequiredMixin, CreateView):
    model = Features
    fields = ["title", "description", "icon"]
    success_url= reverse_lazy("features")

class FeaturesUpdate(LoginRequiredMixin, UpdateView):
    model = Features
    fields = ["title", "description", "icon"]
    success_url = reverse_lazy("features")

class FeaturesDelete(LoginRequiredMixin, DeleteView):
    model = Features
    success_url = reverse_lazy("features")


#__ Subscribe
def subscribe(request):
    subscribes = Subscribe.objects.all()

    for subscribe in subscribes:
        subscribe.features_list = subscribe.features_list()

    contexto = {"subscribe": subscribes}
    return render(request, "Walkly/subscribe.html", contexto)

class SubscribeList(LoginRequiredMixin, ListView):
    model= Subscribe

class SubscribeCreate(LoginRequiredMixin, CreateView):
    model = Subscribe
    fields = ["plan_name", "price", "features"]
    success_url= reverse_lazy("subscribe")

class SubscribeUpdate(LoginRequiredMixin, UpdateView):
    model = Subscribe
    fields = ["plan_name", "price", "features"]
    success_url = reverse_lazy("subscribe")

class SubscribeDelete(LoginRequiredMixin, DeleteView):
    model = Subscribe
    success_url = reverse_lazy("subscribe")


#__ Review

def review(request):
    contexto = {"review": Review.objects.all()}
    return render(request, "Walkly/review.html", contexto)

        #__ Review Formulario
@login_required
def reviewForm(request):
    if request.method == "POST":
        miForm = ReviewForm(request.POST)
        if miForm.is_valid():
            review_customer_name = miForm.cleaned_data.get("customer_name")
            review_profession_name = miForm.cleaned_data.get("profession_name")
            review_review_text = miForm.cleaned_data.get("review_text")
            review = Review(customer_name=review_customer_name, profession_name= review_profession_name, review_text= review_review_text)
            review.save()
            contexto = {"review": Review.objects.all()}
            return render(request, "Walkly/review.html", contexto)
        
    else: 
        miForm = ReviewForm()

    return render(request, "Walkly/reviewForm.html", {"form": miForm})

@login_required
def reviewUpdate(request, id_review):
    review = Review.objects.get(id=id_review)
    if request.method == "POST":
        miForm = ReviewForm(request.POST)
        if miForm.is_valid():
            review.customer_name = miForm.cleaned_data.get("customer_name")
            review.profession_name = miForm.cleaned_data.get("profession_name")
            review.review_text = miForm.cleaned_data.get("review_text")
            review.save()
            contexto = {"review": Review.objects.all()}
            return render(request, "Walkly/review.html", contexto)
    else:
        miForm = ReviewForm(initial={"customer_name": review.customer_name, "profession_name": review.profession_name, "review_text": review.review_text})

    return render(request, "Walkly/reviewForm.html", {"form": miForm})

@login_required
def reviewDelete(request, id_review):
    review = Review.objects.get(id=id_review)
    review.delete()
    contexto = {"review": Review.objects.all()}
    return render(request, "Walkly/review.html", contexto)


#__ Contact Us
def contact_us(request):
    contexto = {"contact_us": Contact_Us.objects.all()}
    return render(request, "Walkly/contact_us.html", contexto)    

class Contact_UsList(LoginRequiredMixin, ListView):
    model= Contact_Us

class Contact_UsCreate(LoginRequiredMixin, CreateView):
    model = Contact_Us
    fields = ["name", "email", "subject", "message" ]
    success_url= reverse_lazy("contact_us")

class Contact_UsUpdate(LoginRequiredMixin, UpdateView):
    model = Contact_Us
    fields = ["name", "email", "subject", "message" ]
    success_url = reverse_lazy("contact_us")

class Contact_UsDelete(LoginRequiredMixin, DeleteView):
    model = Contact_Us
    success_url = reverse_lazy("contact_us")


#__ Buscar

def searchSubscribe(request):
    return render(request, "Walkly/search.html")

def findSearch(request):
    patron = request.GET.get('search', '')  # Usamos get() para evitar MultiValueDictKeyError

    if patron:  # Verificamos si se proporcionó un término de búsqueda
        subscription = Subscribe.objects.filter(plan_name__icontains=patron)
        contexto = {'subscribe': subscription, 'query': patron}
    else:
        contexto = {'subscribe': Subscribe.objects.all()}

    return render(request, "Walkly/subscribe.html", contexto)

#__ LogIn, Logout, Register

def loginRequest(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)

            ## find avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar= "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar



            return render(request, "Walkly/index.html")
        else:
            return redirect(reverse_lazy('login'))
            
    else:
        miForm = AuthenticationForm()

    return render(request, "Walkly/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        miForm = RegisterForm(request.POST)
        if miForm.is_valid():
            username = miForm.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                error_message = "El nombre de usuario ya está en uso."
                return render(request, "Walkly/register.html", {"form": miForm, "error_message": error_message})
            
            
            miForm.save()
            return redirect(reverse_lazy('home'))
            
    else:
        miForm = RegisterForm()

    return render(request, "Walkly/register.html", {"form": miForm})


#___ Profile's edition
@login_required
def editProfile(request):
    username =  request.user
    if request.method == "POST":
        miForm= UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username = username)
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.email = miForm.cleaned_data.get("email_name")
            miForm.save()
            return redirect(reverse_lazy('home'))
        
    else:
        miForm = UserEditForm(instance = username)

    return render(request, "Walkly/editProfile.html", {"form": miForm})

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "Walkly/change_password.html"
    success_url = reverse_lazy("home")

#__ Add Avatar
@login_required
def addAvatar(request):
    if request.method == "POST":
        miForm= AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            username = User.objects.get(username = request.user)
            imagen = miForm.cleaned_data["imagen"]
            #Delete old avatar
            avatarViejo = Avatar.objects.filter(user=username)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            #____ save avatar 
            avatar = Avatar(user=username, imagen=imagen)
            avatar.save()

             #____ sent avatar to home

            imagen = Avatar.objects.get(user=username).imagen.url
            request.session["avatar"]= imagen

            return redirect(reverse_lazy("home"))
        
    else:
        miForm = AvatarForm()
    return render(request, "Walkly/addAvatar.html", {"form": miForm})