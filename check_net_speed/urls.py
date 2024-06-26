from django.urls import path
from check_net_speed import views

urlpatterns = [
    path('home', views.Home.as_view(), name='home'),
    path('ping', views.Ping.as_view(), name='check_ping'),
    path('check-download', views.DownloadSpeed.as_view(), name='check_down'),
    path('check-upload', views.UploadSpeed.as_view(), name='check_upload'),
    path('openspeedtest', views.OpenSpeedTest.as_view(), name='openspeedtest'),

    path('internet-speed-details', views.UserInternetSpeed.as_view(), name='user-details'),
]