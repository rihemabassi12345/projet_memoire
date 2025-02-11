import os

DOSSIER_VIDEOS = r"C:\Users\ASUS\OneDrive\Desktop\projet_memoire\sport"

fichiers_videos = []

# Utiliser os.walk pour parcourir tous les fichiers dans le dossier et ses sous-dossiers
for racine, dossiers, fichiers in os.walk(DOSSIER_VIDEOS):
    for fichier in fichiers:
        # Vérifier si le nom du fichier se termine par l'une des extensions souhaitées (vous pouvez en ajouter d'autres si nécessaire)
        if fichier.lower().endswith(('.mp4', '.avi', '.mov')):
            # Ajouter le chemin complet du fichier à la liste
            fichiers_videos.append(os.path.join(racine, fichier))

print("Fichiers vidéo trouvés :", fichiers_videos)
