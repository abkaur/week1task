pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'abkaur95/simple-web-app' // Docker Hub image name
        GIT_REPO = 'https://github.com/abkaur/python-web-application.git' // GitHub repository URL
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Clone Repository') {
            steps {
                withCredentials([string(credentialsId: 'github-access-token', variable: 'GITHUB_TOKEN')]) {
                    sh 'git clone https://${GITHUB_TOKEN}@github.com/abkaur/python-web-application.git'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                dir('python-web-application') {
                    sh 'docker build -t ${DOCKER_IMAGE}:latest .'
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                  usernameVariable: 'DOCKER_USERNAME', 
                                                  passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                }
                sh 'docker push ${DOCKER_IMAGE}:latest'
            }
        }
    }

    post {
        always {
            sh 'docker rmi ${DOCKER_IMAGE}:latest || true'
        }
    }
}
