from flask import Flask, render_template, abort
import json
import os


def create_app():
    app = Flask(__name__)

    app_path = os.path.dirname(__file__)
    with open(app_path+'/projects.json','r') as file:
        projects = json.load(file)

    slug_to_project = {project["slug"]:project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)


    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project.keys():
            abort(404)
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app

#app = create_app()
#app.run(debug=True, port = 8569)

