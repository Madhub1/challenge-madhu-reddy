# curation-dev-challenge

### 1. Coding standards used

Using Black as python formatting tool

### 2. Running program in a Docker container

1. Folder structure

   ```
   .
   └── challenge-madhu-reddy
    ├── LICENSE
    ├── README.md
    ├── RESPONSE_README.md
    ├── app
    │   ├── __pycache__
    │   │   ├── app.cpython-38.pyc
    │   │   └── models.cpython-38.pyc
    │   ├── app.py
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
   From root folder (challenge-madhu-reddy), where docker-compose file exists

   ```
   $ docker-compose build (to build the images for flask app and MySQL db)

   $ docker-compose ps (to see the running containers)

   $ docker-compose up (to run the flask app and MySQL db, keep this terminal open)


   Madhus:challenge-madhu-reddy$ docker-compose build
   db uses an image, skipping
   Building app
   Step 1/7 : FROM python:3.8
   ---> e7d3be492e61
   Step 2/7 : EXPOSE 5000
   ---> Using cache
   ---> fe08f38fc152
   Step 3/7 : WORKDIR /app
   ---> Using cache
   ---> 3a41202816f7
   Step 4/7 : COPY requirements.txt /app
   ---> Using cache
   ---> db2b013d3d91
   Step 5/7 : RUN pip3 install -r requirements.txt
   ---> Using cache
   ---> 01567ce9e742
   Step 6/7 : COPY . /app
   ---> df756b9d39b7
   Step 7/7 : CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
   ---> Running in 3a48844e8124
   Removing intermediate container 3a48844e8124
   ---> 57b5aecf0289
   Successfully built 57b5aecf0289
   Successfully tagged challenge-madhu-reddy_app:latest


   Madhus:challenge-madhu-reddy$ docker-compose up
   Recreating challenge-madhu-reddy_app_1 ... done
   Attaching to mysql_8a, challenge-madhu-reddy_app_1
   mysql_8a | 2021-06-05 17:33:26+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.25-1debian10 started.
   mysql_8a | 2021-06-05 17:33:26+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
   mysql_8a | 2021-06-05 17:33:26+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.25-1debian10 started.
   mysql_8a | 2021-06-05T17:33:27.262711Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.25) starting as process 1
   mysql_8a | 2021-06-05T17:33:27.273506Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
   mysql_8a | 2021-06-05T17:33:27.469446Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
   mysql_8a | 2021-06-05T17:33:27.564792Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
   app_1  |  * Environment: production
   app_1  |    WARNING: This is a development server. Do not use it in a production deployment.
   app_1  |    Use a production WSGI server instead.
   app_1  |  * Debug mode: off
   mysql_8a | 2021-06-05T17:33:27.625425Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
   mysql_8a | 2021-06-05T17:33:27.625620Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
   mysql_8a | 2021-06-05T17:33:27.629078Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
   mysql_8a | 2021-06-05T17:33:27.649267Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.25'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
   app_1  |  * Running on all addresses.
   app_1  |    WARNING: This is a development server. Do not use it in a production deployment.
   app_1  |  * Running on http://172.21.0.3:5000/ (Press CTRL+C to quit)

   ```

3. Navigate to flask app url (http://localhost:5000/repos), should see landing page

4. Connecting to MySQL database running on Docker container (on separate terminal)

   a. To see the running containers, example below

   ```
   $ docker ps

   Madhus-MBP:challenge-madhu-reddy bmr$ docker-compose ps
   Name                          Command                       State            Ports
   ----------------------------------------------------------------------------------
   challenge-madhu-reddy_app_1   python3 -m flask run --hos ...   Up      0.0.0.0:5000->5000/tcp
   mysql_8a                      docker-entrypoint.sh mysqld      Up      0.0.0.0:3305->3306/tcp, 33060/tcp
   ```

   b. Run the container's interactive bash, it will open the bash shell like below, and log into mysql as a root user, mysql_8c is the container name

   ```
   $ docker exec -it mysql_8c bash

   root@2c041a9b0530:/# mysql -u root -p (see the docker-compose file for the password)

   mysql> show databases;

   mysql> use repos_db;

   mysql> show tables;


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

4. Change the host name from db to localhost (models.py)

5. Run the app
   From app folder (challenge-madhu-reddy/app)
   FLASK_ENV=development flask run

   app runs at http://127.0.0.1:5000/repos

6. Connect to the database on the user machine
   mysql> mysql -u root -p
   Enter password after the prompt
   mysql> show databases;
   mysql> use repos_db;
   mysql> show tables;
   mysql> select \* from repos;
