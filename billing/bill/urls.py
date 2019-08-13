from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name="home"),
     path('confirm/<user>',views.confirm,name='confirm'),
     path('signup',views.signup,name="signup-form"),
     path('login',views.Login,name='login-form'),
     path('main/<username>',views.Official,name="main-page"),
     path('dashboard/<username>/<month>',views.dashboard,name="dashboard"),
     path('logout/<user>',views.logout,name='logout'),
     path('amount/<user>/add',views.add,name="add-amount"),
     path('amount/delete/<int:id>/<user>',views.delete,name='delete'),
     path('remind/<user>/bill',views.Remind,name="remind"),
     path('remind/paid/<int:id>/<user>',views.Paid,name="paid"),
     path('show/remind/<user>/all',views.show,name="show_all")

]
