def solve(nums,k):
    ans = 0
    tot = sum(nums[:k])
    ans = tot
    n = len(nums)
    for i in range(k-1, -1, -1):
        tot += nums[i+n-k] - nums[i]
        ans = max(ans,tot)
    
    return ans

nums = list(map(int,input().strip().split()))
k = int(input())

ans = solve(nums,k)
print(ans)