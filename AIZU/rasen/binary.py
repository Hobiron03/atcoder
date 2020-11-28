def main():
    n = int(input())
    S = list(map(int, input().split()))

    q = int(input())
    T = list(map(int, input().split()))
    
    res = 0
    for t in T:
        res += binary_search(S, t)
        
    print(res)
        
def binary_search(S, t):
    left = 0
    right = len(S)
    
    res = 0
    while left < right:
        mid = (left + right) // 2
    
        if t > S[mid]:
            left = mid + 1
        elif t < S[mid]:
            right = mid
        else:
            res += 1
            break
            
    return res
    
if __name__ == '__main__':
    main()
    