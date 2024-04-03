from django.urls import path
from . import views


urlpatterns = [
    path('Login/', views.Login, name='Login'),
    path('Register/', views.Register, name='Register'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('Logout/', views.Logout, name='Logout'),
    path('enroll_the_course/', views.enroll_the_course, name='enroll_the_course'),
    path('release_the_course/', views.release_the_course, name='release_the_course'),
]
