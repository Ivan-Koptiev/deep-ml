def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    #d/dx(cx^n)=c*n*x^n-1
    dx=c*n*x**(n-1)
    return dx