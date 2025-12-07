from django.contrib import admin
from django.urls import include, path
from town.views import CustomLoginView

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user management
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include("django.contrib.auth.urls")),
    
    #main
    path('', include('town.urls'))
]
