from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from modules.models import Module, Lesson
from modules.serializers import ModuleSerializer, LessonSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [AllowAny]


class ModuleListAPIView(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [AllowAny]


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [AllowAny]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [AllowAny]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [AllowAny]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('module',)
    ordering_fields = ('name',)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
