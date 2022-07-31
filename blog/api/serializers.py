from rest_framework import serializers
from blog.models import Post, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment"]

    def create(self, validated_data):
        post_id = self.context["post_id"]
        return Post.objects.create(post_id=post_id, **validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "category",
            "title",
            "slug",
            "user",
            "image",
            "post",
            "comments",
            "status",
        ]
