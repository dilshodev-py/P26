BACKUP_DIR="/home/dilshod/PycharmProjects/P26/module_4/lesson_5/backups/"
FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S`.tar
PGPASSWORD='1' pg_dump -U postgres -h localhost -d lesson_5 -F tar -f $FILE_NAME

