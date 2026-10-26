import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    flat=torch.flatten(x)
    reshaped = torch.reshape(flat, (new_shape))
    return reshaped

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    # TODO: swap the last two dimensions of x
    new = torch.transpose(x, -2, -1)
    return new
