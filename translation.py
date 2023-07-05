from translate import Translator

print("""Informations complementaires:
    \tAnglais: en
    \tFrançais: fr
    \tChinois: zh
    \tEspagnol: es
    \tAllemand: de
    \tItalien: it
    \tRusse: ru
    \tJaponais: ja
    \tCoréen: ko
    \tPortugais: pt
    \tArabe: ar
    \tHindi: hi
    \tNéerlandais: nl
    \tSuédois: sv
""")

#la liste des codes valable
liste = ['en', 'fr', 'zh', 'es', 'de', 'it', 
         'ru', 'ja', 'ko', 'pt', 'ar', 'hi', 'nl', 'sv']  

# Choix et validation du code du langage choisi
lang = ""
while lang not in liste :
    if lang == "":
        lang = input("Entrer le code de la langue que vous avez choisie: ")
    else:
        lang = input("Entrer le code de la langue que vous avez choisie(un code valable svp): ")
print("code de langue validé")

#Création du traducteur
translator = Translator(to_lang=lang)

#Traduction
phrase_a_traduire = input("Et alors quelle phrase voulez-vous traduire? ")
phrase_traduite = translator.translate(phrase_a_traduire)

#sortie de la traduction
print (f"*** Phrase à traduire:\n\t{phrase_a_traduire}\n\n*** Traduction: \n\t{translator.translate(phrase_a_traduire)}")
 