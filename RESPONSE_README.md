# curation-dev-challenge

### 1. Coding standards used

Using Black as python formatting tool

### 2. Running program in a Docker container

1. Folder structure

   ```
   challenge-madhu-reddy/
   ├── LICENSE
   ├── README.md
   ├── RESPONSE_README.md
   ├── app
   │   ├── app.py
   │   ├── config.py
   │   ├── docker-entrypoint.sh
   │   ├── dockerfile
   │   ├── models.py
   │   ├── requirements.txt
   │   ├── static
   │   │   ├── css
   │   │   │   └── style.css
   │   │   └── js
   │   │       └── search.js
   │   └── templates
   │       └── search.html
   └── docker-compose.yml

   ```

2. Build and run the docker containers
   From root folder (challenge-madhu-reddy/), where docker-compose file exists

   ```
   $ docker-compose build (to build the images for flask app and MySQL db)

   $ docker-compose ps (to see the running containers)

   $ docker-compose up (to run the flask app and MySQL db, keep this terminal open)

   Madhus-MacBook-Pro:challenge-madhu-reddy bmr$ docker-compose build
   db uses an image, skipping
   Building app
   Step 1/9 : FROM python:3.8
   ---> e7d3be492e61
   Step 2/9 : EXPOSE 5000
   ---> Using cache
   ---> fe08f38fc152
   Step 3/9 : WORKDIR /app
   ---> Using cache
   ---> 3a41202816f7
   Step 4/9 : COPY requirements.txt /app
   ---> Using cache
   ---> 6cbb09b3aac6
   Step 5/9 : RUN pip3 install -r requirements.txt
   ---> Using cache
   ---> 0edc85b280de
   Step 6/9 : COPY . /app
   ---> 53ffa0c84c1b
   Step 7/9 : COPY docker-entrypoint.sh /app
   ---> c9ca461258e6
   Step 8/9 : RUN chmod u+x /app/docker-entrypoint.sh
   ---> Running in af3daf63e440
   Removing intermediate container af3daf63e440
   ---> 245769125981
   Step 9/9 : ENTRYPOINT ["/app/docker-entrypoint.sh"]
   ---> Running in af2c5d1b5f67
   Removing intermediate container af2c5d1b5f67
   ---> 13a4d7739b38
   Successfully built 13a4d7739b38
   Successfully tagged challenge-madhu-reddy_app:latest
   ```

   ```
   Madhus-MacBook-Pro:challenge-madhu-reddy bmr$ docker-compose ps
   Name                       Command                       State     Ports
   ------------------------------------------------------------------------
   challenge-madhu-reddy_app_1   /app/docker-entrypoint.sh     Exit 137
   mysql_t3                  docker-entrypoint.sh mysqld   Exit 0
   ```

   ```
   Madhus-MacBook-Pro:challenge-madhu-reddy bmr$ docker-compose up
   Starting mysql_t3 ... done
   Recreating challenge-madhu-reddy_app_1 ... done
   Attaching to mysql_t3, challenge-madhu-reddy_app_1
   mysql_t3 | 2021-06-22 19:14:21+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.25-1debian10 started.
   mysql_t3 | 2021-06-22 19:14:21+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
   mysql_t3 | 2021-06-22 19:14:21+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.25-1debian10 started.
   mysql_t3 | 2021-06-22T19:14:21.638357Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.25) starting as process 1
   mysql_t3 | 2021-06-22T19:14:21.649801Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
   mysql_t3 | 2021-06-22T19:14:21.830360Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
   mysql_t3 | 2021-06-22T19:14:21.921522Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
   mysql_t3 | 2021-06-22T19:14:21.966794Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
   mysql_t3 | 2021-06-22T19:14:21.966989Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
   mysql_t3 | 2021-06-22T19:14:21.969189Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
   mysql_t3 | 2021-06-22T19:14:21.990599Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.25' socket: '/var/run/mysqld/mysqld.sock' port: 3306 MySQL Community Server - GPL.
   app_1 | Creating directory /app/migrations ... done
   app_1 | Creating directory /app/migrations/versions ... done
   app_1 | Generating /app/migrations/README ... done
   app_1 | Generating /app/migrations/script.py.mako ... done
   app_1 | Generating /app/migrations/env.py ... done
   app_1 | Generating /app/migrations/alembic.ini ... done
   app_1 | Please edit configuration/connection/logging settings in '/app/migrations/alembic.ini' before proceeding.
   app_1 | INFO [alembic.runtime.migration] Context impl MySQLImpl.
   app_1 | INFO [alembic.runtime.migration] Will assume non-transactional DDL.
   app_1 | INFO [alembic.autogenerate.compare] Detected added table 'repos'
   app_1 | Generating /app/migrations/versions/42c5618c3b8d*.py ... done
   app_1 | INFO [alembic.runtime.migration] Context impl MySQLImpl.
   app_1 | INFO [alembic.runtime.migration] Will assume non-transactional DDL.
   app_1 | INFO [alembic.runtime.migration] Running upgrade -> 42c5618c3b8d, empty message
   app_1 | _ Environment: production
   app_1 | WARNING: This is a development server. Do not use it in a production deployment.
   app_1 | Use a production WSGI server instead.
   app_1 | _ Debug mode: off
   app_1 | _ Running on all addresses.
   app_1 | WARNING: This is a development server. Do not use it in a production deployment.
   app_1 | _ Running on http://172.22.0.3:5000/ (Press CTRL+C to quit)
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:16:57] "GET /repos HTTP/1.1" 200 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:16:57] "GET /static/css/style.css HTTP/1.1" 304 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:16:57] "GET /static/js/search.js HTTP/1.1" 304 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:16:58] "GET /static/js/search.js HTTP/1.1" 304 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:17:00] "GET /repos HTTP/1.1" 200 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:17:00] "GET /static/css/style.css HTTP/1.1" 304 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:17:00] "GET /static/js/search.js HTTP/1.1" 304 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:17:04] "GET /repos?language=C HTTP/1.1" 200 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:17:04] "GET /static/css/style.css HTTP/1.1" 304 -
   app_1 | 172.22.0.1 - - [22/Jun/2021 19:17:04] "GET /static/js/search.js HTTP/1.1" 304 -
   ```

