from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category, Genre
from .serializers import WomenSerializer, GenreSerializer, GenreListSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    # http://127.0.0.1:8000/api/v1/womens/genre/genres/
    # def get_serializer_class(self):
    #     if self.action in ['list']:
    #         print(self.action)
    #         return GenreListSerializer
    #     return GenreSerializer

    # @action(methods=['get'], detail=False)
    # def genres(self, request):
    #     gen = Genre.objects.all()
    #     cat = Category.objects.all()
    #     return Response({'gen': [g.name for g in gen], 'cat': [c.name for c in cat]})

    # @action(methods=['get'], detail=True)
    # def genres(self, request, pk=None):
    #     gen = Genre.objects.get(pk=pk)
    #     cat = Category.objects.get(pk=pk)
    #     return Response({'gen': gen.name, 'cat': cat.name})


# class WomenAPIListPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
#
#
# class WomenAPIListForOneUser(generics.ListCreateAPIView):
#     serializer_class = WomenSerializer
#     pagination_class = WomenAPIListPagination
#
#     def get_queryset(self):
#         return Women.objects.filter(user=self.request.user)
#
#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     pagination_class = WomenAPIListPagination
#
#
# class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #
    #     if not pk:
    #         return Women.objects.all()[:3]
    #     return Women.objects.filter(pk=pk)
    #
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})
