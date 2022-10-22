from django.shortcuts import render
from rest_framework.views import APIView
from .models import Dog, Breed
from .serializers import DogDetailsSerializer, BreedDetailsSerializer
from rest_framework.response import Response


class DogDetail(APIView):

    def get(self, request):
        details = Dog.objects.all()
        serialized_data = DogDetailsSerializer(details, many=True)
        return Response(serialized_data.data)

    def post(self, request):
        serialized_data = DogDetailsSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)

    def put(self, request, id):
        details = Dog.objects.filter(id=id)[0]
        if not details:
            return Response({"Error": "Id doesn't exist"})
        serialized_data = DogDetailsSerializer(data=request.data, instance=details)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            print(serialized_data.data)
            return Response(serialized_data.data)

    def delete(self, request, id):
        id = Dog.objects.filter(id=id)
        if not id:
            return Response({"Error": "Id doesn't exist!"})
        serialized_data = DogDetailsSerializer(data=request.data, instance=id[0])
        id_name = id[0].id
        id[0].delete()
        return Response({"Message": f"Id {id_name} has been deleted"})


class BreedDetail(APIView):

    def get(self, request):
        details = Breed.objects.all()
        serialized_data = BreedDetailsSerializer(details, many=True)
        return Response(serialized_data.data)

    def post(self, request):
        serialized_data = BreedDetailsSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)

    def put(self, request, id):
        id = Breed.objects.filter(id=id)
        if not id:
            return Response({"Error": "Id doesn't exist"})
        serialized_data = BreedDetailsSerializer(data=request.data, instance=id[0])
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            print(serialized_data.data)
            return Response(serialized_data.data)

    def delete(self, request, id):
        id = Breed.objects.filter(id=id)
        if not id:
            return Response({"Error": "Id doesn't exist!"})
        serialized_data = BreedDetailsSerializer(data=request.data, instance=id[0])
        id_name = id[0].id
        id[0].delete()
        return Response({"Message": f"Id {id_name} has been deleted"})
