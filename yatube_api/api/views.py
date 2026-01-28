from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)


from posts.models import Post, Comment, Group, User
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, UserSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied()
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied()
        instance.delete()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        comments = Comment.objects.filter(post=post_id)
        return comments

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        comments = Comment.objects.filter(post=post_id, id=comment_id)
        return comments

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied()
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied()
        instance.delete()
