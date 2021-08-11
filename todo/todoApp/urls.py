from . import views
from django.urls import path

urlpatterns = [

    path('', views.todo, name='todo'),

    path('delete/<int:taskid>/', views.delete, name='delete'),

    path('update/<int:id>/', views.update, name='update'),

    path('home/', views.listview.as_view(), name='home'),

    path('detail/<int:pk>/', views.detailview.as_view(), name='detail'),

    path('edit/<int:pk>/', views.upadateview.as_view(), name='edit'),

    path('delete1/<int:pk>/', views.deleteview.as_view(), name='delete1')
]
