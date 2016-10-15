from flask import Flask, render_template, request
import giphypop
import os
app = Flask(__name__)
g = giphypop.Giphy()

def header_results(terms):
    return 'GIFs tagged with: "{}"'.format(terms)

# This is our index page:
@app.route('/')
def index():
    greeting = "Welcome!"
    return render_template('index.html', greeting=greeting)

# This is our about page:
@app.route('/about')
def about():
    return render_template('about.html')

# This is our results page:
@app.route('/results')
def results():
    terms = request.values.get('terms')
    header = header_results(terms)
    results = g.search(terms)
    return render_template('results.html', header=header, results=results, terms=terms)


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)