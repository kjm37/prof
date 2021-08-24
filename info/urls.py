

from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('form',views.update,name='form'),
    path('message',views.send_message,name='message'),
    path('gallary',views.gallary,name='gallary'),
    path('gal/<int:id>',views.del_galary,name='delete_gal'),
    path('add_image',views.add_image,name='add_image'),
    path('add_service',views.ser,name='ser'),
    path('del_service/<int:id>',views.del_ser,name='del_ser'),
    path('add_ser',views.add_ser,name='add_ser'),
    path('add_skil000l',views.skills,name='skills'),
    path('del_skill/<int:id>',views.del_skill,name='del_skill'),
    path('add_sk',views.add_skill,name='add_skill'),
    path('add_comment',views.commentx,name='comment'),
    path('del_comment/<int:id>',views.del_comment,name='del_comment'),
    path('add_commentsssss',views.add_comment,name='add_comment'),
]
