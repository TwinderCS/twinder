# La fonction qui met à jour les candidates quand on appuie sur le bouton de gauche ou de droite.
# "lr" vaut +1 si on a swipe droite, -1 si on a swipe gauche
def main(lr, n_clicks):
    if lr == 1:
        return "C'est un match ! (" + str(n_clicks) + ")"
    if lr == -1:
        return "Quel dommage... (" + str(n_clicks) + ")"