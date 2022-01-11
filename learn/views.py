from django.http import HttpResponse
from rest_framework.decorators import api_view
from learn.models import CreateTask
from learn.serializers import CreateTaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class addtask(APIView):

    def get(self, request):
        task = CreateTask.objects.all()
        serializer = CreateTaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#
# class CreateTaskViewSet(viewsets.ModelViewSet):
#     queryset = CreateTask.objects.all()
#     serializer_class = CreateTaskSerializer
