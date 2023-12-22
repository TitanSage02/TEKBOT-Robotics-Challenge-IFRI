from flask import Flask, render_template
from main import change_main_flag_to, thread_principal
import secrets
import asyncio

app = Flask(__name__)

user_links = set()
unique_link = secrets.token_hex(16)  # s'assurer qu'une et une seule personne pourra lancer le démarrage

@app.route('/')
def home():
    return render_template("acceuil.html")

@app.route('/start_robot')
def start():
    if unique_link not in user_links:
        user_links.add(unique_link)
        
        thread_principal.start()
        return "Robot démarré avec succès"
    
    else:
        
        return "Impossible, le robot a déjà été démarré"

async def start_flask():
    serveur_flask = asyncio.create_task(app.run(host='0.0.0.0', port=5000))
    print("Serveur démarré")

if __name__ == '__main__':
    try: 
        asyncio.run(start_flask())
    except:
        change_main_flag_to(False)
        thread_principal.join()