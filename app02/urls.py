from django.conf.urls import url

from app02 import views

urlpatterns = [

    url(r'^xxinfo/$', views.App02List.as_view(), name="xxinfo"),
    url(r'^xxinfo/list$', views.App02ListShixian.as_view(), name="xxinfo-list"),

]
