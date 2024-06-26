# analog_to_digital
Simulateur d'horloges mécaniques pour former une horloge digitale

## Utilité :

Ce projet permet de se représenter différentes transitions et chiffres que nous pourrions former avec des horloges en forme matricielle. Son utilité est principalement pour voir et pouvoir faire des choix matériels pour créer une horloge digitale avec des horloges à aiguilles en ayant un aperçu de ce que l'horloge digitale montrerait.

## Prise en main :

Ce simulateur est composé de deux parties :
<ul>
<li>le code dans le dossier horloge permet d'afficher les transitions et horloges</li>
<li>le code dans le dossier fichier permet d'envoyer les transitions et chiffres qu'on veut tester <b>après avoir lancé le code dans le dossier horloge</b></li>
</ul>

### Dossier horloge

Pour lancer le simulateur, il faut tout d'abord lancer simulateur.py (en étant dans le bon dossier) avec les arguments qu'il faut :
<ul>
<li>--help ou -h : permet de voir ce qu'il faut mettre comme arguments</li>
<li>--version : montre la version du simulateur</li>
<li>< hauteur > < largeur > < nbligne > < nbcolonne > < butée > : permet de lancer le simulateur avec la taille de la fenêtre voulue (< hauteur > et < largeur >), le nombre d'horloges voulu avec le nombre de lignes et de colonnes voulues (< nbligne > et < nbcolonne >), ainsi que si on veut une butée (1) ou pas de butée (0)</li>
</ul>

### Dossier fichier

Pour visualiser ce qu'on veut, nous avons deux possibilités (dans un autre terminal que celui du simulateur.py et dans le bon dossier) :
<ul>
  <li>lancer fichier.py après avoir vérifié dans les dossiers parametres, transitions et chiffres que les informations sont bonnes avec les transitions que nous voulons (plus de détails après) avec comme argument un fichier dans parametres</li>
  <li>lancer test_transition.py aves les mêmes arguments, en pouvant changer la transition que nous voulons voir</li>
</ul>

#### Pour lancer fichier.py :

Pour lancer la fonction principale, il faut tout d'abord se placer dans le dossier fichier, et lancer le fichier.py avec les arguments suivants:
<ul>
<li> < nom du fichier >  < butée > : ces arguments représentent respectivement le nom du fichier du dossier paramètres que l'on souhaite lancer et si l'on souhaite (1) ou non (0) activer la fonction permettant de changer le sens des aiguilles pour qu'elles évitent les butées</li>
<li>--help ou -h : permet de voir ce qu'il faut mettre comme arguments</li>
<li>--version : montre la version du simulateur</li>
<li>Notez qu'il est essentiel de faire correspondre le nombre de lignes et de colonnes du simulateur avec ceux indiqués dans le fichier de paramètres que l'on souhaite lancer</li>
</ul>

#### Pour lancer test_transition.py :

Les consignes sont les mêmes que pour lancer fichier.py, à noter que les paramètres du simulateur (nombre de lignes, nombre de colonnes et butée) seront écrasés et remplacés automatiquement par ceux indiqués lors du lancement de test_transition.py.
Notez qu'avec test_transition.py, activer la fonction pour éviter les butées active automatiquement les butées sur le simulateur et inversement.

#### Données qu'on peut modifier pour tester des transitions différentes :

Les fichiers qu'on peut modifier sont :
<ul>
  <li>tout d'abord dans le dossier parametres, il y a les paramètres globaux (on peut ajouter des lignes ou colonnes, changer les transitions, les fonctions cadres, modifier où apparaissent les chiffres ...)</li>
  <li>dans le dossier transitions, on peut ajouter ou modifier une transition (c'est aussi le cas dans generation_transition, il faut par contre supprimer le fichier correspondant dans le dossier transitions pour que la fonction soit appelée)</li>
  <li>dans le dossier chiffre, on peut modifier, ajouter des chiffres dans différents formats</li>
  <li>dans le dossier fonctions, dans le fichier fonctions_cadre.py, on peut modifier ou ajouter les fonctions qui génèrent les cadres</li>
</ul>
NB : Attention à ce que vous mettiez les bonnes données, par exemple si vous mettez des nombres d'horloges différents, si vous mettez la butée d'un côté mais pas de l'autre ou si vous mettez un chiffre sur des horloges qui n'existent pas, vous n'aurez pas un résultat graphique satisfaisant ou vous aurez des erreurs. Aussi, au début de l'envoi des données sur test_transition.py surtout, les transitions ne sont pas complètement envoyées. Il faut attendre la deuxième fois qu'elles apparaissent pour les voir complètement.

## Aide :

Si vous êtes le groupe d'EI qui reprend le projet, allez faire un tour chez les MAIN4. Il y a nos noms en bas.  

## Contributeurs au projet et outils utilisés :
Nous avons fait ce projet en python, du 14 février au 20 mai 2024.

### Ressource:
<ul>
  <li>socketio</li>
  <li>pygame</li>
  <li>time</li>
  <li>json</li>
  <li>pickle</li>
  <li>queue</li>
  <li>regular expression (re)</li>
  <li>datetime</li>
  <li>importlib</li>
  <li>thread</li>
  <li>docopt</li>
</ul>

### Contributeurs :
<ul>
<li>Marina MOUELE</li>
<li>Cassandra DELPLANQUE</li>
<li>Nour RACHDI</li>
<li>Alex FAUCHEU</li>
</ul>
