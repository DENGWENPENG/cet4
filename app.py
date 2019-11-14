from flask import Flask, escape, render_template, url_for

app = Flask(__name__)


@app.route('/word/<word>', methods=['GET'])
def word(word):
    import requests
    from bs4 import BeautifulSoup
    data = requests.get(
        'https://cn.bing.com/dict/SerpHoverTrans?q='+escape(word))
    soup = BeautifulSoup(data.text, 'html.parser')
    word = soup.find_all('li')
    try:
        yin = soup.find('span', class_='ht_attr').text
    except:
        yin = '*****'
    import json
    return json.dumps({'yin': yin, 'mean': [i.text for i in word]})


@app.route('/')
def index():
    return render_template('index.html', jsurl=url_for('static', filename='index.js'), cssurl=url_for('static', filename='index.css'), vuejs=url_for('static', filename='vue.js'))


if __name__ == '__main__':
    import webbrowser
    webbrowser.open('http:127.0.0.1:5000')
    app.run(port=5000)
