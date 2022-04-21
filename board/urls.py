from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.board_paging, name='board'),
    path('write/', views.board_write, name='write'),
    path('detail/<int:pk>/', views.board_detail, name='board_detail'),
    path('detail/edit/<int:pk>/', views.board_edit, name='edit'),
    path('notice/', views.notice_boardpaging, name='notice'),
    path('notice_detail/<int:pk>/',views.notice_detail, name = 'notice_detail'),
]
