source ../.secrets.sh
psql --user=$DB_USERNAME --host=$DB_HOST --password $DB_NAME
