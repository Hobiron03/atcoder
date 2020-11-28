import sys
def main():
    x, y = map(int, input().split())
    
    for i in range(0, x+1):
        for j in range(0, x-i+1):
            res = i * 2 + j * 4
            if y == res and i + j == x:
                print('Yes')
                sys.exit()
                
    print('No')

if __name__ == '__main__':
    main()
    