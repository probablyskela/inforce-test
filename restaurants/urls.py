from django.urls import path
from restaurants import views

urlpatterns = [
    path("restaurants/", views.RestaurantList.as_view()),
    path("restaurants/<int:pk>/", views.RestaurantDetail.as_view()),
    path("restaurants/<int:pk>/menus/", views.MenusList.as_view()),
    path("menus/<int:pk>/", views.MenuDetail.as_view()),
    path("offers/", views.CurrentMenusList.as_view()),
    path("offers/result/", views.CurrentMenusDetail.as_view()),
    path("offers/<int:pk>/vote/", views.VoteDetail.as_view()),
    path("dishes/", views.DishList.as_view()),
    path("dishes/<int:pk>/", views.DishDetail.as_view()),
]
