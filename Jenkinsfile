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
        stage('Cleanup and Buffer') {
    steps {
        script {
            echo 'Moving files to buffer with subdirectories and cleaning up...'

            // Create the parent BUFFER directory if it doesn't exist
            def bufferParentPath = "/home/baolong/Workspace/workspace/PROC/BUFFER"
            sh """
                mkdir -p ${bufferParentPath}
            """

            // Create a timestamped subdirectory for this pipeline run
            def timestamp = new Date().format("yyyyMMddHHmmss")
            def bufferSubPath = "${bufferParentPath}/RUN_${timestamp}"
            sh """
                mkdir -p ${bufferSubPath}
            """

            // Move files to the subdirectory
            sh """
                mv /home/baolong/Workspace/workspace/PROC/INPUT_CHECKED/* ${bufferSubPath}/
                mv /home/baolong/Workspace/workspace/PROC/OBJECTFILE/* ${bufferSubPath}/
            """
            
            echo "Files moved to buffer: ${bufferSubPath}"
            echo "INPUT_CHECKED and OBJECTFILE directories are now empty."

            // Use withCredentials for Git operations
            withCredentials([sshUserPrivateKey(credentialsId: 'git', keyFileVariable: 'SSH_KEY')]) {
            sh """
                git remote set-url origin git@github.com:lokx1/jenkins-logs
                git add .
                git commit -m "Automated commit from Jenkins pipeline"
                GIT_SSH_COMMAND="ssh -i $SSH_KEY" git push
            """
            }


            // Delete the files in the timestamped subdirectory after ensuring they are backed up
            sh """
                rm -rf ${bufferSubPath}/*
            """

            echo "Cleanup complete, buffer subdirectory cleared: ${bufferSubPath}"
        }
    }
}

     

    }
}
