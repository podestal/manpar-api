from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('dishes', views.DishViewSet)
router.register('images', views.DishImageViewSet)

router.register('categories', views.CategoryViewSet)
router.register('tables', views.TableViewSet)
router.register('orders', views.OrderViewSet)
router.register('order-items', views.OrderItemViewSet)

urlpatterns = router.urls