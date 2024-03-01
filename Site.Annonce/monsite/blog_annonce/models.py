from django.db import models
from django.contrib.auth.models import User

class Annonce(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.ImageField(upload_to='annonces/', null=True, blank=True)  # Champ pour l'image de l'annonce
    date_creation = models.DateTimeField(auto_now_add=True)

class Commentaire(models.Model):
    annonce = models.ForeignKey(Annonce, related_name='commentaires', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    image = models.ImageField(upload_to='commentaires/', null=True, blank=True)  # Champ pour l'image du commentaire
    date_creation = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='commentaires_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='commentaires_dislikes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
