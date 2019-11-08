RAPPORT BE ACOUSTIQUE SOUS-MARINE ET TEMPS-FRÉQUENCE --- Adam Philibert & Bouveron Matthieu
===========================================================================================




Chants de baleines et temps-fréquence
-------------------------------------

### STFT inverse et filtrage    

- Le premier code fourni commence par créer un signal avec une modulation fréquentielle linéaire.
On lui applique ensuite une fenêtre de Hamming puis une transformée de Fourier à court terme.
Cela nous donne un spectrogramme temps-fréquence parfaitement linéaire qui montre bien l'évolution de la fréquence au court du temps.
Puis par transformée inverse, nous reconstruisons le signal d'origine avec une bonne approximation.  


- Le second code fourni commence par créer un signal bruité, toujours avec une modulation fréquentielle linéaire.  Par transformée de Fourier appliquée avec une fenêtre de Hamming, on retrouve encore l'évolution de la fréquence au court du temps.
Cette évolution suit toujours une droite, mais l'influence du bruit est visible sur le spectrogramme. Pour l'éliminer, nous construisons
donc un masque autour de la droite d'intérêt qui aura pour effet de couper les fréquences qui en sont éloignées.
Puis nous reconstruisons le signal débruité par transformée inverse.  

	- Première solution pour le masque: on considère la matrice issue de la transformée de Fourier à court terme comme une image et on 
dessine une région d'intérêt à la main autour des zones où l'énergie est la plus élevée. Cela nous donne un masque binaire, que l'on utilise pour ne conserver que les parties intéressantes du spectrogramme. A partir de ce spectrogramme filtré on peut alors reconstruire le signal débruité par transformée inverse.  

	- Seconde solution pour le masque: on filtre automatiquement en utilisant un seuil d'énergie. Pour que le filtrage soit à peu près généralisable, nous avons choisi de normaliser le spectrogramme. De même que précédemment, on reconstruit le signal à partir du spectrogramme filtré.  



### Application aux chants de baleines

- Le spectrogramme est la représentation la plus adaptée car il permet de visualiser et localiser dans le temps les bandes de fréquences correspondant au bruit, ce qui est utile pour le filtrage.  

- Les vocalises sont visibles sur le spectrogramme, mais ont une énergie faible par rapport au bruit. Elles sont dans les basses fréquences.  

- Le bruit est permanent, avec une énergie importante.  

- Les vocalises sont audibles mais très graves et partiellement masquées par le bruit. Pour les rendre audibles avec la fonction *sound* de Matlab, il suffit d'augmenter la fréquence d'échantillonage ("accélérer l'audio").  

	- Connaissant le spectrogramme du signal bruité, nous savons dans quelle zone se trouvent les vocalises et nous fabriquons un filtre qui les englobe en passant toutes les autres zones à 0. Cela permet de récupérer la vocalise avec sa première harmonique (d'énergie netteent plus faible encore).  

	- Nous combinons ensuite ce premier filtre manuel avec un filtre permettant de prendre en compte les énergie, en considérant que les pics d'énergie les plus important parmi les restants correspondent à la vocalise et ses harmoniques.  

	- Pour chaque filtre ajouté, on a bien éliminé du bruit et le son est plus clair.  


### Clics d’écholocation et analyse temps-rythme

On suppose que pour chaque individu le rythme d’émission des clics est approximativement constant sur une durée de 500 ms, donc en identifiant les différents rythmes d'émission on peut espérer obtenir une bonne estimation du nombre de dauphins en émission.  

Pour obtenir les différents rythmes, plusieurs étapes sont nécessaires:

- On commence par filtrer le signal d'origine pour faire apparaître uniquement à chaque instant s'il y a eu émission ou non. Cela donne un vecteur à valeurs binaires.

- On crée ensuite une série de vecteurs sous le même format correspondant à des émissions entre 15 et 100Hz. Ils serviront de références pour analyser le signal selon ses réponses aux sollicitations de différentes fréquences.

- En utilisant la fonction *xcorr* de Matlab, on relève les valeurs de corrélation entre le signal de *clics* et les différents signaux de référence. Une valeur élevée montre la présence d'un dauphin émettant à cette fréquence. En comptant les fréquences pour lesquelles on obtient une forte corrélation, on obtient une estimation du nombre de dauphins.





*ADAM Philibert & BOUVERON Matthieu*












