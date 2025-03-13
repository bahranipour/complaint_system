from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.complaint_list, name='complaint_list'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('detail/<int:complaint_id>/', views.complaint_detail, name='complaint_detail'),
    path('edit/<int:complaint_id>/', views.edit_complaint, name='edit_complaint'),
    path('delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
]