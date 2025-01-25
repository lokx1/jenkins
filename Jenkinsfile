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
        stage('Test') {
            steps {
                echo 'Testing Jenkins pipeline with Git'
                script{
                        def Output = bat(script:"/home/baolong/Workspace/workspace/JenkinsAgentest/helloworld.py",returnStdout:true).trim()
                        echo "Output is: ${Output}"

                }
            }
        }
    }
}
