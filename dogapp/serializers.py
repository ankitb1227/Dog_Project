from rest_framework.serializers import ModelSerializer
from .models import Dog, Breed


class DogDetailsSerializer(ModelSerializer):

    class Meta:
        model = Dog
        fields = '__all__'


class BreedDetailsSerializer(ModelSerializer):

    class Meta:
        model = Breed
        fields = '__all__'
