pipeline {
    agent any
    tools {
        git 'git' // Use the correct Git tool name
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your Git repository
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/lokx1/jenkins.git']]])
            }
        }
        stage('Test') {
            steps {
                echo 'Testing Jenkins pipeline with Git'
                echo "Testing Jenkins pipeline with Git" > test.txt
            }
        }
    }
}
