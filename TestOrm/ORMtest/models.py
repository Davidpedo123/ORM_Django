from pickle import TRUE
from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class djangoUser(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=250, null=True)
    password = models.CharField(max_length=8, null=True)

    def save(self, *args, **kwargs):
        # Valida la contraseña
        try:
            validate_password(self.password)
        except ValidationError as e:
            # Maneja el error de validación aquí
            pass

        # Encripta la contraseña y guarda el objeto
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
