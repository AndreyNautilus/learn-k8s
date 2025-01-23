FROM mysql:9.1.0

# these scripts will run if the storage is empty
# (first initialization of a DB).
COPY db.sql test-data.sql /docker-entrypoint-initdb.d/
