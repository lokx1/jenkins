pipeline {
    agent {
        node {
            label 'JenkinsTEST' // Agent có nhãn 'JenkinsTEST'
        }
    }

    stages {
        stage('Setup Workspace') {
            steps {
                echo "Setting up workspace..."
                sh '''
                cd /home/baolong/Jenkins Testing/workspace/JenkinsAgentest
                echo "hello" > file.txt
                '''
            }
        }
    }
}
