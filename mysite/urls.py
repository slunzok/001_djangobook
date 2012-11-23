from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    url(r'^$', 'homepage'),
    url(r'^hello/$', 'hello'),
    url(r'^time/$', 'current_time'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^ua1/$', 'ua_display_good1'),
    url(r'^ua2/$', 'ua_display_good2'),
    url(r'^meta/$', 'display_meta'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('books.views',
    # url(r'^search-form/$', views.search_form), (removed)
    url(r'^search/$', 'search'),
)

urlpatterns += patterns('contact.views',
    url(r'^contact/$', 'contact'),
    url(r'^contact/thanks/$', 'contact_thanks'),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
)

urlpatterns += patterns('accounts.views',
    url(r'^accounts/register/$', 'register'),
)
