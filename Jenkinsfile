pipeline {

    environment {
        CI = 'true'
        // Docker registry information
        registry = "amitmazor/daas-restapi"
        registryCredential = "dockerhub"
        // create an environment to save docker image informations
        dockerImage = ''
   }

    agent any
   
    stages {
    
        stage('build') {
            agent { docker { image 'python:3.7.2' } }
             steps {
                 sh 'pip install -r requirements.txt'
              }
         }
    
        //stage('test') {
            //steps {
              //sh 'python test.py'
            //}   
        //}
     
        // Building the docker image. It will run the docker build and use the jenkins build number in docker tag.
        // With build number turn easeful to deploy or rollback based in jenkins.
        stage('Building the docker image') {
            steps {
                 script {
                     dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
  
        // Push the docker image builded to dockerhub.
        stage('Deploy Image') {
            steps {
                 script {
                     docker.withRegistry( '', registryCredential ) {
                     dockerImage.push()
                            }
                 }
           }
        }
                
        // After build and deploy, delete the image to cleanup your server space.
        stage('Remove Unused docker image') {
            steps{
                 sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
}
}