from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name="home"),
     path('confirm/<user>',views.confirm,name='confirm'),
     path('signup',views.signup,name="signup-form"),
     path('login',views.Login,name='login-form'),
     path('dashboard/<username>',views.dashboard,name="dashboard"),
     path('logout/<user>',views.logout,name='logout'),
     path('amount/<user>/add',views.add,name="add-amount"),
     path('amount/delete/<int:id>/<user>',views.delete,name='delete')

]
