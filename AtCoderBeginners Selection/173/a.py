def main():
    N = int(input())
    
    res = N % 1000
    if res == 0:
        print(res)
    else:
        print(abs(res-1000))

if __name__ == '__main__':
    main()
    