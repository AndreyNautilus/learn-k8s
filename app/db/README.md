# Backend MySQL database

Temporary Database image. Works for the playground.

Base image: https://hub.docker.com/_/mysql
Dockerfile copies init scripts into `/docker-entrypoint-initdb.d/`
which will init the DB on the first start.

Building:

```bash
docker build -t mysql-msgs:9.1.0 .
```

Running the DB

```bash
docker run --rm --name mysql --network=my-bridge -e MYSQL_ROOT_PASSWORD=root-password -e MYSQL_BACKEND_PASSWORD=backend_password -p 3306:3306 mysql-msgs:9.1.0
```

and CLI (as root):

```bash
$ docker run --rm -it --network=my-bridge -v db:/schema mysql:9.1.0 mysql -hmysql -uroot -proot-password
mysql> source /schema/1-db.sql
mysql> source /schema/2-test-data.sql
```

and CLI (as user):

```bash
docker run --rm -it --network=my-bridge -v db:/schema mysql:9.1.0 mysql -hmysql -ubackend -pbackend_password
```

then:

```sql
SHOW databases;
USE msgs;
SELECT * FROM posts;
```

## Schema

- `1-db.sql` - main schema
- `2-test_data.sql` - the test data to push into DB
