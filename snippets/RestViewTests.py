from django.test import TestCase
from django.http import HttpRequest
from  snippets import jenkinsservice, views

class RestViewTests(TestCase):
    
    def test_jenkins_version_is_2_46_3(self):
        request=HttpRequest()
        request.method='GET'
        version=views.jenkins_version(request)
        self.assertTrue(version.content==b'{"version": "2.46.3"}')
    
    def test_jenkins_has_jobs(self):
        request=HttpRequest()
        request.method='GET'
        jobs=views.jobs(request)
        self.assertTrue(jobs.content.index(b'job 0')==2)