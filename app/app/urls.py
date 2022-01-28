from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from discussionspace.views import GetDiscussionsByUserID
from events.views import GetEventsByUserID,UpcomingEvents,OfficialEvents,CommunityEvent
from users.views import GetUserView,Signup
from comments.views import CommentsDiscussion
from rest_framework import permissions
from marketplace.views import GetMarketplaceByUserID
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/discussions/userid/', GetDiscussionsByUserID.as_view(), name='Sign up'),
    path('api/v1/marketplace/userid/', GetMarketplaceByUserID.as_view(), name='Sign up'),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/events/userid/', GetEventsByUserID.as_view(), name='Get Events by UserID'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/marketplace/', include('marketplace.urls')),
    path('api/v1/events/', include('events.urls')),
    path('api/v1/discussions/', include('discussionspace.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/announcement/', include('announcement.urls')),
    path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
    path('api/v1/upcoming/events/', UpcomingEvents.as_view(), name='get_user'),
    path('api/v1/official/events/', OfficialEvents.as_view(), name='get_user'),
    path('api/v1/community/events/', CommunityEvent.as_view(), name='get_user'),
    path('api/v1/comments_discussion/', CommentsDiscussion.as_view(), name='get_user'),
    
    
]