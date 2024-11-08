from rest_framework.routers import DefaultRouter

from src.structure_management.views import DepartmentViewSet, PositionViewSet, EmployeeViewSet, PermissionViewSet

router = DefaultRouter()

router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = router.urls