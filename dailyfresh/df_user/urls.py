from django.conf.urls import url
import views


urlpatterns = [
    url(r"^$", views.user_center_info),
    url(r"^register/$", views.register),
    url(r"^register_handle/$", views.register_handle),
    url(r"^register_exist/$", views.register_exist),
#          register_exist
    url(r"^login/$", views.login),
    url(r"^login_handle/$", views.login_handle),
    url(r"^info/$", views.user_center_info),
    url(r"^site/$", views.site),
    url(r"^order/$", views.order),
    url(r"^logout/$", views.logout),
    url(r"^user_center_order&(\d+)/$", views.user_center_order),
]