3. Go to /app folder on Docker container (on separate terminal)

   a. To see the running containers, example below

   ```
   $ docker ps

   Madhus-MacBook-Pro:challenge-madhu-reddy bmr$ docker-compose ps
   Name                       Command                       State     Ports
   ------------------------------------------------------------------------
   challenge-madhu-reddy_app_1   /app/docker-entrypoint.sh     Exit 137
   mysql_t3                  docker-entrypoint.sh mysqld   Exit 0

   ```

   b. Run the container's interactive bash, it will open the bash shell like below, and cd into /app folder to see the content, challenge-madhu-reddy_app_1 is the container name

   ```
   $ docker exec -it challenge-madhu-reddy_app_1 bash

   root@6edfc0c0cbac:/app# pwd
   /app

   root@6edfc0c0cbac:/app# ls ( to see the /app files along with migrations)

   __pycache__  app.py  config.py  docker-entrypoint.sh  dockerfile  migrations  models.py  requirements.txt  static  templates

   ```

4. Navigate to flask app url (http://localhost:5000/repos), should see landing page

5. Connecting to MySQL database running on Docker container (on separate terminal)

   a. To see the running containers, example below

   ```
   $ docker ps

   Madhus-MacBook-Pro:challenge-madhu-reddy bmr$ docker-compose ps
   Name                       Command                       State     Ports
   ------------------------------------------------------------------------
   challenge-madhu-reddy_app_1   /app/docker-entrypoint.sh     Exit 137
   mysql_t3                  docker-entrypoint.sh mysqld   Exit 0

   ```

   b. Run the container's interactive bash, it will open the bash shell like below, and log into mysql as a root user, mysql_t3 is the container name

   ```
   $ docker exec -it mysql_t3 bash

   root@2c041a9b0530:/# mysql -u root -p (see the docker-compose file for the password)

   mysql> show databases;
   +--------------------+
   | information_schema |
   | mysql |
   | performance_schema |
   | sys |
   | repos_db |
   +--------------------+

   mysql> use repos_db;

   mysql> show tables;
   +----------------------+
   | Tables_in_repos_db |
   +----------------------+
   | alembic_version |
   | repos |
   +----------------------+

   mysql> select * from repos; (data appears as the user performs repo search on the web page)
   ```

### 3. Basic workflow of program

#### App workflow

1. User selects the choice of language (example Python) from the home page and clicks submit.

2. Flask app runs on the matched route (/repos)

3. Creates a database if that does not exist.

4. App verifies if the database has the data for the Python public repos.

5. If the data does not exist in db, it will call the GitHub api and store the data (repo_name, stars count, repo_url) in the database. If data exists, it will jump to step 6 to get the data for the requested language direclty from the db instead of calling the github api.

6. Retrieves the data from the table and renders on the html template.

7. The GitHub api returns 30 reords by default, so the same is stored in database and will be displayed on web page. We can customize to get upto maximum of 100 records.

8. Webpage displays the data in the table format (Repo_name, Stars, Repo_URL) and all the columns can be sorted, by default it is sorted desc order on Stars.

9. Webpage filters the data from the table when user enters the keyword.

#### OPTIONAL --- Environment setup locally (assuming MySQL client is installed on the user machine, db credentials has been created),

1. Create a virtual env
   From root folder (challenge-madhu-reddy)
   python3 -m venv .venv

2. Activate venv
   From root folder (challenge-madhu-reddy)
   source .venv/bin/activate

3. Install dependencies
   From app folder (challenge-madhu-reddy/app)
   pip install -r requirements.txt

4. Change the host name from db to localhost (config.py)

5. Run the app
   From app folder (challenge-madhu-reddy/app)
   FLASK_ENV=development flask run

   app runs at http://127.0.0.1:5000/repos

6. On separate terminal run the migrations from app folder (challenge-madhu-reddy/app)

   ```
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

7. Connect to the database on the user machine

   ```
   mysql> mysql -u root -p
   Enter password after the prompt
   mysql> show databases;
   mysql> use repos_db;
   mysql> show tables;
   mysql> select \* from repos;
   ```

8. Folder structure

   ```
   challenge-madhu-reddy/
   ├── RESPONSE_README.md
   ├── app
   │   ├── __pycache__
   │   │   ├── __init__.cpython-38.pyc
   │   │   ├── app.cpython-38.pyc
   │   │   ├── config.cpython-38.pyc
   │   │   └── models.cpython-38.pyc
   │   ├── app.py
   │   ├── config.py
   │   ├── docker-entrypoint.sh
   │   ├── dockerfile
   │   ├── migrations
   │   │   ├── README
   │   │   ├── __pycache__
   │   │   │   └── env.cpython-38.pyc
   │   │   ├── alembic.ini
   │   │   ├── env.py
   │   │   ├── script.py.mako
   │   │   └── versions
   │   │       ├── 3bd7db880fca_.py
   │   │       ├── 7cc27cd56624_.py
   │   │       └── __pycache__
   │   │           ├── 3bd7db880fca_.cpython-38.pyc
   │   │           └── 7cc27cd56624_.cpython-38.pyc
   │   ├── models.py
   │   ├── requirements.txt
   │   ├── static
   │   │   ├── css
   │   │   │   └── style.css
   │   │   └── js
   │   │       └── search.js
   │   └── templates
   │       └── search.html
   └── docker-compose.yml
   ```
