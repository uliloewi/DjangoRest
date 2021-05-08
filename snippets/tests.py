import json
from django.test import TestCase
from django.http import HttpRequest
from  snippets import jenkinsservice, views
from rest_framework import request
from jenkinsapi.custom_exceptions import NotFound, UnknownJob

class JenkinsServiceTests(TestCase):
    
    def test_jenkins_version_is_not_one(self):
        version=jenkinsservice.get_jenkins_version()
        self.assertTrue(version=='2.46.3')
        
    def test_jenkins_jobs_lists(self):
        i=0
        try:
            jobs=jenkinsservice.get_jobs()
        except:
            i=-1            
        for x in jobs:
            i=i+1
        self.assertTrue(i>=0)
    
    def test_jenkins_find_a_job(self):
        try:
            job=jenkinsservice.get_job('TestJob')
            self.assertTrue(job.get_full_name()=='TestJob')
        except NotFound:
            self.assertTrue(True)
        
class RestViewTests(TestCase):
    def test_greeting(self):
        request=HttpRequest()
        request.method='GET'
        response=views.call_jenkins(request)
        self.assertTrue(response.content==b'''Hallo, my name is Jenkins. What can I do for you?''')
    
    def test_jenkins_version_is_2_46_3(self):
        request=HttpRequest()
        request.method='GET'
        response=views.jenkins_version(request)
        dict=json.loads(response.content)
        self.assertTrue(dict['version']=="2.46.3")
    
    def test_has_jobs(self):
        request=HttpRequest()
        request.method='GET'
        response=views.jobs(request)
        dict=json.loads(response.content)
        if len(dict)>0:
            self.assertTrue(response.content.index(b'job 0')==2)
        else:
            self.assertTrue()
            
    def test_find_job(self):
        request=HttpRequest()
        request.method='GET'
        try:
            response=views.job(request,job_name='TestJob')
            dict=json.loads(response.content)
            self.assertTrue(dict['name']=='TestJob')
        except UnknownJob:
            self.assertTrue(True)
        
    def test_enable_or_disable_job(self):
        request=HttpRequest()
        request.method='PUT'
        request.content_type='application/json'
        #request.body=b'{"active":true}' 
        request.POST["active"]=True        
        try:
            response=views.job(request,job_name='TestJob')
            dict=json.loads(response.content)
            self.assertTrue(dict['active']==True)
        except UnknownJob:
            self.assertTrue(True)    