from django.conf.urls import url

from amovies import views

urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^register/',views.register,name='register'),
    url(r'^dologin/',views.dologin,name='dologin'),
    url(r'^doregister/',views.doregister,name='doregister'),
    url(r'^home/',views.home,name='home'),
    url(r'^userinfo/',views.userinfo,name='userinfo'),
    url(r'^douserinfo/',views.douserinfo,name='douserinfo'),
    url(r'^home_logined/',views.home_logined,name='home_logined'),
    url(r'^home_logined_collected/',views.home_logined_collected,name='home_logined_collected'),
    url(r'^addtomycollect/',views.addtomycollect,name='addtomycollect'),
    url(r'^delmycollect/',views.delmycollect,name='delmycollect'),
]