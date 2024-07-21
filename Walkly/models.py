from django.db import models
from django.contrib.auth.models import User

# Create models 
class Features(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100)  #  this to store the name of an icon class if using an icon library

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()  # List of features included in the plan

    def __str__(self):
        return self.plan_name
    def features_list(self):
        return self.features.split('\n')
    

class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    profession_name = models.CharField(max_length=100)
    review_text = models.TextField()

    class Meta:
        ordering = ["customer_name"]
    
    def __str__(self):
        return f"{self.customer_name}"

class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    class Meta:
        verbose_name = "Contact u"
        verbose_name_plural = "Contact us"

    def __str__(self):
        return f"{self.name}- {self.email}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"