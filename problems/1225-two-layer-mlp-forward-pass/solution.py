import torch
import torch.nn as nn


def two_layer_mlp_forward(x, w1, b1, w2, b2):
    """Build a 2-layer MLP, set fixed weights, return scalar output.

    Args:
        x (torch.Tensor): Input of shape (1, 2).
        w1 (torch.Tensor): First Linear weight, shape (2, 2).
        b1 (torch.Tensor): First Linear bias, shape (2,).
        w2 (torch.Tensor): Second Linear weight, shape (1, 2).
        b2 (torch.Tensor): Second Linear bias, shape (1,).

    Returns:
        float: Scalar network output.
    """
    # TODO
    linear1 = nn.Linear(2,2)
    relu = nn.ReLU()
    linear2 = nn.Linear(2,1)

    with torch.no_grad():
        linear1.weight.copy_(w1)
        linear1.bias.copy_(b1)
        linear2.weight.copy_(w2)
        linear2.bias.copy_(b2)

    model = nn.Sequential(
        linear1,
        relu,
        linear2
    )

    output = model(x)

    return float(output.item())
