from os import stat
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPwdChangeForm,MyPwdResetForm,MySetPwdForm

urlpatterns = [
    #----------------------------- Home Page -----------------------------------
    path('', views.ProductView.as_view(), name="home"),    
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),

    path('cartbadge/', views.cart_badge),
    
    #------------------------------ Filter --------------------------------------
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),    

    #-------------------------------Profile --------------------------------------
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    
    path('orders/', views.orders, name='orders'),
    # cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removeitem/', views.remove_item_in_cart),

    path('buy/', views.buy_now, name='buy-now'),
    path('checkout/', views.checkout, name='checkout'),
    # Paytm intigration API
    path('initiate-payment/', views.initiate_payment, name="initiate_payment"),
    path('paytmSuccess/', views.paytmSuccess, name="paytmSuccess"),
    path('paymentdone/', views.payment_done, name="paymentdone"),

    # --------------- Manage Account(Using Django provided view) -----------------------------------
    # User sign-Up
    path('registration/', views.CustomerRegisterationView.as_view(), name='customerregistration'),
    # User Login
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name="login"),
    # USer Logout
    path('logout/', auth_view.LogoutView.as_view(next_page="login"), name="logout"),    
    # Password Change
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPwdChangeForm, success_url='/pwdchangedone/'), name='passwordchange'),
    path('pwdchangedone/', auth_view.PasswordChangeView.as_view(template_name='app/pwdchangedone.html'), name="pwdchangedone"),
    
    # -------------------Resetting Password(E-mail Authentication) ------------------------------------
    # Password Reset
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name="app/pwd_reset.html", form_class=MyPwdResetForm), name='password-reset'),    
    # password reset done
    path('pwd-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name='password_reset_done'),    
    # Password reset confirm
    path('pwd-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=MySetPwdForm), name='password_reset_confirm'),
    # Password Reset Complete
    path('pwd-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name="app/pwd_reset_complete.html"), name='password_reset_complete'),
    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
