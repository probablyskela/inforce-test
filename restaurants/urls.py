from django.urls import path
from restaurants import views

urlpatterns = [
    path("restaurants/", views.RestaurantList.as_view(), name="restaurant-list"),
    path("restaurants/<int:pk>/", views.RestaurantDetail.as_view(), name="restaurant-details"),
    path("restaurants/<int:pk>/menus/", views.MenusList.as_view(), name="menus-list"),
    path("menus/<int:pk>/", views.MenuDetail.as_view(), name="menus-detail"),
    path("offers/", views.CurrentMenusList.as_view(), name="offers"),
    path("offers/result/", views.CurrentMenusDetail.as_view(), name="oferrs-result"),
    path("offers/<int:pk>/vote/", views.VoteDetail.as_view(), name="offers-vote"),
    path("dishes/", views.DishList.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", views.DishDetail.as_view(), name="dishes-list"),
]
