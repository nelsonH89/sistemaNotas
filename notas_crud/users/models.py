from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'administrador'),
      (2, 'professor'),
      (3, 'aluno'),
      (4, 'responsavel'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    # Adicione um related_name aos campos groups e user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='',
        related_query_name='customuser',
        related_name='customuser_set',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
        related_name='customuser_set',
    )
