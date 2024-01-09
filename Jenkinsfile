#!groovy
pipeline {
    agent any

    stages {
//        stage('Ws-Cleanup') {
//            steps {
//                cleanWs()
//            }
//       }
//       stage('Checkout') {
//            steps {
//                // Забрать код из системы контроля версий (например, Git)
//                git 'https://github.com/gavitt/jenkins.git'
//            }
//        }
        stage('Unit Test') {
            steps {
                // Запуск unit тестов используя, например, junit для Java или pytest для Python
                sh '''
                    cd python-simple-app
                    /var/lib/jenkins/.local/bin/pytest -v --junitxml=report.xml
                    '''
            }
            post {
                always {
                    // Сбор результатов тестов для Jenkins
                    junit 'python-simple-app/report.xml'
                }
            }
        }
        post('Upload to Jira') {
            always {
                step([
                        $class                    : 'TestResultSenderBuildStep',
                        jiraURL                   : 'https://jira.iskrauraltel.ru/',
                        jiraUserName              : 'gluhov',
                        jiraPassword              : hudson.util.Secret.fromString(SECRET),
                        testResultsDirectory      : 'python-simple-app/*.xml',
                        testResultsType           : 'JUNIT',
                        missingTestPlanKeyStrategy: 'FAIL_TASK'
                ])    
            }
        }
    }
}
