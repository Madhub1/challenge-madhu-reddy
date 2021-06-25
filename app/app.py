from flask import Flask, request, render_template
import requests
import json


app = Flask(__name__)

# this import needs to be here to avoid circular import error
from models import (
    verify_if_data_exists_in_db,
    insert_data_into_db,
    get_data_from_db,
    create_database,
)

## create the database for the first time
create_database()

# A route for a home page
# http://127.0.0.1:5000/repos?language=Python
@app.route("/repos", methods=["GET"])
def search():
    results = []
    language = ""
    language_choice = request.args.get("language")
    if language_choice != None:
        language = f'"{language_choice}"'

        ## verify if the data exists in db for the requested language
        count = verify_if_data_exists_in_db(language_choice)
        print("count...", count)
        # if the data does not exist, make a call to the GitHub api and store the that data in db
        if count == 0:
            ## make a call to function to get data from the GitHiub api
            results = get_data_from_github_api(language_choice)

            ## wtite the data to the db
            insert_data_into_db(results)

        ## retrieve the data from the db
        repos = get_data_from_db(language_choice)

        results = [(repo.repo_name, repo.stars, repo.repo_url) for repo in repos]

    ## return the data to the template to render
    return render_template(
        "search.html",
        title="Search most starred Repos",
        repos=results,
        language=language,
    )


def get_data_from_github_api(language_choice):
    print("get_data_from_github_api is invoked")
    results = []
    url = f"https://api.github.com/search/repositories?q=language:{language_choice}&sort=stars"

    ## make a call to the GitHub API
    repos = requests.get(url)
    repos = repos.json()

    ## retrieve the repo_name, stargrazers_count, github_repo_url from the results
    for key, value in repos.items():
        if key == "items":
            for item in value:
                results.append(
                    (
                        item["full_name"],
                        item["stargazers_count"],
                        item["html_url"],
                        language_choice,
                    )
                )
    ## return results from API
    return results


if __name__ == "__main__":
    app.run()
