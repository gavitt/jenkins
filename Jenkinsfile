#!groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Забрать код из системы контроля версий (например, Git)
                git 'https://github.com/gavitt/jenkins.git'
            }
        }
        stage('Unit Test') {
            steps {
                // Запуск unit тестов используя, например, junit для Java или pytest для Python
                sh '''
                    cd python-simple-app
                    pytest -v --junitxml=report.xml
                    '''
            }
            post {
                always {
                    // Сбор результатов тестов для Jenkins
                    junit 'report.xml'
                }
            }
        }
        stage('Upload to TestFLO') {
            steps {
                script {
                    // Здесь должна быть реализована логика отправки отчета в TestFLO
                    // Например, используйте HTTP запрос для отправки результатов тестирования
                    echo 'Здесь должен быть скрипт загруки результатов тестирования в TestFLO'
                }
            }
        }
    }
}
