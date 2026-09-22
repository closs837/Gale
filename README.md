# Gale — GAIL on CartPole

Generative adversarial imitation learning in PyTorch: a policy and a value network trained
against a discriminator that has to tell generated rollouts apart from the expert's.
`cartpole/model_config.json` holds the training configuration and
`cartpole/expert/policy.ckpt` is the expert policy used to produce the demonstrations.

```
python gail.py
```

Notes from the report on why GAIL rather than behavioural cloning or IRL:

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