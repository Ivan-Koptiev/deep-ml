def OSA(source: str, target: str) -> int:
	# Your code here
	len_s1, len_s2=len(source), len(target)

    dp=[[0]*(len_s2+1) for _ in range(len_s1+1)]

    for i in range(len_s1+1):
        dp[i][0]=i
    for j in range(len_s2+1):
        dp[0][j]=j

    for i in range(1,len_s1+1):
        for j in range(1,len_s2+1):
            if source[i-1]==target[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(
                    dp[i-1][j]+1,
                    dp[i][j-1]+1,
                    dp[i-1][j-1]+1
                )
            if i>1 and j>1 and source[i-1]==target[j-2] and source[i-1]==target[j-1]:
                dp[i][j]=min(dp[i][j], dp[i-2][j-2]+1)

    return dp[len_s1][len_s2]
