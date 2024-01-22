from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListingListView.as_view()),
    path('search', views.SearchListingView.as_view()),
    path('<slug>', views.ListingView.as_view()),
]
