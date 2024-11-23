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
                    sh 'docker build -t myapp-image .'
                }
            }
        }

        stage('Deploy Services') {
            steps {
                script {
                    // Deploy using docker-compose.yml
                    sh 'docker run -d myapp-image 9000:9000'
                }
            }
        }
    }

    post {
        always {
            // Optional cleanup after the pipeline finishes
            sh 'docker compose down'
        }
    }
}
