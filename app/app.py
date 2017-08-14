from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False

def get_nav(cur_page):
    nav_hrefs = {
                  'exper': '/exper',
                  'about': '/about',
                  'exper_vt': '/exper/vt',
                  'exper_hu': '/exper/hu',
                  'exper_rs': '/exper/rs',
                }
    nav_hrefs[cur_page] = '#'
    return nav_hrefs

@app.route('/')
def index():
    return redirect('/exper')

@app.route('/exper')
def exper():
    return render_template('index.html',
                           nav_hrefs = get_nav('exper'),
                           exper_sub = None
                          )

@app.route('/exper/vt')
def exper_vt():
    return render_template('vt.html',
                           nav_hrefs = get_nav('exper_vt'),
                           exper_sub = 'vt'
                          )

@app.route('/exper/hu')
def exper_hu():
    return render_template('hu.html',
                           nav_hrefs = get_nav('exper_hu'),
                           exper_sub = 'hu'
                          )

@app.route('/exper/rs')
def exper_rs():
    return render_template('rs.html',
                           nav_hrefs = get_nav('exper_rs'),
                           exper_sub = 'rs'
                          )

@app.route('/about')
def about():
    return render_template('about.html',
                           nav_hrefs = get_nav('about'),
                           exper_sub = None
                          )


if __name__ == '__main__':
    app.run()
