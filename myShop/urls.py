from django.urls import path
from . import views

urlpatterns = [
    path('',views.category_list,name='home_page'),
    path('category/<int:id>/',views.category)
]