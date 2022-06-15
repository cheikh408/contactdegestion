from django.shortcuts import render,get_object_or_404,redirect
from repertoire.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from repertoire.models import Contact
from django.forms import ModelForm




class ContactForm(ModelForm):
 class Meta:
  model = Contact 
  fields =("nom","prenom","telephone","mail")    
@login_required
def  index (request): 
  contact_form = ContactForm()
  
  if request.method == "POST":  
    auteur = request.user
    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")        
    mail = request.POST.get("mail")  
    telephone = request.POST.get("telephone")
 
    contact= Contact.objects.create(
      auteur=auteur,
      nom=nom,
      prenom=prenom,
      mail=mail,
      telephone=telephone)

    contact.save()
    messages.success(request,"contact créer avec succés")
            
      
  return render(request, "repertoire/index.html",{"contact_form":contact_form})



@login_required
def contactlist(request):

    contacts = Contact.objects.filter(archive=False) 
    return render(request, 'repertoire/contactlist.html',{"contacts":contacts})  


def contact_detail(request, id):

   contact = get_object_or_404(Contact, id = id) 

   

   return render(request,"repertoire/detail_contact.html",{"contact":contact})



def contact_update(request,id):
    contact_form = ContactForm()
    contact = get_object_or_404(Contact ,  id=id)
    if request.method == "POST":  
     nom = request.POST.get("nom")
     prenom = request.POST.get("prenom")        
     mail = request.POST.get("mail")  
     telephone = request.POST.get("telephone")
     contact_update= Contact.objects.filter(id = contact.id)
     contact_update.update( 
       nom=nom,
       prenom=prenom,
       mail=mail,
       telephone=telephone)
     return redirect ("contact")

      
    return render(request,"repertoire/contact_edit.html" , {"contact":contact,"contact_form":contact_form})

def contact_delete(request,id):
   
    contact = get_object_or_404(Contact ,  id=id)
    if request.method == "POST":
        contact_delete= Contact.objects.filter(id = contact.id)
        contact_delete.update(
          archive=True
        )
       # contact.delete()
        return redirect ("contact")
    return render(request,"repertoire/contact_delete.html",{"contact":contact})
