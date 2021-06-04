# curation-dev-challenge

### 1. Coding standards used

Using Black as python formatting tool

### 2. Running program in a Docker container

### 3. Basic workflow of program

#### Environment setup --- This may change after dockerfile is created

1. Create a virtual env
   From root folder (challenge-madhu-reddy)
   python3 -m venv .venv

2. Activate venv
   From root folder (challenge-madhu-reddy)
   source .venv/bin/activate

3. Install dependencies
   From app folder (challenge-madhu-reddy/app)
   pip install -r requirements.txt

4. Run the app
   From app folder (challenge-madhu-reddy/app)
   FLASK_ENV=development flask run

   app runs at http://127.0.0.1:5000/repos

5. At this point, MySQL is not ready (will be ready after dockerfile is created), but should be able to run the app and see the web page.

#### App workflow

1. User selects the choice of language (ex Python) from the home page and clicks submit.
2. Flask app runs on the matched route /repos
3. Creates a database if that does not exist.
4. App verifies if the database has the data for the Python public repos.
5. If the data does not exist in db, it will call the GitHub api and store the data (repo_name, stars count, repo_url) in the database. If data exists, it will jump to step 6 to get the data for the requested language direclty from the db instead of calling the github api.
6. Retrieves the data from the table and renders on the html template.
7. The GitHub api returns 30 reords by default, so the same is stored in database and will be displayed on web page. We can customize to get upto maximum of 100 records.
8. Webpage displays the data in the table format (Repo_name, Stars, Repo_URL) and all the columns can be sorted, by default it is sorted desc order on Stars.
9. Webpage filters the data from the table when user enters the keyword.
