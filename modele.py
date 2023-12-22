class Model:
    def __init__(self):
        # C'est ici il faut charger le modèle 
        pass

    def predict(self, data):
        "Renvoie le coté où se trouve la poubelle et la couleur de la poubelle"
        
        #ce code est juste là pour permettre d'effectuer les tests en toute tranquillité EN ATTENTE DU MODULE DE L'EQUIPE IA
        
        cat_poubelle = {"GLASS" : "vert", "ORGANIC" : "marron", "PAPER" : "bleu", "PLASTIC" : "rouge",  }
        """import random
        dechet =  random.choices(["GLASS", "ORGANIC", "PAPER", "PLASTIC"])[0]
        poubelle = cat_poubelle[dechet]
        print(f"Déchet type : {dechet} \nPoubelle correspondante : {poubelle}")
        # ici on cherche si c'est à gauche ou à droite se trouve la poubelle
        cote = random.choices(["gauche", "droit"])[0]
        print(f"Elle se trouve du coté {cote}")"""
        return "gauche", "rouge"
    
if __name__ == "__main__":
    ia = Model()
    ia.predict()