from django.urls import path
from . import views

'''
    Client endpoints
'''

urlpatterns = [
    path('', views.ClientListAPIView.as_view(), name='list_clients'),
    path('create/', views.ClientCreateAPIView.as_view(), name='create_client'),
    path('edit/<int:pk>/', views.ClientUpdateAPIView.as_view(), name='edit_client'),
    path('<int:pk>/', views.ClientRetrieveAPIView.as_view(), name='retrieve_client'),
    path('delete/<int:pk>/', views.ClientDestroyAPIView.as_view(), name='delete_client'),
]