from django.urls import path
from teachers.views import TeachersViews, TeacherViews


urlpatterns = [
    path('', TeachersViews.as_view(), name='teachers'),
    path('teacher/<int:pk>/', TeacherViews.as_view(), name='teacher'),
]
