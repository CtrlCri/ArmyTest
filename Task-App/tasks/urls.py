from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register('api/tasks', views.TaskView, 'tasks')

urlpatterns = router.urls