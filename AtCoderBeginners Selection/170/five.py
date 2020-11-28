def main():
    nums = map(int, input().split())
    for i, num in enumerate(nums, 1):
        if num == 0:
            print(i)
            break
            
if __name__ == '__main__':
    main()
    