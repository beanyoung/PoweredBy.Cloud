from flask import (
    Flask,
    g,
    render_template,
    request,
)


app = Flask(__name__)


sites = [
    dict(id=1, name='foo'),
    dict(id=2, name='bar'),
    dict(id=3, name='baz'),
    dict(id=4, name='qux'),
]


@app.route('/')
def index():
    g.user = 'Tommy'
    return render_template('index.html', sites=sites)


@app.route('/api/sites', methods=['POST'])
def create_site():
    site_name = request.get_json()['name']
    site = dict(id=len(sites) + 1, name=site_name)
    sites.append(site)
    return site


if __name__ == '__main__':
    app.run()
