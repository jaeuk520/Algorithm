def main():
    str = input()
    cnt=0
    while(str.find('O') != -1):
        idx = str.find('O')
        str1 = str[:idx]
        if(str1.find('X') != -1):
           str1 = str1.replace('X', 'O')
        if(len(str) == idx):
            str = str1 + 'X'
        else:
            str = str1 + 'X' + str[idx+1:]
        cnt += 1
        cnt %= 10^9 + 7
        print(str)
    print(cnt)


if __name__=="__main__":
    main()
