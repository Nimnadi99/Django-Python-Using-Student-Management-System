from django.urls import path
from . import views

urlpatterns = [
    # get & post request for insert operation
    path('', views.student_form, name='student_add'),
    # get & post request for update operation
    path('student/<int:id>', views.student_form, name='student_update'),
    # get request to retrieve and display all records
    path('student/list', views.student_list, name='student_list'),
    # get request to delete operation
    path('student/delete/<int:id>', views.student_delete, name='student_delete'),
]
