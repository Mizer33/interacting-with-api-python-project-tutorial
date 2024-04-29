import pandas as pd

# Convertir la lista de top tracks en un DataFrame
df_top_tracks = pd.DataFrame(top_canciones, columns=['Nombre Canción', 'Popularidad', 'Álbum'])
print(df_top_tracks)


