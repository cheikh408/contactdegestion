
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Contact(models.Model):
     
    nom = models.CharField(max_length=30)  
    prenom = models.CharField(max_length=30)  
    telephone = models.CharField(max_length=10)  
    mail = models.EmailField(max_length=50,blank=True,null=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete= models.CASCADE)
    archive= models.BooleanField(default=False)



    def __str__(self):
        return "{} {}".format(self.nom,self.prenom)



    def  get_absolute_url(self):
        
        return reverse('contact_detail', kwargs={'id': self.id})    


