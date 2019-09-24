from rest_framework_mongoengine import routers
from crmsystem2.views import EmployeeView

router = routers.DefaultRouter()
router.register(r'crmsystem2', EmployeeView)

urlpatterns = []
urlpatterns += router.urls


