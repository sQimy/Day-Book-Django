"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics list
    path('topics/', views.topics, name='topics'),
    # Detalied page about Topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for creating new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for creating new Entry of Topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry')

]