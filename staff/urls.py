from django.urls import path
from . import views

'''
    Staff endpoints
'''

urlpatterns = [
    path('', views.StaffListAPIView.as_view(), name='list_staffs'),
    path('create/', views.StaffCreateAPIView.as_view(), name='create_staff'),
    path('edit/<int:pk>/', views.StaffUpdateAPIView.as_view(), name='edit_staff'),
    path('<int:pk>/', views.StaffRetrieveAPIView.as_view(), name='retrieve_staff'),
    path('delete/<int:pk>/', views.StaffDestroyAPIView.as_view(), name='delete_staff'),
]