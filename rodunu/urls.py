from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'rodunu.recipe.views.index'),
    (r'^recipe/add/$', 'rodunu.recipe.views.add'),
    (r'^recipe/(?P<recipe_key>[^\.^/]+)/$', 'rodunu.recipe.views.view'),
    # Example:
    # (r'^rodunu/', include('rodunu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
