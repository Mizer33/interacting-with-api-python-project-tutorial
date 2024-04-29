# Importar las bibliotecas necesarias
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar las credenciales para utilizar la API de Spotify
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET")))

def buscar_id_artista(nombre_artista):
    results = spotify.search(q='artist:' + nombre_artista, type='artist', limit=1)
    artist = results['artists']['items'][0]
    return artist['id'], artist['name']

def obtener_top_tracks_con_duracion(artista_id):
    top_tracks = spotify.artist_top_tracks(artista_id, country='US')
    return [(track['name'], track['popularity'], track['duration_ms']) for track in top_tracks['tracks']]

# Función para obtener el ID del artista y el top 10 de canciones
artista_id, artista_nombre = buscar_id_artista("canserbero")  # Cambia "Queen" por el nombre del artista que desees
top_canciones = obtener_top_tracks_con_duracion(artista_id)
print(artista_id)
# Crear un DataFrame con los datos obtenidos
df_top_tracks = pd.DataFrame(top_canciones, columns=['Nombre Canción', 'Popularidad', 'Duración (ms)'])

# Convertir la duración de milisegundos a minutos para mejor comprensión
df_top_tracks['Duración (min)'] = df_top_tracks['Duración (ms)'] / 60000
print(df_top_tracks)
# Graficar un scatter plot para analizar la relación entre duración y popularidad
plt.figure(figsize=(10, 6))
plt.scatter(df_top_tracks['Duración (min)'], df_top_tracks['Popularidad'], color='blue')
plt.title(f'Relación entre Duración y Popularidad de las Canciones de {artista_nombre}')
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.grid(True)

print("Mostrando gráfico...")
plt.show()
print("Gráfico mostrado.")

