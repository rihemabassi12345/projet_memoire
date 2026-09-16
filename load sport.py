import os
DOSSIER_VIDEOS = r"C:\Users\ASUS\OneDrive\Desktop\projet_memoire\sport"
fichiers_videos = []
for racine, dossiers, fichiers in os.walk(DOSSIER_VIDEOS):
    for fichier in fichiers:
        if fichier.lower().endswith(('.mp4', '.avi', '.mov')):
            fichiers_videos.append(os.path.join(racine, fichier))

print("Fichiers vidéo trouvés :", fichiers_videos)
