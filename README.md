# analog_to_digital
Simulateur d'horloges mécaniques pour former une horloge digitale

## Utilité :

Ce projet permet de se représenter différentes transitions et chiffres que nous pourrions former avec des horloges en forme matricielle. Son utilité est principalement pour voir et pouvoir faire des choix matériels pour créer une horloge digitale avec des horloges mécaniques en ayant un aperçu de ce que l'horloge digitale montrerait.

## Prise en main :

Ce simulateur est composé de deux parties :
<ul>
<li>le code dans le dossier horloge permet d'afficher les transitions et horloges</li>
<li>le code dans le dossier fichier permet d'envoyer les transitions et chiffres qu'on veut tester <b>après avoir lancer le code dans le dossier horloge</b></li>
</ul>

### Dossier horloge

Pour lancer le simulateur, il faut tout d'abord lancer simulateur.py (en étant dans le bon dossier) avec les arguments qu'il faut :
<ul>
<li>--help ou -h : permet de voir ce qu'il faut mettre comme arguments</li>
<li>--version : montre la version du simulateur</li>
<li>$<$hauteur$>$ $<$largeur$>$ $<$nbligne$>$ $<$nbcolonne$>$ $<$butee$>$ : permet de lancer le simulateur avec la taille de la fenêtre voulue ($<$hauteur$>$ et $<$largeur$>$), le nombre d'horloges voulu avec le nombre de lignes et de colonnes voulu ($<$nbligne$>$ et $<$nbcolonne$>$), ainsi que si on veut une butée (1) ou pas de butée (0)</li>
</ul>

### Dossier fichier

Pour visualiser ce qu'on veut, nous avons deux possibilités (dans un autre terminal que celui du simulateur.py et dans le bon dossier) :
<ul>
<li>lancer test_transition.py et mettre en input le nom des transitions que l'on veut regarder sur le simulateur</li>
<li>lancer fichier.py après avoir vérifier dans les dossiers parametres, transitions et chiffres que les informations sont bonnes avec les transitions que nous voulons (plus de détails après) avec comme argument un fichier dans parametres</li>
</ul>

#### Pour lancer fichier.py :

Pour lancer la fonction principale, il faut tout d'abord se placer dans le dossier fichier, et lancer le fichier.py avec les arguments suivants:
<ul>
<li> \< nom du fichier \>  \< butée \> : ces arguments représentent respectivement le nom du fichier du dossier paramètres que l'on souhaite lancer et si l'on souhaite (1) ou non (0) activer la fonction permettant de changer le sens des aiguilles pour qu'elles évitent les butées</li>
<li>--help ou -h : permet de voir ce qu'il faut mettre comme arguments</li>
<li>--version : montre la version du simulateur</li>
<li>Notez qu'il est essentiel de faire correspondre le nombre de lignes et de colonnes du simulateur avec ceux indiqués dans le fichier de paramètres que l'on souhaite lancer</li>
</ul>

#### Pour lancer test_transition.py :

Les consignes sont les mêmes que pour lancer fichier.py, à noter que les paramètres du simulateur (nombre de lignes, nombre de colonnes et butée) seront écrasés et remplacés automatiquement par ceux indiqués lors du lancement de test_transition.py.
Notez qu'avec test_transition.py, activer la fonction pour éviter les butées active automatiquement les butées sur le simulateur et inversement.

## Aide :

Si vous êtes le groupe d'EI qui reprend le projet, aller faire un tour chez les MAIN4. Il y a nos noms en bas.  

## Contributeurs du projet et outils utilisé :
Nous avons fait ce projet en python, du 14 février au 19 mai 2024.

### Ressource:
<ul>
<li>socketio</li>
<li>pygame</li>
<li>time</li>
<li>json</li>
<li>pickle</li>
</ul>

### Contributeurs :
<ul>
<li>Marina MOUELE</li>
<li>Cassandra DELPLANQUE</li>
<li>Nour RACHDI</li>
<li>Alex FAUCHEU</li>
</ul>
