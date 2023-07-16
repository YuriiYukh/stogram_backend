from rest_framework import generics, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Poster, Post, Vote
from .serializers import PosterSerializer, PostSerializer, VoteSerializer


class UserInfo(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = ('user_id')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserPosts(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        user_posts = Post.objects.filter(id=kwargs['id']).order_by('created')
        serializer = PostSerializer(user_posts, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostVotes(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs['post_id'])
        return Vote.objects.filter(post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('Already voted')
        serializer.save(voter=self.request.user, post=Post.objects.get(
            id=self.kwargs['post_id']))
