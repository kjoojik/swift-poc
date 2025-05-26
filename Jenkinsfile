pipeline {
    /* 1. Agent w kontenerze z Pythonem */
    agent {
        docker {
			image 'python:3.12-slim'
			args  '-u 0:0 -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    options { timestamps() }          // czytelniejsze logi
    stages {

        stage('Checkout') {
            steps {
				deleteDir()
				checkout scm 
				}
        }

        /* stage('Install deps') {
            when { fileExists 'requirements.txt' }
            steps { sh 'pip install -r requirements.txt' }
        }

        2. Kolejne skrypty – sekwencyjnie */
        stage('Run scripts') {
            steps {
                sh 'python skrypt_1.py'
                sh 'python skrypt_2.py'
                sh 'python skrypt_3.py'
                sh 'python skrypt_4.py'
                sh 'python skrypt_5.py'
            }
        }

        /*   Jeśli skrypty są niezależne, możesz zamiast powyższego
               użyć wykonania równoległego:

        stage('Run scripts in parallel') {
            parallel {
                script1 { sh 'python script1.py' }
                script2 { sh 'python script2.py' }
                ...
        } */

    }

    /* 3. Sekcja post do raportów i powiadomień */
    post {
        always {
            archiveArtifacts artifacts: '**/*.log', fingerprint: true
        }
        success {
            echo 'Wszystkie skrypty zakończone sukcesem'
        }
        failure {
           /*  mail to: 'dev-team@example.com',
                 subject: "${env.JOB_NAME} #${env.BUILD_NUMBER} FAILED",
                 body: "Sprawdź logi: ${env.BUILD_URL}" */
			echo 'Wyjebalo sie'
        }
    }
}
