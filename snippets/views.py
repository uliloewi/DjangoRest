from snippets.models import Snippet #,JenkinsServer
from snippets.serializers import SnippetSerializer #, JenkinsServerSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import snippets.jenkinsservice
#from django.contrib.auth.models import User

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# 
# 
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user) 


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
# class JenkinsServerDetail(generics.RetrieveAPIView):
#     queryset = JenkinsServer.objects.all()    
#     serializer_class = JenkinsServerSerializer    
    

def call_jenkins(request):
    if request.method == 'GET':        
        return HttpResponse('''Hallo, my name is Jenkins. What can I do for you?''')

def jenkins_version(request):
    if request.method == 'GET':
        rsp = {}
        rsp['version']=snippets.jenkinsservice.get_jenkins_version()
        return JsonResponse(rsp, safe=False)

def jobs(request):
    if request.method == 'GET':
        rsp={}
        d=snippets.jenkinsservice.get_jobs()
        i=0
        for x in d:
            rsp["job "+str(i)]=x[0]
            i=i+1
        return JsonResponse(rsp)
    
@csrf_exempt    
def job(request,job_name):
    if request.method == 'GET':        
        job=snippets.jenkinsservice.get_job(job_name=job_name)
        rsp={}
        rsp["name"]=job.get_full_name()
        rsp["description"]=job.get_description()
        rsp["active"]=job.is_enabled()
        return JsonResponse(rsp)
    if request.method == 'PUT':  
        data = JSONParser().parse(request) 
        job=snippets.jenkinsservice.get_job(job_name=job_name)
        if (data['active']==True):
            job.enable()
        elif (data['active']==False):
            job.disable()
        rsp={}
        rsp["name"]=job.get_full_name()
        rsp["description"]=job.get_description()
        rsp["active"]=job.is_enabled()
        return JsonResponse(rsp)


    
