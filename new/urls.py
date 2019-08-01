from django.conf.urls import url
from new import views as views_new
from new import views_one

urlpatterns = [

    url(r'^userinfo/$', views_one.xiangmuGuanli.as_view(), name="userinfo"),
    url(r'^userinfo/list$', views_one.xiangmuGuanliViewList.as_view(), name="userinfo-list"),
    url(r'^userinfo/detail$', views_one.xiangmuGuanliDetail.as_view(), name="userinfo-detail"),
    url(r'^userinfo/delete$', views_one.xiangmuGuanliDelete.as_view(), name="userinfo-delete"),
    url(r'^userinfo/add_users$', views_one.xiangmuGuanliAdd.as_view(), name="userinfo-add_users"),

]
