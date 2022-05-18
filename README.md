### Pourquoi utiliser GAIL au lieu de Behavorial cloning ou IRL ?
#
#### Behavorial cloning
Cela consiste à créer un dataset supervisé ou chaque observation en input a une action en output

Avantages: 
- simple à mettre en place

Inconvénients:
- l'algorithme sera inneficace lorsqu'il rencontrera des valeurs éloignées du dataset d'entrainement (behavorial cloning)
#
#### Inverse reinforcement learning (IRL)
On va dans un premier temps créer un modèle qui renverra une cost function telle qu'elle permettra d'expliquer les actions de l'expert puis une fois la cost fonction obtenue, on pourra effectuer du reinforcement learning traditionnel

Avantages:
- blabla

Inconvénients:
- blabla
#
#### GAIL
Reprend le principe du GAN avec un générateur et un discriminateur. Le générateur va générer les séries d'actions, ensuite le discriminateur recevra en entrée à la fois des séries d'actions d'expert et générateur et devra déterminer lesquelles viennent de l'expert et inversement.

Avantages:
- blabla

Inconvénients:
- blabla