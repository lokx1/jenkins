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
                        python3 /home/agent1/Workspace/workspace/Jenkins/stageInput.py \
                        /home/agent1/Workspace/workspace/Jenkins/INPUT \
                        /home/agent1/Workspace/workspace/Jenkins/INPUT_CHECKED
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
                        python3 /home/agent1/Workspace/workspace/Jenkins/stageCompile.py \
                        /home/agent1/Workspace/workspace/Jenkins/INPUT_CHECKED \
                        /home/agent1/Workspace/workspace/Jenkins/OBJECTFILE
                    """, returnStdout: true).trim()
                    echo "Output:\n${output}"
                   
                }
            }
        }

        stage('AI Generating Testcase') {
            steps {
                script {
                    echo 'Generating test cases using AI...'
                    def output = sh(script: """
                        python3 /home/agent1/Workspace/workspace/Jenkins/AiGen.py \
                        /home/agent1/Workspace/workspace/Jenkins/INPUT_CHECKED \
                        /home/agent1/Workspace/workspace/Jenkins/TESTCASE
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
                    def bufferParentPath = "/home/agent1/Workspace/workspace/Jenkins/BUFFER"
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
                        mv /home/agent1/Workspace/workspace/Jenkins/INPUT_CHECKED/* ${bufferSubPath}/
                        mv /home/agent1/Workspace/workspace/Jenkins/OBJECTFILE/* ${bufferSubPath}/
                        mv /home/agent1/Workspace/workspace/Jenkins/INPUT/InputLogs.txt ${bufferSubPath}/
                        mkdir -p ${bufferSubPath}/TESTCASE
                       
                    """
                    // mv /home/agent1/Workspace/workspace/Jenkins/TESTCASE/*.c ${bufferSubPath}/TESTCASE/
                    
                    echo "Files moved to buffer: ${bufferSubPath}"
                    echo "INPUT_CHECKED, OBJECTFILE directories are now empty."

                    // Use withCredentials for Git operations
                    withCredentials([sshUserPrivateKey(credentialsId: 'git', keyFileVariable: 'SSH_KEY')]) {
                        dir(bufferParentPath) {
                            sh '''
                                export GIT_SSH_COMMAND="ssh -i $SSH_KEY"
                                
                                # Check if the remote 'origin' exists
                                if ! git remote | grep -q 'origin'; then
                                    git remote add origin git@github.com:lokx1/jenkins-logs.git
                                else
                                    git remote set-url origin git@github.com:lokx1/jenkins-logs.git
                                fi

                                # Ensure we are on a valid branch
                                if ! git rev-parse --verify main >/dev/null 2>&1; then
                                    echo "Main branch does not exist. Creating it..."
                                    git checkout -b main
                                    git push --set-upstream origin main
                                else
                                    echo "Switching to main branch..."
                                    git checkout main
                                fi

                                # Stage all changes
                                git add .

                                # Commit changes if there are any
                                git commit -m "Automated commit from Jenkins pipeline: $(date +%Y%m%d%H%M%S)" || echo "No changes to commit"

                                # Pull the latest changes from the remote repository with rebase
                                git pull --rebase origin main || echo "Pull failed, please check for conflicts"

                                # Push changes to the remote repository
                                git push origin main || echo "Push failed, please check credentials"
                            '''
                        }
                    }

                    // Delete the files in INPUT_CHECKED and OBJECTFILE directories
                    sh """
                        rm -rf /home/agent1/Workspace/workspace/Jenkins/INPUT_CHECKED/*
                        rm -rf /home/agent1/Workspace/workspace/Jenkins/OBJECTFILE/*
                    """

                    echo "Cleanup complete, INPUT_CHECKED and OBJECTFILE directories cleared."
                }
            }
        }
    }
}