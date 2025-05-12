pipeline {
    agent any

    environment {
        IMAGE_NAME = "smarttasks-app"
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/lalit-shinkar/smarttasks.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/' // You can skip this if not using tests yet
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Run Docker Container') {
            steps {
                sh "docker run -d -p 5000:5000 $IMAGE_NAME"
            }
        }
    }
}
