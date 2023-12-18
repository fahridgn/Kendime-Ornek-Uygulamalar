from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Users


# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()


def sample_get(request):
    query = Users.objects.all().values()
    return render(request, "sample.html", {"query": query})


def example(request):
    return render(request, "index.html")
