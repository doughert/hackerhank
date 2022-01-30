if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    winner = arr[0]
    for i in arr[1:]:
        if i != winner:
            print(i)