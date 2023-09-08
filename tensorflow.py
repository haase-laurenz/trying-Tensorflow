import tweepy
import time

# Twitter API-Anmeldeinformationen
API_KEY = 'LaIa7be8f4kBB4aU5r1kPcS71'
API_SECRET_KEY = 'HQefzrfbP7AQi18XrRp7r9lH3PDSmDEGbDrPls9FhM7zdipPCl'

ACCESS_TOKEN = '1700079980959453184-8hq3JqaXbIRpbwspktJFr6RHa20SOv'
ACCESS_TOKEN_SECRET = 'yaTxObwZ2l84XOVblCtFqbKuhVp1vJdCpUYGRg5UAuW6Q'

# Funktion zum Erstellen und Veröffentlichen eines Tweets
def create_and_post_tweet():
    # Authentifizierung bei Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Erstellen einer API-Instanz
    api = tweepy.API(auth)
    
    # Der zu veröffentlichende Tweet-Text
    tweet_text = "Dies ist ein automatisch erstellter Tweet."
    
    # Tweet veröffentlichen
    api.update_status(status=tweet_text)
    print("Tweet erfolgreich erstellt und veröffentlicht.")

# Schleife zum automatischen Erstellen und Veröffentlichen von Tweets alle 5 Minuten
while True:
    create_and_post_tweet()
    # Warten für 5 Minuten (300 Sekunden) vor der nächsten Iteration
    time.sleep(300)
