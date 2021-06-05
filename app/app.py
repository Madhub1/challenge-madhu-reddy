from flask import Flask, request, render_template
import requests
from models import Repo

## creates a Flask application, named app
app = Flask(__name__)

## create a instance of repo model
repo = Repo()

## create a database on app run, if does not exist
repo.create_database()

# a route where we will display a home page via an HTML template
# http://127.0.0.1:5000/repos?language=Python
@app.route("/repos", methods=["GET"])
def search():
    repos = []
    language = ""
    language_choice = request.args.get("language")
    if language_choice != None:
        language = f'"{language_choice}"'
        # verify if the data exists in db for the requested language
        count = repo.verify_if_data_exists_in_db(language_choice)

        # if the data does not exist, make a call to the GitHub api and store the that data in db
        if count == 0:
            #     ## make a call to function to get data from the GitHiub api
            results = get_data_from_github_api(language_choice)

            # # wtite the data to the db
            repo.insert_data_into_db(results)

        # retrieve the data from the db
        repos = repo.get_data_from_db(language_choice)

    ## return the data to the template to render
    return render_template(
        "search.html",
        title="Search most starred Repos",
        repos=repos,
        language=language,
    )


def get_data_from_github_api(language_choice):
    print("get_data_from_github_api is invoked")
    results = []
    url = f"https://api.github.com/search/repositories?q={language_choice}&sort=stars"

    ## make a call to the GitHub API
    repos = requests.get(url)
    repos = repos.json()

    ## retrieve the repo_name, stargrazers_count, github_repo_url from the results
    for key, value in repos.items():
        if key == "items":
            for item in value:
                results.append(
                    {
                        "repo_name": item["full_name"],
                        "stars": item["stargazers_count"],
                        "repo_url": item["html_url"],
                        "language": language_choice,
                    }
                )

    ## return results from API
    return results


## run the app
if __name__ == "__main__":
    app.run(debug=True)
