def sumDigit(n):
   if n < 10:
      return n
   return sumDigit(n//10) + n%10

if __name__ == '__main__':
   n = int(input())
   print(sumDigit(n))