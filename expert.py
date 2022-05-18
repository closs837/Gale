import torch
import json

from nets import Expert


# fonctionne uniquement pour cartpole
def return_expert():
    # si cuda disponible, on utilise le gpu sinon le cpu
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    with open('cartpole/model_config.json') as f:
        expert_config = json.load(f)

    # Initiliase l'expert
    expert = Expert(4, 2, True, **expert_config).to(device)

    # Charge le modèle déjà pré-entrainé
    expert.pi.load_state_dict(
        torch.load(
            'cartpole/expert/policy.ckpt', map_location=device
        )
    )
    return expert


