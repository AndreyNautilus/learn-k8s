FROM mysql:9.1.0

# these scripts will run if the storage is empty
# (first initialization of a DB).
COPY \
    1-db.sql \
    2-test-data.sql \
    3-create-users.sh create-users.sql.template \
    /docker-entrypoint-initdb.d/
