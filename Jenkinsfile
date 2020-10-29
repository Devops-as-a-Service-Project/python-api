pipeline {

    environment {
        CI = 'true'
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

          stage ('Invoke pipeline CD') {
            steps {
                build job: 'python-cd', parameters: [
                string(name: 'python-cd', value: "value1")
                ]
            }
        }
     
    }
}