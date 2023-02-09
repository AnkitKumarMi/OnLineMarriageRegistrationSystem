from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from marriage.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="home"),
    path('login', Login,name="login"),
    path('logout/', Logout,name="logout"),
    path('login_admin', Admin_Login,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('user_home', User_Home,name="user_home"),
    path('search_marriage_application', Search_Registration,name="search_marriage_application"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('registration', Marriage_Registration,name="registration"),
    path('view_registration', View_Registration_Application,name="view_registration"),
    path('verified_application', View_Verified_Application,name="verified_application"),
    path('all_application', View_All_Application,name="all_application"),
    path('registration_detail(<int:pid>)', registration_detail,name="registration_detail"),
    path('assign_status(<int:pid>)', Assign_Status,name="assign_status"),
    path('rejected_application', View_Rejected_Application,name="rejected_application"),
    path('search_report', Search_Report,name="search_report"),
    path('change_password', Change_Password,name="change_password"),
    path('new_application', View_New_Application,name="new_application"),
    path('pdf/', GeneratePdf.as_view()),
    path('get_invoice(<int:book_id>)', get2, name="get_invoice"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
