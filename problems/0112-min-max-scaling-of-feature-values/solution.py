def min_max(x: list[int]) -> list[float]:
    # Your code here
    x_max=max(x)
    x_min=min(x)
    norm_x=[]
    if x_max-x_min==0:
        for i in range(len(x)):
            norm_x.append(0.0)
        return norm_x
    else:
        for i in x:
            norm_x.append((i-x_min)/(x_max-x_min))
        return norm_x