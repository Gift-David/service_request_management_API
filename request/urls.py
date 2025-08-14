from django.urls import path
from . import views

urlpatterns = [
    # Service request endpoints
    path('create/', views.ServiceRequestCreateAPIView.as_view(), name='create_requests'),
    path('', views.ServiceRequestListAPIView.as_view(), name='list_requests'),
    path('edit/<int:pk>/', views.ServiceRequestUpdateAPIView.as_view(), name='edit_request'),
    path('<int:pk>/', views.ServiceRequestRetrieveAPIView.as_view(), name='retrieve_request'),
    path('delete/<int:pk>/', views.ServiceRequestDestroyAPIView.as_view(), name='delete_request'),
    # Request note endpoints
    path('notes/', views.RequestNoteListAPIView.as_view(), name='list_notes'),
    path('notes/create/', views.RequestNoteCreateAPIView.as_view(), name='create_note'),
    path('notes/<int:pk>/', views.RequestNoteRetrieveAPIView.as_view(), name='retrieve_note'),
    path('notes/delete/<int:pk>/', views.RequestNoteDestroyAPIView.as_view(), name='delete_note'),
    # Feedback endpoints
    path('feedbacks/', views.FeedbackListAPIView.as_view(), name='list_feedbacks'),
    path('feedbacks/create/', views.FeedbackCreateAPIView.as_view(), name='create_feedback'),
    path('feedbacks/<int:pk>/', views.FeedbackRetrieveAPIView.as_view(), name='retrieve_feedback'),
    path('feedbacks/delete/<int:pk>/', views.FeedbackDestroyAPIView.as_view(), name='delete_feedback'),
]