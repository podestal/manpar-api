from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('dishes', views.DishViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = router.urls