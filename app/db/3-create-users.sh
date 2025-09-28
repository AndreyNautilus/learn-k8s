#!/bin/bash
set -e

createuserssql=$(dirname "$0")/create-users.sql.template

sed "s|\${BACKEND_PASSWORD}|${MYSQL_BACKEND_PASSWORD}|g" ${createuserssql} | mysql -u root -p"$MYSQL_ROOT_PASSWORD"
