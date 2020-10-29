from atlassian import Bitbucket
import jenkins

bitbucket = Bitbucket(
    url='http://localhost:7990',
    username='amitmazor',
    password='Am53235323')


server = jenkins.Jenkins('http://localhost:8081', username='amitmazor', password='Am53235323')

EMPTY_CONFIG_XML = '''<?xml version='1.0' encoding='UTF-8'?>
<project>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class='jenkins.scm.NullSCM'/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers class='vector'/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>'''


server.create_job('tryagain', jenkins.EMPTY_CONFIG_XML)
print(server.get_job_config('empty'))

info = server.get_job_info('amitjenkinsrepoo')
print(info['lastCompletedBuild'])
