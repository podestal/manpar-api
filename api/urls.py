from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('dishes', views.DishViewSet)

dishes_router = routers.NestedDefaultRouter(router, 'dishes', lookup='dishes')
dishes_router.register('images', views.DishImageViewSet, basename='dish-images')

router.register('categories', views.CategoryViewSet)
router.register('tables', views.TableViewSet)
router.register('orders', views.OrderViewSet)
router.register('order-items', views.OrderItemViewSet)

urlpatterns = router.urls + dishes_router.urls