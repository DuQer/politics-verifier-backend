pipeline {
    agent any
    
    stages {
        stage('DFX Start') {
            steps {
                script {
                    sh(script: 'dfx start --background')
                }
            }
        }
        stage('DFX Deploy') {
            steps {
                script {
                    sh(script: 'dfx deploy')
                }
            }
        }
        

        stage('Building Docker Image') {
            steps {
                script {
                    sh(script: 'docker build -t politics-verifier-backend:latest .', label: 'Building image')
                }
            }
        }
        
        stage('Pushing Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "docker login -u $DOCKER_USER -p $DOCKER_PASSWORD"
                    sh 'docker tag back-image:latest duqer/politics-verifier-backend:latest'
                    sh 'docker push duqer/politics-verifier-backend:latest'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker logout'
            }
        }
    }
}
