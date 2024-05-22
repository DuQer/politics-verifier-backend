pipeline {
    agent any
    
    stages {
        stage('DFX start') {
            steps {
                script {
                    sh(script: 'dfx start --background')
                }
            }
        }
        stage('DFX deploy') {
            steps {
                script {
                    sh(script: 'dfx deploy')
                }
            }
        }
        

        stage('Building Docker Image') {
            steps {
                script {
                    sh(script: 'docker build -t back-image:latest .', label: 'Building image')
                }
            }
        }
        
        stage('Pushing Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "docker login -u $DOCKER_USER -p $DOCKER_PASSWORD"
                    sh 'docker tag back-image:latest genzoo/back-image:latest'
                    sh 'docker push genzoo/back-image:latest'
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
