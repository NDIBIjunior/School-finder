from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email doit être renseignée.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        



class Owner(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    adress = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =  ["first_name","last_name","phone_number","adress"]

    def __str__(self):
        return self.email



class School(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    Neighborhood = models.TextField()
    type = models.CharField(max_length=30, choices=[
        ('Francophone', 'Francophone'),
        ('Anglophone', 'Anglophgone'),
        ('Bilingue','Bilingue'),
    ])
    teaching_type = models.CharField(max_length=30, choices=[
        ('Général','Général'),
        ('Technique','Technique'),
    ])
    description = models.TextField(blank=True,null=True)
    images = models.ImageField(blank=True,null=True)
    videos = models.URLField(blank=True,null=True)
    views_number = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='schools')





class Level(models.Model):
    name = models.CharField(max_length=50)
    prix_pension = models.DecimalField(max_digits=10, decimal_places=2)

    # Relation avec School
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='levels')

    def clean(self):
        if self.prix_pension <= 0:
            raise ValidationError("Le prix de pension doit être supérieur à 0.")

    def __str__(self):
        return f"{self.nom} - {self.school.nom}"

class Exam(models.Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ('Général', 'Général'),
        ('Technique', 'Technique'),
    ])
    series = models.TextField(help_text="Liste des séries, séparées par des virgules") 
    taux_reussite = models.FloatField(default=0.0)


    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='exams')

    def clean(self):
        if not (0 <= self.taux_reussite <= 100):
            raise ValidationError("Le taux de réussite doit être compris entre 0 et 100.")


    def __str__(self):
        return f"{self.nom} - {self.school.nom}"   

