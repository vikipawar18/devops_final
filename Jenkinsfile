pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vikipawar18/devops_final.git']]])
            }
        }
        stage('Build') {
         steps {
               git branch: 'main', url: 'https://github.com/vikipawar18/devops_final.git'
               sh 'python3 app.py'
            }
        }
        stage('Test') {
            steps {
                echo 'TESTING'
            }
        }
        stage('Deploy'){
            steps {
                echo 'Deploying'
            }
        }
    }
}