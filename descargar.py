# from pytube import YouTube

# # URL del video de YouTube
# video_url = 'https://www.youtube.com/watch?v=uz0sOL5spW4'

# # Crear objeto YouTube
# yt = YouTube(video_url)

# # Mostrar los streams disponibles
# for stream in yt.streams:
#     print(stream)

# # Descargar un stream específico
# video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

# # Descargar el video
# print(f'Descargando {yt.title} en {video_stream.resolution}...')
# video_stream.download(output_path='.', filename='jetpens_video.mp4')
# print('Descarga completada.')


# import yt_dlp

# video_url = 'https://www.youtube.com/watch?v=uz0sOL5spW4'

# # Configurar opciones
# ydl_opts = {
#     'format': 'best',
#     'outtmpl': 'jetpens_video.mp4'
# }

# # Descargar el video
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([video_url])

# print('Descarga completada.')

import yt_dlp

# URL del video de YouTube
video_url = input("Ingrese la URL del video de YouTube: ")

# Configurar opciones para descargar en 1080p o 720p si 1080p no está disponible
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=720]',  # 1080p si está disponible, o 720p
    'outtmpl': '%(title)s.%(ext)s',  # Guardar archivo con el nombre del título del video
    'merge_output_format': 'mp4',    # Formato final del archivo
}

# Descargar el video con la configuración especificada
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print('Descarga completada.')
