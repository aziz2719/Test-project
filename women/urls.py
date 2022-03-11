from rest_framework.routers import SimpleRouter

from women.views import WomenViewSet, GenreView, CategoryView


router = SimpleRouter()
router.register('women', WomenViewSet, basename='women')
router.register('genre', GenreView, basename='genre')
router.register('category', CategoryView, basename='category')

urlpatterns = []

urlpatterns += router.urls
print(router.urls)