# analog_to_digital
Code from analog clocks to digital clocks

ressource:
<li>socketio</li>

CE QU'ON A FAIT AUJ (premières scénce):


Questions :

Quelles entrées et sorties avons-nous accès ?

(Avons-nous accès à l'heure tout le temps ?

Est-ce des vrais horloges ?)

Préciser quelles transitions

A-t-il déjà quelque chose ou devons-nous partir de 0 ?

Qu'est-ce que le simulateur doit exactement montrer ?

Peut-on utiliser un autre langage pour le simulateur (CSS/HTML ou autre)


Maintenant : 

Faire un simulateur (des ronds avec des barres qui tournent à une certaine vitesse ?)

Faire un fichier avec les détails des nombres et des transitions simples


Idées pour les transitions :

"Je suis batman"

PACMAN

transitions simplesw ou complexes (faire bouger uniquement les hirloges concernées ou toutes les horloges)




<h1>SEANCE 21 / 02: </h1>
FAIT:
<li>classe horloge , classe essai horloge</li>
on a fait un programme qui dessine une horloge et met ses aiguilles en une position spécifique .
<li>>Découverte de pygame et initiation à son utilisation</li>
<h3>récision des objectifs du projet:</h3>
  -faire un simulateur d'une horloge "réaliste"
  -déterminer quelle type de truc qui permet de faire bouger les aiguilles est le plus adaptées, entre un qui bloque au bout d'un 360 ou celui qui ne se bloque pas mais peut se décaler de qq degrée 
  -faire des transitions classes
  
ETAPE DU PROJET (provisoire):
Etape 1:
créer un similateur simple (2 programmes séparés?) avec transition 
afficher chiffres puis afficher lettres puis combiner les deux
Etape2:
déterminer quel type d'engrenage est le plus adaptés,

Etape 3:
faire transition classes et améliorer le code

<h1>SEANCE 28 / 02: </h1>

<h3>OBJECTIFS: </h3>
<ul>
  <li>Faire une classe grille qui dessine toutes les horloges,</li>
  <li>Faire une classe chiffre qui dessine un chiffre donné en argument </li>
</ul>



<h3>QUESTIONS: </h3>
<ul>
  <li>Confirmer que c'est deux programmes différents (un simulateur + un code = on fait dssiner le truc directement) =OUI</li>
  <li>socket? thread?=Comme on veux </li>
  <li>demander clocktick fonctionnement pour déterminer le bon pas pour les transitions= pas d'interet pour ça</li>
  <li>format texte pour savoir les éléments (heure, jour, année,...) et l'ordre .?<= comme on veut possible de le faire à nous de décider/li>
  <li>Interface ou pas ?(simulateur avec interface ou non ?)= NON pas necessaire mtn</li>
  </ul>
    
 <h3>PISTES </h3>
 <ul>
 <li>pour le code= faire classe élément interessant</li>pour le code= faire classe élément interessant</li> 
 <li>utiliser surcharge opérateur ou property pour faire set</li>
 <li>faire un intervalle [thetha_int-pas; thetha-int+pas] pour déterminer quand l'aiguille s'arrête</li>
 <li>envisager idée de faire fonction position dans horloges et non donner deux angles à chaque fois</li>
 <li>bien commenter le code</li>
 <li>verifier si la taille de l'écran et l'espace entre les horloges n'impactent pas l'esthétisme</li>
    
</ul>
