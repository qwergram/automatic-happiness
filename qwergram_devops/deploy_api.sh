echo "DEPLOYING TO EC2 INSTANCE"
source "../.secrets.sh"
echo "Sending environmental variables to ec2 instance"
cat "../.secrets.sh" | ssh -i $SERVER_KEY $SERVER_USER@$SERVER_LOCATION
ssh -i $SERVER_KEY $SERVER_USER@$SERVER_LOCATION << EOF
  echo "Saving secret environment variables..."
  export SECRET_KEY="$SECRET_KEY"
  export DEBUG_MODE="$DEBUG_MODE"
  export DB_HOST="$DB_HOST"
  export DB_NAME="$DB_NAME"
  export DB_PORT="$DB_PORT"
  export DB_IDENTITY="$DB_IDENTITY"
  export DB_USERNAME="$DB_USERNAME"
  export DB_PASSWORD="$DB_PASSWORD"
  export EMAIL_PORT="$EMAIL_PORT"
  export EMAIL_ADDR="$EMAIL_ADDR"
  export EMAIL_PASS="$EMAIL_PASS"
  export EMAIL_HOST="$EMAIL_HOST"
  export SERVER_LOCATION="$SERVER_LOCATION"
  export SERVER_USER="$SERVER_USER"
  export SERVER_KEY="$SERVER_KEY"
  export CLIENT_REPO="$CLIENT_REPO"
  echo "Killing old server..."
  pkill gunicorn
  echo "Deleting old code..."
  rm -rf api/
  echo "Cloning down new code..."
  git clone https://github.com/qwergram/automatic-happiness.git api
  echo "Updating code..."
  cd api/
  git pull origin master
  echo "Launching new server..."
  cd qwergram_api/
  gunicorn -w 4 qwergram_api.wsgi:application -D
EOF

echo "EC2 INSTANCE DEPLOYED!"
