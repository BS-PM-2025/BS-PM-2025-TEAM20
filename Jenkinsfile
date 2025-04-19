pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python setup.py install'  // אם מדובר בפרויקט Python
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/'  // הרצת מבחנים
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh './deploy.sh'  // סקריפט פריסה, אם יש לך כזה
            }
        }
    }
}
