import sys
def main():
    x_num, n = map(int, input().split())
    
    p_nums = list(map(int, input().split()))
    
    if n == 0:
        print(x_num)
        sys.exit()
    
    i = 1
    while(True):
        up_num = x_num + i
        down_num = x_num - i
        
        up_sub = abs(x_num - up_num)
        down_sub = abs(x_num - down_num)
        
        if up_num in p_nums:
            if down_num in p_nums:
                i+= 1
                continue
            else:
                if down_num == 0:
                    i+= 1
                    continue
                print(down_num)
                sys.exit()
        else:
            if down_num in p_nums:
                if up_num == 0:
                    i+= 1
                    continue
                print(up_num)
                sys.exit()
            elif up_sub == down_sub:
                if down_num == x_num:
                    i+= 1
                    continue
                print(min(up_num, down_num)) 
                sys.exit()
        i += 1
if __name__ == '__main__':
    main()
    