from django.test import TestCase
from django.http import HttpRequest
from  snippets import jenkinsservice, views

class JenkinsServiceTests(TestCase):
    
    def test_jenkins_version_is_not_one(self):
        version=jenkinsservice.get_jenkins_version()
        self.assertTrue(version=='2.46.3')
        
    def test_jenkins_jobs_lists(self):
        jobs=jenkinsservice.get_jobs()
        i=0
        for x in jobs:
            i=i+1
        self.assertTrue(i>0)