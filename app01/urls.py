from django.conf.urls import url
from app01 import views

urlpatterns = [

    url(r'^infos/$',views.RmoteConnectionInfo.as_view(), name="infos"),
    url(r'^infos/list$', views.RmoteConnectionInfoList.as_view(), name="infos-list"),
    url(r'^infos/detail$', views.RmoteConnectionInfoDetail.as_view(), name="infos-detail"),
    url(r'^infos/delete$', views.RmoteConnectionInfoDelete.as_view(), name="infos-delete"),
    url(r'^infos/add$', views.RmoteConnectionInfoAdd.as_view(), name="infos-add"),
    # url(r'^infos/login/', views.RmoteConnectionInfoLogin.as_view(), name="infos-login"),

]