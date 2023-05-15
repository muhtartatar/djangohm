from django.urls import path
from online_school import views
from django.contrib import admin


urlpatterns = [
    path('', views.add_user, name='add_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('choose_course/', views.choose_course, name='choose_course'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('students_list/', views.students_list, name='students_list'),
    path('admin/', admin.site.urls),
]
