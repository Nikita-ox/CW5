from rest_framework.viewsets import ModelViewSet
from ads.views.ads import Category
from ads.views.ads import CategorySerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



