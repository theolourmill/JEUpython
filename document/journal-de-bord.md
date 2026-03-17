Le but de ce petit jeu en python est de pouvoirune fênetre simple, ou le joueur
pourra cliquer sur un bouton pour créer une ressource puis acheter des améliorations
qui l'aiderons dans son aventure.
J'utiliserai une interface simple, donc tkinter sera suffisant, voici quelques idées 
préliminaires :

1) système de sauvegarde
2) cout exponentiel
3) plusieurs niveau d'améliorations
4) Systèmes de statistiques

Pour l'interface visuelle (surtout au niveau de la cohérence des boutons),
j'utiliserai la fonction .grid de tkinter, qui repose "presque" sur le même
principe que les flexbox de CSS.
Pour le moment, dans le jeu final il y aura 5 machines, je copie colle la logique de la machine 1, 5 fois ce qui est au
passage vraiment peu utile, je réglerai ça plus tard (surement avec un dictionnaire avec le tick de production de chaque machine, on pourrait même imaginer des bonus de production etc...).
