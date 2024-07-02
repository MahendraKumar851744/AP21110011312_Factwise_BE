def solve(n):
    l1 = ["","one","two","three","four","five","six","seven","eight","nine"]
    l2 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
          "seventeen","eighteen",'nineteen']
    l3 = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty',
          'ninety']
    
    const = "hundred"
    
    if n == 1000:
        return "onethousand"
    elif 1 <= n < 10:
        return l1[n]
    elif 10 <= n < 20:
        return l2[n-10]
    elif 20 <= n < 100:
        num1 = l3[n//10]
        num2 = l1[n%10]
        return num1 + num2
    elif 100 <= n < 1000:
        if n%100 != 0:
            return l1[n//100] + "hundredand" + solve(n%100)
        else:
            return l1[n//100] + const
        
    
ans = 0
for i in range(1,1001):
    ans += len(solve(i))
    
print(ans)  # I got ans 21124