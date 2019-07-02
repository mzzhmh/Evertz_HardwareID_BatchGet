node
{
        stage('Build') {
	    checkout scm
        }
	stage('list source') {
	    sh "ls -lrt"
        }
        stage('Deploy') {
            sh "rsync -av ./* /opt/getEvertzHardwareID/"
        }
	stage('Run filter code'){
	    sh "cd /opt/getEvertzHardwareID/"
            sh "grep -e '<Name.*[0-9][0-9][0-9][0-9].*</Name><Type dt:dt=\"ui4\">1</Type>' -e 'Evertz' /opt/serialNumber/2x-gorehill.dat > Evertz.txt"
	}
	stage('Run batch get'){
	    sh "/opt//getEvertzHardwareID/HardwareIDreader.py &>/opt/getEvertzHardwareID/EvertzSoftwareBuild.csv"
            sh "cp /opt/getEvertzHardwareID/EvertzSoftwareBuild.csv /opt/serialNumber/"
	}
}
