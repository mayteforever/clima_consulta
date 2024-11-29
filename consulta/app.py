from flask import Flask, render_template, request
import requests

# Inicializar la aplicación Flask
app = Flask(__name__)

# Función para obtener datos del clima desde la API
def get_weather_data(city: str):
    API_KEY = '97a070903d595d8d61e4bff468c84817'  # Clave válida
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Ruta principal
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            data = get_weather_data(city)
            if data and data.get('cod') == 200:
                latitude = data['coord']['lat']
                longitude = data['coord']['lon']
                return render_template('index.html', data=data, latitude=latitude, longitude=longitude)
            return render_template('index.html', error="Ciudad no encontrada")
    return render_template('index.html')

# Ruta para el currículo
@app.route("/cv")
def cv():
    return render_template('cv.html')

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
