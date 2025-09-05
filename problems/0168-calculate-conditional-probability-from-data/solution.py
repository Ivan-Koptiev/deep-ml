def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    count_xx_yy=0
    count_xx=0
    final_prob=0
    for i in data:
        if i[0]==x and i[1]==y:
            count_xx_yy+=1
        if i[0]==x:
            count_xx+=1

    if count_xx==0:
        return 0.0
    else:
        return round(count_xx_yy/count_xx, 4)
