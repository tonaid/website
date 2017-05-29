from flask import Flask, render_template

__all__ = ("app")

app = Flask(__name__)


@app.route('/')
@app.route('index.html')
def index():
    return render_template(
        'index.html'
    )


def run_debug():
    site_host = "0.0.0.0"
    site_port = 3000
    site_debug = True
    app.run(
        host=site_host, port=site_port,
        debug=site_debug, use_debugger=site_debug)


if "__main__" == __name__:
    run_debug()
