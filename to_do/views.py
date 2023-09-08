from django.shortcuts import render, get_object_or_404
from .models import ToDo
from .serializer import ToDoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CreateToDo(APIView):
    def post(self, request):
        user_body = request.data
        serializer = ToDoSerializer(data=user_body)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)     
        return Response(serializer.errors)    

class UpdateToDo(APIView):
    def patch(self, request, *args, **kwargs):
        tasks = get_object_or_404(ToDo, id = kwargs['task_id'])
        serializer = ToDoSerializer(tasks, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

class DeleteToDo(APIView):
    def delete(self, request, *args, **kwargs):
        tasks = get_object_or_404(ToDo, id = kwargs['task_id'])
        tasks.delete()
        return Response({'task':"successfully deleted"})   

class All(APIView):
    def get(self, request):
        all_data = ToDo.objects.all()
        result = ToDoSerializer(all_data, many=True)
        return Response(result.data)

# class AllByDate(APIView):
#     def get(self, request)

# class Get(APIView):    