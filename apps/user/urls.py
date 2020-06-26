from django.urls import path,re_path
from user.views import RegisterView,ActiveView,LoginView,LogoutView,UserInfoView,UserOrderView,AddressView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),  # 注册页面
    re_path(r'^active/(.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    path('login', LoginView.as_view(), name='login'),  # 登录页面
    path('logout',LogoutView.as_view(), name='logout'),  # 注销登录

    re_path(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    re_path(r'order/(?P<page>\d+)', UserOrderView.as_view(), name='order'),  # 用户中心-订单页面
    path('address/', AddressView.as_view(), name='address'),  # 用户中心-地址页
]