
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'department', DepartmentView)
router.register(r'author', AuthorView)
router.register(r'student', StudentView)
router.register(r'book', BookView)
router.register(r'issuebook', IssueBookView)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/department', DepartmentView.as_view())
]
