echo "DEPLOYING TO EC2 INSTANCE"
source "../.secrets.sh"
echo "Sending environmental variables to ec2 instance"
# cat "../.secrets.sh" | ssh -i $SERVER_KEY $SERVER_USER@$SERVER_LOCATION
ssh -i $SERVER_KEY $SERVER_USER@$SERVER_LOCATION << EOF
  echo "Saving secret environment variables..."
  export SECRET_KEY="$SECRET_KEY"
  export DEBUG_MODE="False"
  export ADMIN_USER="$ADMIN_USER"
  export ADMIN_PASS="$ADMIN_PASS"
  export DB_HOST="$DB_HOST"
  export DB_NAME="$DB_NAME"
  export DB_PORT="$DB_PORT"
  export DB_USERNAME="$DB_USERNAME"
  export DB_PASSWORD="$DB_PASSWORD"
  export EMAIL_PORT="$EMAIL_PORT"
  export EMAIL_ADDR="$EMAIL_ADDR"
  export EMAIL_ADMIN="$EMAIL_ADMIN"
  export EMAIL_PASS="$EMAIL_PASS"
  export EMAIL_HOST="$EMAIL_HOST"
  export EMAIL_IMAP="$EMAIL_IMAP"
  export SERVER_LOCATION="$SERVER_LOCATION"
  export SERVER_USER="$SERVER_USER"
  export SERVER_KEY="$SERVER_KEY"
  export SERVER_REPO="$SERVER_REPO"
  export CLIENT_REPO="$CLIENT_REPO"
  export TWITTER_CONSUMER_KEY="$TWITTER_CONSUMER_KEY"
  export TWITTER_CONSUMER_SECRET="$TWITTER_CONSUMER_SECRET"
  export TWITTER_ACCESS_TOKEN="$TWITTER_ACCESS_TOKEN"
  export TWITTER_ACCESS_TOKEN_SECRET="$TWITTER_ACCESS_TOKEN_SECRET"

  echo $DEBUG_MODE
  echo "Killing old server..."
  pkill python3
  echo "Deleting old code..."
  rm -rf api/
  echo "Cloning down new code..."
  git clone $SERVER_REPO api
  echo "Updating code..."
  cd api/
  git pull origin master
  echo "Downloading everything..."
  sudo pip3 install -r requirements.txt
  echo "Launching new server..."
  cd qwergram_api/
  python3 /usr/local/lib/python3.4/dist-packages/gunicorn/app/wsgiapp.py -w 4 qwergram_api.wsgi:application -D
  python3 -c "import requests; print(requests.get('http://127.0.0.1:8000/api/v1/articles').json())"
  cd ../qwergram_bots/
  echo "Booting up Hydrogen and Lithium Bot..."
  python3 -m smtp.get_articles &>/dev/null &!
EOF

echo "API & BOTS DEPLOYED!"
