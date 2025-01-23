# Backend MySQL database

Base image: https://hub.docker.com/_/mysql
Dockerfile copies init scripts into `/docker-entrypoint-initdb.d/`
which will init the DB on the first start.

Building:

```bash
docker build -t mysql-msgs:9.1.0 .
```

Running the DB

```bash
docker run --rm --name mysql --network=my-bridge -e MYSQL_ROOT_PASSWORD=root-password -p 3306:3306 mysql-msg:9.1.0
```

and CLI:

```bash
$ docker run --rm -it --network=my-bridge -v db:/schema mysql:9.1.0 mysql -hmysql -uroot -proot-password
mysql> source /schema/db.sql
mysql> source /schema/test-data.sql
```

then:

```sql
SHOW databases;
USE msgs;
SELECT * FROM posts;
```

## Schema

- `db.sql` - main schema
- `test_data.sql` - the test data to push into DB
