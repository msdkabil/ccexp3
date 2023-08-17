from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])

def get_weather():
    city = request.args.get('city')
    if city is None:
        abort(400, 'Missing argument city')
    data = {}
    data['q'] = request.args.get('city')
    data['appid'] = 'XXXXXXXXX'
    data['units'] = 'metric'
    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)
    resp = Response(data)
    resp.status_code = 200
    return render_template('index.html', title='Weather App', data=json.loads(data.read().decode('utf8')))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
