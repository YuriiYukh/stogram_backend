from rest_framework import serializers
from .models import Poster, Post, Vote


class PosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poster
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
