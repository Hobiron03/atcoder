def main():
    N = int(input())
    judges = [input() for _ in range(N)]
    
    res_dic = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    for judge in judges:
        if judge in res_dic:
            res_dic[judge] += 1
        else:
            res_dic[judge] = 0
            
    for k, v in res_dic.items():
        print("{} x {}".format(k, v))

if __name__ == '__main__':
    main()