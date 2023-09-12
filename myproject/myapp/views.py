

# Create your views here.


# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskdataSerializer,TaskprioritySerializer,task_priority_data
from rest_framework import status
from rest_framework import permissions 

from django.views.decorators.csrf import csrf_exempt

# class SnippetList(APIView):
   
    
#     def get(self,request):
#         queryset =Task.objects.all()
#         serializer1 = TaskdataSerializer(queryset, many=True)
#         serializer2=TaskprioritySerializer(queryset,many=True)
#         print(serializer1,"this is serializer")
#         print(serializer2,"this is second serialier")
#         return Response(serializer1.data)
#         return Response(serializer1.data)

class MyModelViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset =Task.objects.all()
    serializer_class = task_priority_data

        
    # def get(self,request):
    #     queryset =Task.objects.all()
    #     serializer1 = TaskdataSerializer(queryset, many=True)
       
        
    #     return Response(serializer1.data)
      
    
      
    # def get(self,request):
    #     queryset =Task.objects.all()
       
    #     serializer2=TaskprioritySerializer(queryset,many=True)
      
    #     return Response(serializer2.data)
       
   
    @action(detail=False, methods=['post'],url_path='post-data')
    def post_data_task(self, request, format=None):
        serializer = TaskdataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

   
    @action(detail=False, methods=['post'] ,url_name='post-priority')
    def post_priority_task(self, request, format=None):
        serializer = TaskprioritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

