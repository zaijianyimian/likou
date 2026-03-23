import sys

input = sys.stdin.readline
if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    arr = list(map(int, input().split()))
    question = []
    for i in range(m):
        question.append(list(map(int, input().split())))
    # print(question)
    count = arr.count(0)
    tmp = sum(arr)
    for num in question:
        min = count * num[0] + tmp
        max = count * num[1] + tmp
        print(f'{min} {max}')
