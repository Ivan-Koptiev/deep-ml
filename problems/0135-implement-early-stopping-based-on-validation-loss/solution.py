from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    """
    Implements early stopping based on validation loss.
    
    Parameters:
    val_losses: List of validation losses for each epoch.
    patience: Number of epochs to wait for improvement before stopping.
    min_delta: Minimum change in validation loss to count as an improvement.
    
    Returns:
    A tuple (stop_epoch, best_epoch), where:
        - stop_epoch is the epoch index at which training should stop (based on early stopping).
        - best_epoch is the epoch with the lowest validation loss.
    """
    
    best_loss = float('inf')  # Start with an infinitely large loss
    best_epoch = 0  # The epoch with the best loss
    no_impr = 0  # Counter for how many epochs since last improvement
    
    for epoch in range(len(val_losses)):
        current_loss = val_losses[epoch]
        
        # If there's an improvement 