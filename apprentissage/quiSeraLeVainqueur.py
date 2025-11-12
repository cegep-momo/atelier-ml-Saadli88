# PARTIE 3 prediction combat

#Module de lecture de fichiers CSV
import csv
#Module de chargement du modèle d'apprentissage
import joblib

#---------------------------------------------
#  FONCTION DE RECHERCHE D'INFORMATIONS
#---------------------------------------------
def rechercheInformationsPokemon(numPokemon, Pokedex):
    infosPokemon = []
    for pokemon in Pokedex:
        if int(pokemon[0]) == numPokemon:
            infosPokemon = [
                pokemon[0],  # NUMERO
                pokemon[1],  # NOM
                pokemon[4],  # POINTS_DE_VIE
                pokemon[5],  # NIVEAU_ATTAQUE
                pokemon[6],  # NIVEAU_DEFENSE
                pokemon[7],  # NIVEAU_ATTAQUE_SPECIALE
                pokemon[8],  # NIVEAU_DEFENSE_SPECIALE
                pokemon[9],  # VITESSE
                pokemon[10]  # GENERATION
            ]
            break
    return infosPokemon

#---------------------------------------------
#  FONCTION DE PREDICTION DU VAINQUEUR
#---------------------------------------------
def prediction(numeroPokemon1, numeroPokemon2, Pokedex):
    pokemon1 = rechercheInformationsPokemon(numeroPokemon1, Pokedex)
    pokemon2 = rechercheInformationsPokemon(numeroPokemon2, Pokedex)
    
    # Chargement du modèle
    modele_prediction = joblib.load('modele/modele_pokemon.mod')
    
    # Prédiction pour chaque Pokémon
    prediction_Pokemon_1 = modele_prediction.predict([[
        float(pokemon1[2]), float(pokemon1[3]), float(pokemon1[4]),
        float(pokemon1[5]), float(pokemon1[6]), float(pokemon1[7]), float(pokemon1[8])
    ]])
    prediction_Pokemon_2 = modele_prediction.predict([[
        float(pokemon2[2]), float(pokemon2[3]), float(pokemon2[4]),
        float(pokemon2[5]), float(pokemon2[6]), float(pokemon2[7]), float(pokemon2[8])
    ]])
    
    # Affichage des résultats
    print(f"COMBAT OPPOSANT : ({numeroPokemon1}) {pokemon1[1]} à ({numeroPokemon2}) {pokemon2[1]}")
    print(f" {pokemon1[1]}: {prediction_Pokemon_1[0]}")
    print(f" {pokemon2[1]}: {prediction_Pokemon_2[0]}\n")
    
    if prediction_Pokemon_1 > prediction_Pokemon_2:
        print(pokemon1[1].upper() + " EST LE VAINQUEUR !")
    else:
        print(pokemon2[1].upper() + " EST LE VAINQUEUR !")

#---------------------------------------------
#  EXECUTION DU SCRIPT AVEC LE POKEDEX
#---------------------------------------------
with open("datas/pokedex.csv", newline='') as csvfile:
    pokedex = csv.reader(csvfile)
    next(pokedex)  # Ignorer l’en-tête
    prediction(368, 598, pokedex)
