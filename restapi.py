from atlassian import Bitbucket
import requests
from flask import Flask, jsonify, request
from python-jenkins import jenkins

bitbucket = Bitbucket(
    url='http://localhost:7990',
    username='amitmazor',
    password='Am53235323')

server = jenkins.Jenkins('http://localhost:8081', username='amitmazor', password='Am53235323')
app = Flask(__name__)

# Get request - get project info if exists 
@app.route('/project/<string:project_name>')
def get_project_data(project_name):
    for project in bitbucket.project_list():
        if project['name'] == project_name:
            return jsonify(project)
    return jsonify ({'message' :'project not found'})
   

# Get request - get repo info is exists
@app.route('/project/<string:project_name>/<string:repo_name>')
def get_repo_data(project_name, repo_name):
    for project in bitbucket.project_list():
        if project['name'] == project_name:
            project_key = project['key']
            for repo in bitbucket.repo_list(project_key):
                if repo['name'] == repo_name:
                    return jsonify(bitbucket.get_repo(project_key, repo_name))
            return jsonify ({'message' :'repo not found'})       
    return jsonify ({'message' :'project not found'})

# Post request - creates npm project and repository, and run the jenkins pipeline 
@app.route('/create/npm/<string:project_name>/<string:project_key>/<string:repo_name>')
def create_project_and_repo(project_name, project_key, repo_name):
    for project in bitbucket.project_list():
        if project['name'] == project_name:
            project_key = project['key']
            bitbucket.create_repo(project_key, repo_name, forkable=False, is_private=True)
            # After creating the new repo, lets start the pipeline
            #server.create_job(repo_name, jenkins.EMPTY_CONFIG_XML)
               
            return jsonify(repo_name)
    bitbucket.create_project(project_key, project_name)
    bitbucket.create_repo(project_key, repo_name, forkable=False, is_private=True)
    return jsonify(repo_name)




app.run(port=5000)
 

# #GET repository - #http://localhost:7990/rest/api/1.0/repos/?<name=test> 
# #GET project - http://localhost:7990/rest/api/1.0/projects
