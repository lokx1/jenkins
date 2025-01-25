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

        stage('Checking Input') {
            steps {
                script {
                    echo 'Checking input files for .c syntax and moving valid ones...'
                    def output = sh(script: """
                        python3 /home/baolong/Workspace/workspace/PROC/stageInput.py \
                        /home/baolong/Workspace/workspace/PROC/INPUT \
                        /home/baolong/Workspace/workspace/PROC/INPUT_CHECKED
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
                        python3 /home/baolong/Workspace/workspace/PROC/stageCompile.py \
                        /home/baolong/Workspace/workspace/PROC/INPUT_CHECKED \
                        /home/baolong/Workspace/workspace/PROC/OBJECTFILE
                    """, returnStdout: true).trim()
                    echo "Output:\n${output}"
                }
            }
        }

    }
}
