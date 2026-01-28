from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


from .views import (
    PostViewSet, GroupViewSet, CommentListView, CommentDetailView
)


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/posts/<int:post_id>/comments/',
         CommentListView.as_view(), name='comment-list'),
    path('v1/posts/<int:post_id>/comments/<int:comment_id>/',
         CommentDetailView.as_view(), name='comment-detail'),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
