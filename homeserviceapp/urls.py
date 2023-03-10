from django.urls import path

from homeserviceapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('login_page',views.login_page,name="login_page"),
    path('admin_page',views.admin_page,name="admin_page"),
    path('register',views.register,name="register"),
    path('worker',views.worker,name="worker"),
    path('user',views.user,name="user"),
    path('userregister',views.userregister,name="userregister"),
    path('workerregister',views.workerregister,name="workerregister"),
    path('viewuser',views.viewuser,name="viewuser"),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    path('viewworker',views.viewworker,name="viewworker"),
    path('delete_worker/<int:id>/',views.delete_worker,name='delete_worker'),
    path('update_worker/<int:id>/',views.update_worker,name='update_worker'),
    path('viewworkeruser',views.viewworkeruser,name='viewworkeruser'),
    path('workershedule',views.workershedule,name='workershedule'),
    path('addworkershedule',views.addworkershedule,name='addworkershedule'),
    path('sheduleview',views.sheduleview,name='sheduleview'),
    path('update_shedule/<int:id>/',views.update_shedule,name='update_shedule'),
    path('delete_shedule/<int:id>/',views.delete_shedule,name='delete_shedule'),
    path('viewworkershedule',views.viewworkershedule,name='viewworkershedule'),
    path('addworkmanagement',views.addworkmanagement,name='addworkmanagement'),
    # path('addappointment',views.addappointment,name='addappointment'),
    path('viewappointment',views.viewappointment,name='viewappointment'),
    path('addfeedbacks',views.addfeedbacks,name='addfeedbacks'),
    path('viewfeedbacks',views.viewfeedbacks,name='viewfeedbacks'),
    path('viewworkmanagement',views.viewworkmanagement,name='viewworkmanagement'),
    path('update_workmanagement/<int:id>/',views.update_workmanagement,name='update_workmanagement'),
    path('delete_workmanagement/<int:id>/',views.delete_workmanagement,name='delete_workmanagement'),
    path('user_appointment/<int:id>/',views.user_appointment,name='user_appointment'),
    path('appointment_view',views.appointment_view,name='appointment_view'),
    path('appointment_viewworker',views.appointment_viewworker,name='appointment_viewworker'),
    path('appointment_viewadmin',views.appointment_viewadmin,name='appointment_viewadmin'),
    path('approve_appointment/<int:id>/',views.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<int:id>/',views.reject_appointment,name='reject_appointment'),
    path('admin_replay/<int:id>/',views.admin_replay,name='admin_replay'),
    path('feedbackview',views.feedbackview,name='feedbackview'),
    path('addpayments',views.addpayments,name='addpayments'),
    path('viewpayments',views.viewpayments,name='viewpayments'),
    path('pay_now/<int:id>/',views.pay_now,name='pay_now'),
    path('pay_direct/<int:id>/',views.pay_direct,name='pay_direct'),
    path('userpayment_view',views.userpayment_view,name='userpayment_view'),
    path('pay_bttn',views.pay_bttn,name='pay_bttn'),
    path('wrkr_paymentview',views.wrkr_paymentview,name='wrkr_paymentview'),
    path('logout_view',views.logout_view,name='logout_view'),

]
