pipeline {
    agent any
    stages {
        stage('Move Files') {
            steps {
                script {
                    def bufferSubPath = "/path/to/buffer"
                    def bufferParentPath = "/path/to/bufferParent"
                    sh """
                        mv /home/agent1/Workspace/workspace/Jenkins/INPUT_CHECKED/* ${bufferSubPath}/
                        mv /home/agent1/Workspace/workspace/Jenkins/OBJECTFILE/* ${bufferSubPath}/
                        mv /home/agent1/Workspace/workspace/Jenkins/INPUT/InputLogs.txt ${bufferSubPath}/
                        mkdir -p ${bufferSubPath}/TESTCASE
                    """
                    echo "Files moved to buffer: ${bufferSubPath}"
                    echo "INPUT_CHECKED, OBJECTFILE directories are now empty."
                }
            }
        }
        stage('Git Operations') {
            steps {
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
                                # Make an initial commit
                                git commit --allow-empty -m "Initial commit"
                                git push --set-upstream origin main
                            else
                                echo "Switching to main branch..."
                                git checkout main
                            fi

                            # Stage all changes
                            git add .
                            git commit -m "Automated commit"
                            git push origin main
                        '''
                    }
                }
            }
        }
    }
}