from rest_framework import serializers

from modules.models import Module, Lesson


class ModuleSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели образовательных модулей'''

    class Meta:
        model = Module
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели уроков'''

    class Meta:
        model = Lesson
        fields = '__all__'
