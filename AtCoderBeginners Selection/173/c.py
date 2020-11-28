import itertools

def main():
    H, W, K = map(int, input().split())
    matrix = []
    for i in range(H):
        s = list(input().split())
        matrix.append(list(s[0]))
        
    #iはmatrix[i]
    #jはmatrix[i]
    res = 0
    if count_sharp(matrix) == K:
        res += 1
    
    matrix2 = matrix.copy()
    for i in range(0, H):
        matrix = matrix2.copy()
        matrix[i] = ["a" for i in range(0, W)]
        for j in range(0, W):  
            matrix[i][j] = "a"
            if count_sharp(matrix) == K:
                res += 1
    
    print(matrix)

def count_sharp(matrix):
    print(list(itertools.chain.from_iterable(matrix)))
    sharp_num = 0
    for s in list(itertools.chain.from_iterable(matrix)):
        sharp_num += s.count("#")
    
    return sharp_num


if __name__ == '__main__':
    main()
    