#!/usr/bin/python3
"""

    Author: Bernardo Mota
    Contact email: bernardo.mota at tecnico.ulisboa.pt

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

DB_FILE_PATH = "db.sql"


from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from wsgiref.handlers import CGIHandler


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return redirect(url_for("index"))

    if "phone" not in request.form:
        flash("Ocorreu um erro")
        return redirect(url_for("index"))


    conn = sqlite3.connect(DB_FILE_PATH)
    c = conn.cursor()
    c.execute("SELECT phone FROM fb WHERE phone = ?", (int(request.form["phone"]), ))
    is_in_leak = bool(c.fetchone())


    if not is_in_leak:
        return render_template("notFound.html")

    return render_template("found.html", phone=request.form["phone"])



# # For development purposes we do not use CGI
# if __name__ == '__main__':
#     app.run(debug=True)

CGIHandler().run(app)