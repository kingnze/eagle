from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('rooms',views.rooms,name='rooms'),
    path('<int:room_id>',views.room,name='room'),
    path('whoweare/<slug:slug_id>/',views.whowearedetail,name='whowearedetail'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('bookings',views.bookings,name='bookings'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('blog/<slug:slug_id>/',views.blogdetail,name='blogdetail'),
    path('gallery',views.gallery,name='gallery'),
    path('dining',views.dining,name='dining'),
    path('spa',views.spa,name='spa'),
    path('meeting',views.meeting,name='meeting'),
    path('ourservice',views.ourservice,name='ourservice'),
    path('whoweare',views.whoweare,name='whoweare'),
    path('ourservice_1',views.ourservice_1,name='ourservice_1'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    path('myCart/',views.myCart,name='myCart'),
    path('manageCart/<int:id>/',views.manageCart,name='manageCart'),
    path('emptyCart/',views.emptyCart,name='emptyCart'),
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('transfer/',views.transferPage,name='transfer'),
    path('payment/<int:id>/',views.paymentPage,name='payment'),
    path('<str:ref>/',views.verify_payment,name='verify-payment'),
    path('profile',views.profile,name='profile'),

]
