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

        stage('Deploy Services') {
            steps {
                script {
                    // Deploy using docker-compose.yml
                    sh 'docker run -d -p 9000:9000 myapp-image:v0.1'
                }
            }
        }
    }
}
