pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository (Jenkins automatically checks out code from SCM)
                checkout scm
            }
        }
            
        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker image using the Dockerfile in the root
                    sh 'docker build --no-cache -t myapp-image:v0.1 .'
                }
            }
        }

        stage('Deploy Docker Services') {
            steps {
                script {
                    // Deploy using docker-compose.yml
                    sh 'docker run -d  --name myapp-image -p 9000:9000 myapp-image:v0.1'
                }
            }
        }

        stage('Stop Deployed Docker Services') {
            steps {
                script {
                    // Deploy using docker-compose.yml
                    sh 'docker stop myapp-image'
                }
            }
        }        

        stage('Remove Deployed Docker Services') {
            steps {
                script {
                    // Deploy using docker-compose.yml
                    sh 'docker rm myapp-image'
                }
            }
        }

        stage('Remove Deployed Docker Image') {
            steps {
                script {
                    // Deploy using docker-compose.yml
                    sh 'docker rmi myapp-image:v0.1'
                }
            }
        }       
        
    }
}
