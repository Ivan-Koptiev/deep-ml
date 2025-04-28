def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Your code here
    #derivative=4x^3 -9x^2

    def f(x):
        return ((x**4)-(3*x**3)+2)

    def f_prime(x):
        return ((4*x**3)-(9*x**2))

    learning_rate = 0.01
    tolerance = 1e-6
    x = start_x
    max_iterations = 1000
    iteration=0
    momentum_factor=0.9
    velocity=0

    while iteration < max_iterations:
        previous_x = x
        slope = f_prime(x)
        velocity = momentum_factor * velocity + learning_rate * slope
        x=x-velocity
        if abs(x - previous_x) < tolerance:
            break
        iteration += 1

    return x