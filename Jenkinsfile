pipeline {
    agent {
        node {
            label 'LinuxVM'
        }
    }
    tools {
        git 'Default' // Đảm bảo tên Git tool khớp với cấu hình trong Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out repository..."
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/lokx1/jenkins.git'
                    ]]
                ])
            }
        }
        stages('test') {
            steps {
                echo "Testing..."
                echo "hello" >> test.txt
                sh 'mvn test'
            }
        }
    }
}
