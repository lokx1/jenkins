pipeline {
    agent {
        node {
            label 'LinuxVM'
        }
    }
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
        stage('Checking Input') {
            steps {
                script {
                    echo 'Checking input files for .c extension...'
                    def output = sh(script: "python3 /home/baolong/Workspace/workspace/JenkinsAgentest/check_input.py /home/baolong/Workspace/workspace/JenkinsAgentest/INPUT", returnStdout: true).trim()
                    echo "Output:\n${output}"
                }
            }
        }
    }
}
