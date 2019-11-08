RAPPORT BE ACOUSTIQUE SOUS-MARINE ET TEMPS-FRÉQUENCE
====================================================




Chants de baleines et temps-fréquence
-------------------------------------

###STFT inverse et filtrage
-Le premier code fourni commence par créer un signal avec une modulation fréquentielle linéaire.
On lui applique ensuite une fenêtre de Hamming puis une transformée de Fourier à court terme.
Cela nous donne un spectrogramme temps-fréquence parfaitement linéaire qui montre bien l'évolution de la fréquence au court du temps.
Puis par transformée inverse, nous reconstruisons le signal d'origine avec une bonne approximation.


-Le second code fourni commence par créer un signal bruité, toujours avec une modulation fréquentielle linéaire.
Par transformée de Fourier appliquée avec une fenêtre de Hamming, on retrouve encore l'évolution de la fréquence au court du temps.
Cette évolution suit toujours une droite, mais l'influence du bruit est visible sur le spectrogramme. Pour l'éliminer, nous construisons
donc un masque autour de la droite d'intérêt qui aura pour effet de couper les fréquences qui en sont éloignées.
Puis nous reconstruisons le signal débruité par transformée inverse.
