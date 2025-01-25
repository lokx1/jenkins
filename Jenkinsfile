pipeline {
    agent {
        node {
            label 'JenkinsTEST' // Agent có nhãn 'JenkinsTEST'
        }
    }
    triggers {
        pollSCM('* * * * *') // Kiểm tra source code mỗi phút
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
