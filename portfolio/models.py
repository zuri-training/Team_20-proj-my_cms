# The below class is for the Portfolio App.
from tkinter import CASCADE
from unicodedata import name
from django.db import models

from django.contrib.auth import get_user_model

# define user field by importing from django
User = get_user_model()

# Certification Model that returns certification name


class Certification(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    credentialid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Education Model that returns Education name
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    degree_name = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    started_at = models.DateTimeField(blank=True)
    ended_at = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Projects models


class Project(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=255)
    project_url = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Changed this from Jobs to Experience Model


class Experience(models.Model):
    STATUS_CHOICES = (
        ("fulltime", "Full Time"),
        ("parttime", "Part Time"),
        ("selfemployed", "Self Employed"),
        ("freelance", "Free Lance"),
    )
    company_name = models.CharField(max_length=255)
    started_at = models.DateTimeField(blank=True)
    ended_at = models.DateTimeField(blank=True)
    role = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


# skill model


class Skill(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# contact section model


class Contact(models.Model):
    message = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
