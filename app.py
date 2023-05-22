from flask import Flask, send_file, request, jsonify
from flask import render_template, url_for
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            routes.append(f'<a href="{rule}">{rule}</a>')
    return '<br>'.join(routes)

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        return send_file('static/resume.pdf', as_attachment=True)
    else:
        return send_file('static/resume.pdf', as_attachment=True)
    

@app.route('/personal-info')
def personal_info():
    with open('static/personal-info.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/skills')
def skills():
    with open('static/skills.json') as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/contact')
def contact():
    with open('static/contact.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/education')
def education():
    with open('static/education.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/experience')
def experience():
    with open('static/experience.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/profiles')
def profiles():
    with open('static/profiles.json') as f:
        data = json.load(f)
    return jsonify(data)


# serve the static.courses.json file
@app.route('/courses')
def courses():
    with open('static/courses.json') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)