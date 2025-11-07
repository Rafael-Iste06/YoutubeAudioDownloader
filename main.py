import yt_dlp

def download_audio(url, output_path='.', format_choice='m4a'):
    try:
        format_option = 'bestaudio[ext=m4a]'  # Télécharger le meilleur audio en MP3 ou M4A
        postprocessors = []  # Pas de conversion, on garde le fichier MP3 ou M4A

        # Paramètres de téléchargement pour yt-dlp
        ydl_opts = {
            'format': format_option,  # Télécharger selon le format choisi
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Définit le chemin de téléchargement
            'postprocessors': postprocessors,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Télécharger la vidéo ou audio
            print(f"Téléchargement de l'audio : {url}")
            ydl.download([url])
            print(f"Audio téléchargé avec succès dans le dossier : {output_path}")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo YouTube dont vous voulez télécharger l'audio : ")
    download_path = input("Entrez le chemin du dossier de téléchargement (laisser vide pour le dossier videos) : ")

    download_audio(video_url, download_path if download_path else './videos')