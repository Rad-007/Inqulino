from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('faq',views.faq,name='faq'),
    path('blog',views.blog,name='blog'),
    path('error',views.error,name='error'),
    path('team',views.team,name='team'),
    path('charts',views.charts,name='charts'),
    path('pricing',views.pricing,name='pricing'),
    path('contact',views.contact,name='contact'),
    path('pay',views.pay,name='pay'),
    path('borrow',views.borrow,name='borrow'),
    path('lend',views.lend,name='lend'),
    path('profile',views.profile,name='profile'),
    path('eth_borrow',views.eth_borrow,name='eth_borrow'),
    path('eth_lend',views.eth_lend,name='eth_lend'),
    path('phonepe',views.phonepe,name='phonepe'),
    #path('home/', views.ProductListView.as_view(), name='home'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('detail/<id>/', views.ProductDetailView.as_view(), name='detail'),
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('failed/', views.PaymentFailedView.as_view(), name='failed'),
    path('history/', views.OrderHistoryListView.as_view(), name='history'),
    path('stripe_check', views.HomePageView.as_view(), name='stripe_check'),
    path('create_checkout_session', views.create_checkout_session, name='create_checkout_session'),
    #path('stripe_charge/', views.charge, name='stripe_charge'),
    path('charge/', views.charge, name='charge'),
    #path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),





]