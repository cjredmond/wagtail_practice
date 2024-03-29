from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from user_authentication import views as auth_views
from pick import views as pick_views

router = routers.DefaultRouter()
router.register(r'api/leagues', pick_views.LeagueViewSet)
router.register(r'api/teams', pick_views.TeamViewSet)
router.register(r'api/games', pick_views.GameViewSet)
router.register(r'api/user_picks', pick_views.UserPickViewSet)

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^comments/', include('django_comments.urls')),

    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^test/', auth_views.TestView.as_view(), name='test_view'),

    url(r'^signup/', auth_views.signup, name='signup'),

    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
