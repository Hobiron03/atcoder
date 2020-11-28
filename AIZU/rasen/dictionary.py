def main():
    num = int(input())
    lines = [input() for _ in range(0, num)]
    
    m = 101
    command_dictionary = [0 for _ in range(0, m)]
    for line in lines:
        command = line.split(" ")[0]
        string = line.split(" ")[1]
        

if __name__ == '__main__':
    main()
    