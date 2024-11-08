pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/direct66612/ci-cd-pipelines-monitoring'
        IMAGE_NAME = 'ci-cd-test-image'
        CONTAINER_NAME = 'ci-cd-test-container'
        PORT = '80'
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

    post {
        always {
            cleanWs()
        }
    }
}

