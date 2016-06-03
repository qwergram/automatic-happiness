echo "Download and Install Jenkins"
source "../.secrets.sh"
ssh -i $SERVER_KEY $SERVER_USER@$SERVER_LOCATION << EOF
  wget http://pkg.jenkins-ci.org/debian-stable/binary/jenkins_1.651.2_all.deb
  sudo dpkg -i jenkins_1.651.2_all.deb
  sudo apt-get -y -f --force-yes install
  rm jenkins_1.651.2_all.deb
EOF
