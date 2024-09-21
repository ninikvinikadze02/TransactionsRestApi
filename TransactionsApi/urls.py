from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from transactions.views import TransactionViewSet, UserPurchasesView, ProductPurchasesView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Set up the router for your existing views
router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)

# Schema view for Swagger and Redoc
schema_view = get_schema_view(
    openapi.Info(
        title="Transactions API",
        default_version='v1',
        description="API for handling transactions data",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user-purchases/<str:user_id>/', UserPurchasesView.as_view(), name='user-purchases'),
    path('api/product-purchases/<str:item_code>/', ProductPurchasesView.as_view(), name='product-purchases'),
    # Swagger and ReDoc Endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]