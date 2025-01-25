pipeline {
    agent {
        node {
            label 'LinuxVM'
        }
    }
    tools {
        git 'git' // Ensure this matches the configured Git tool in Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/lokx1/jenkins.git']]])
            }
        }
        stage('Checking Input') {
            steps {
                script {
                    echo 'Checking input files for .c syntax and moving valid ones...'
                    def output = sh(script: """
                        python3 /home/baolong/Workspace/workspace/JenkinsAgentest/stageInput.py \
                        /home/baolong/Workspace/workspace/JenkinsAgentest/INPUT \
                        /home/baolong/Workspace/workspace/JenkinsAgentest/INPUT_CHECKED
                    """, returnStdout: true).trim()
                    echo "Output:\n${output}"
                }
            }
        }
        stage('Compile') {
            steps {
                script {
                    echo 'Compiling .c files...'
                    def output = sh(script: """
                        python3 /home/baolong/Workspace/workspace/JenkinsAgentest/stageCompile.py \
                        /home/baolong/Workspace/workspace/JenkinsAgentest/INPUT_CHECKED \
                        /home/baolong/Workspace/workspace/JenkinsAgentest/OBJECTFILE
                    """, returnStdout: true).trim()
                    echo "Output:\n${output}"
                }
            }
        }
        stage('Push Output') {
            steps {
                script {
                    echo 'Pushing output to a new branch...'
                    
                    // Generate a unique branch name using BUILD_NUMBER and timestamp
                    def branchName = "output-${env.BUILD_NUMBER}-${new Date().format('yyyyMMddHHmmss')}"

                    // Add and commit all output files
                    sh """
                        cd /home/baolong/Workspace/workspace/JenkinsAgentest
                        git checkout -b ${branchName}
                        git add .
                        git commit -m "Pipeline output for build #${env.BUILD_NUMBER}"
                    """

                    // Push the new branch to the public repository
                    sh """
                        git push https://github.com/lokx1/jenkins.git ${branchName}
                    """
                    
                    echo "Output pushed to branch '${branchName}'."
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    echo 'Resetting pipeline state...'
                    // Clean OBJECTFILE folder
                    sh """
                        rm -rf /home/baolong/Workspace/workspace/JenkinsAgentest/OBJECTFILE/*
                    """
                    echo 'OBJECTFILE folder is now empty.'

                    // Clean INPUT_CHECKED folder
                    sh """
                        rm -rf /home/baolong/Workspace/workspace/JenkinsAgentest/INPUT_CHECKED/*
                    """
                    echo 'INPUT_CHECKED folder is now empty.'

                    // Leave INPUT folder unchanged
                    echo 'INPUT folder remains unchanged.'
                }
            }
        }
    }
}
