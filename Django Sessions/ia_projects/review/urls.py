from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload),
    path('list/', views.ReviewListView.as_view(), name='list-review'),
    path('create/', views.ReviewCreateView.as_view(), name='create-review'),
    path("favorite/", views.AddFavoriteView.as_view(), name="add-favorite"),
    path("favorite-delete/<int:id>", views.delete_favorite, name="delete-favorite"),
]
