# Backend MySQL database

Docker image: https://hub.docker.com/_/mysql

```bash
docker run --rm -it --name mysql --network=my-bridge -e MYSQL_ROOT_PASSWORD=root-password mysql:9.1.0
```

and CLI:

```bash
$ docker run --rm -it --network=my-bridge -v db:/schema  mysql:9.1.0 mysql -hmysql -uroot -proot-password
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
