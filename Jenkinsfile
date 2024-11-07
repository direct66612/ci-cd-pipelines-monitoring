pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/direct66612/ci-cd-pipelines-monitoring'
        IMAGE_NAME = 'ci-cd-test-image'
        CONTAINER_NAME = 'ci-cd-test-container'
        PORT = '8080'
    }

    stages {
        stage('clone Repository') {
            steps {
                git url: "${REPO_URL}", branch: 'main'
            }
        }

        stage('build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('run Container') {
            steps {
                script {
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:${PORT} ${IMAGE_NAME}"
                }
            }
        }

        stage('test http request') {
            steps {
                script {
                    sh "curl -s http://localhost:${PORT}"
                }
            }
        }

        stage('stop container and delete image') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}"

                    sh "docker rmi ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

