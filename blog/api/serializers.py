from blog.models import Category, Comment, Post
from rest_framework import serializers
# from .models import Post, Comment , Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [   "id", "category",     "title",   "slug",    "user", "image","post","comments",  "status"        ]
    
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment 
        fields = ["id", "user", "comment"]
        
    def create(self, validated_data):
        post_id = self.context["post_id"]
        return Post.objects.create(post_id=post_id, **validated_data)

    
        
    
    