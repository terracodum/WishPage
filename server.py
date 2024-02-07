from bottle import run, template, route, static_file

@route("/")
def index():
    return template("./index.html")

@route("/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./")

run(reloader=True)