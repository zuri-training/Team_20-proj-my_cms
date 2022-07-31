from uuid import uuid4

from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib import admin
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import PublishedManager


def upload_to(instance, filename):
    return "posts/{filename}".format(filename=filename)


User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post_category"
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250, blank=True, null=True, unique_for_date="publish"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    post = RichTextField(blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=upload_to, blank=True, null=True)
    # image = CloudinaryField("image")
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="draft")
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ["-publish"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_user"
    )
    comment = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
