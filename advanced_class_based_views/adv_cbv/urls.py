from django.urls import path
from adv_cbv import views

app_name = 'adv_cbv'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<pk>', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<pk>', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.SchoolDeleteView.as_view(), name='delete')
]