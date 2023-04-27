from flask import render_template

import config
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(debug=True)