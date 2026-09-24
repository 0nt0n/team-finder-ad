from django.db import models

from users.models import User

# Create your models here.


class Project(models.Model):
    """Модель проекта"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Узнать насчет получения по юзеру
    created_at = models.DateField()
    github_url = models.URLField()
    status = models.CharField(
        max_length=6, choices=[("open", "Open"), ("closed", "Closed")]
    )
    participants = models.ManyToManyField(
        User, blank=True
    )  # также проработать получение
#    skills = ... # свзяь табличек


class Skill(models.Model):
    name = models.CharField(max_length=124)
