import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto, "html.parser")

preguntas = soup.select(".s-post-summary")

# print(preguntas[0])

for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print(f"{usuario} - Titulo: {titulo}")
