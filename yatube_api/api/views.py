from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Post, Comment, Group, User
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, UserSerializer
)
from .permissions import AuthorOnly


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post=post_id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_pk'))
        serializer.save(post=post, author=self.request.user)
