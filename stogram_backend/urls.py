from django.contrib import admin
from django.urls import path
from stogram_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/<int:user_id>', views.UserInfo.as_view()),
    path('api/user_posts/<int:id>', views.UserPosts.as_view()),
    path('api/votes/<int:post_id>', views.PostVotes.as_view()),
]
