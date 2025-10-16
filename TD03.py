import praw
import pandas as pd
import os

# Vérifie si le fichier CSV existe déjà
fichier_csv = "reddit_textes.csv"

if os.path.exists(fichier_csv):
    # Si le fichier existe, on le charge directement 
    print("📂 Le fichier existe déjà, chargement depuis le disque...")
    df = pd.read_csv(fichier_csv, sep="\t", encoding="utf-8")
else:
    # Sinon, on interroge l'API Reddit 
    print("🌐 Aucun fichier trouvé, interrogation de l'API Reddit...")

    reddit = praw.Reddit(
        client_id='DNRXo8NPa6OMRFGifCP7ug',
        client_secret='GBmiInh5G9lSr6vEYEk8y_mDjbnFEQ',
        user_agent='TD003'
    )

    submission = reddit.submission(id="a3p0uq")
    submission.comments.replace_more(limit=0)

    data = []
    identifiant = 1

    # Texte du post principal
    data.append([identifiant, submission.selftext, "reddit"])
    identifiant += 1

    # Tous les commentaires
    for comment in submission.comments.list():
        data.append([identifiant, comment.body, "reddit"])
        identifiant += 1

    # Création du DataFrame
    df = pd.DataFrame(data, columns=["id", "texte", "origine"])

    # Sauvegarde avec tabulation comme séparateur
    df.to_csv(fichier_csv, index=False, sep="\t", encoding="utf-8")
    print("✅ Données récupérées et sauvegardées dans 'reddit_textes.csv'.")

# Affichage d’un aperçu 
print("\nAperçu des données chargées :")
print(df.head())

# --- 3.1 Afficher la taille du corpus ---
taille_corpus = len(df)
print(f"\n📊 Taille du corpus : {taille_corpus} documents")
