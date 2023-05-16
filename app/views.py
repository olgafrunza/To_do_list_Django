from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def home(request):
    return HttpResponse("<h2>Todo API</h2>")

@api_view(["GET","POST"])
def todo_view(request):

    if request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # this part covert GET method
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many = True)
    return Response(serializer.data)

class TodoView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        param = self.request.query_params.get("completed")
        if param == "true":
            return Todo.objects.filter(done=True)
        return super().get_queryset()
    
    def get_serializer(self, *args, **kwargs):
        print("place your additional coding here!!!!")
        return super().get_serializer(*args, **kwargs)
    
    
    def perform_create(self, serializer):
        print("If you want to todo sthg just before save update here!")
        serializer.save(priority="L", task=serializer.validated_data.get("task").upper())





@api_view(["GET", "PUT","PATCH","DELETE"])
def todo_detail(request, id):
    if request.method == "GET":
        # data = Todo.objects.get(id=id)
        data = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(data)
        return Response(serializer.data)
    elif request.method == "PUT":
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
        return Response({"message" : "Delete successfull"})

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"

class TodoCRUD(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer