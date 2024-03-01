from django.shortcuts import render
from .models import Annonce, Commentaire  # Import correct pour les modèles

# Create your views here.

def blog(request):

    annonces = Annonce.objects.all()
    commentaire = Commentaire.objects.all()
   

    datas = {
        'annonces': annonces,
        'commentaire': commentaire,
       
    }

    return render(request, 'blog.html', datas)