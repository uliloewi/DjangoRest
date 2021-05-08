from jenkinsapi.jenkins import Jenkins

jenkins_url = 'http://127.0.0.1:8080'
server = Jenkins(jenkins_url, username='admin', password='admin')

def get_jenkins_version():
    return server.version

def get_jobs():
    return server.get_jobs();

def get_job(job_name):
    return server.get_job(job_name);

def disable_job(job_name):
    return server.get_job(job_name).disable();