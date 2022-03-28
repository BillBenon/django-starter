from django.urls import path
from adv_cbv import views

app_name = 'adv_cbv'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<pk>', views.SchoolDetailView.as_view(), name='detail')
]