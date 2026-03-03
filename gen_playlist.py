import os
import json

# --- CONFIGURATION ---
GITHUB_USER = "TomVCQL"  # Remplace par ton pseudo GitHub
REPO_NAME = "spotyshare-music"      # Remplace par le nom de ton dépôt
BRANCH = "main"             # Généralement 'main' ou 'master'

def generate_json():
    playlist = []
    # On liste tous les fichiers du dossier
    files = [f for f in os.listdir('.') if f.endswith('.mp3')]
    files.sort() # Pour avoir un ordre alphabétique

    for filename in files:
        # On nettoie le nom pour le titre (ex: "ma_musique.mp3" -> "Ma musique")
        title = filename.replace('.mp3', '').replace('_', ' ').capitalize()
        
        # On crée l'URL "Raw" pour GitHub
        url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{filename}"
        
        playlist.append({
            "title": title,
            "url": url
        })

    # On écrit le fichier playlist.json
    with open('playlist.json', 'w', encoding='utf-8') as f:
        json.dump(playlist, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Terminé ! {len(playlist)} musiques ajoutées dans playlist.json")

if __name__ == "__main__":
    generate_json()