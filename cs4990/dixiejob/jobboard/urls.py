from django.conf.urls import patterns, url

from jobboard import views 

urlpatterns = patterns('',
	url(r'^$', views.PostList.as_view(), name='post-list'),
	url(r'^jobboard/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post-detail'),
	url(r'^company/(?P<pk>\d+)/$', views.CompanyDetail.as_view(),name='company-detail'),
	url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetail.as_view(),name='profile-detail'),
	url(r'^employer/(?P<pk>\d+)/$', views.EmployerDetail.as_view(),name='employer-detail'),
	
	url(r'^loged_in/(?P<pk>\d+)/$', views.LogedIn,name='loged-in'),
)	


#from django.conf.urls import defaults, patterns, include, url
#from django.conf import settings
#from django.conf.urls.static import static
#from django.views.generic import DetailView, ListView
#from jobboard.models import Post, Employer, Employee

#url(r'^employeecreate/(?P<pk>\d+)/$',EmployeeCreate.as_view(), name='employeecreate', template_name='jobboard/profile.html'),
	
#url(r'^jobboard/(?P<employer_id>\d+)/$', views.company, name='company'),
#url(r'^company/(?P<employer_id>\d+)/$', views.company, name='company'),
#url(r'^detail/(?P<job_id>\d+)/$', views.detail, name='detail'),
#url(r'^detail/(?P<pk>\d+)/$', DetailView.as_view(model=Job, template_name='detail')),
#url(r'^profile/(?P<user_id>\d+)/$',views.profile, name='profile'),
#url(r'^accounts/register/employer/$',views.employerregister, name='employerregister'),
	#url(r'^profile/(?P<pk>\d+)/$',
		#DetailView.as_view(
		#model=Employee,
		#context_object_name='profiledetail',
		#template_name='jobboard/profile.html')),
