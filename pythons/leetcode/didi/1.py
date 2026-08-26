import sys
input = sys.stdin.readline

n = int(input())
dic = {'p': 'd',
       '6': '9',
       'b': 'q',
       'E': '3'}
for i in range(n):
       n,k = map(int,input().split())
       left = set(dic)
       right = {'d','q','9','3'}
       stack = []
       s = input().strip()
       cnt = 0
       for ch in s:
              if ch in left:
                     stack.append(ch)
              else:
                     if not stack:
                            print('NO')
                            break
                     top = stack.pop()
                     if dic[top] != ch:
                            cnt += 1
                            if cnt > k:
                                   print('NO')
                                   break
       else:
              if stack:
                     print('NO')
              else:
                     print('YES')
