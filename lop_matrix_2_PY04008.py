from sys import stdin

class Matrix:
    def __init__(self, n, m, a):
        self.__n = n
        self.__m = m
        self.__a = a

    def transp(self):
        b = [[0 for _ in range(self.__n)] for _ in range(self.__m)]
        for i in range(self.__n):
            for j in range(self.__m):
                b[j][i] = self.__a[i][j]
        return Matrix(self.__m, self.__n, b)

    def __mul__(self, other):
        ans = [[0 for _ in range(self.__n)] for _ in range(self.__n)]
        for i in range(self.__n):
            for j in range(self.__n):
                for k in range(self.__m):
                    ans[i][j] += self.__a[i][k] * other.__a[k][j]
        return Matrix(self.__n, self.__n, ans)

    def __str__(self):
        ans = ''
        for i in range(self.__n):
            for j in range(self.__m):
                ans += str(self.__a[i][j]) + ' '
            ans += '\n'
        return ans[:-1]

if __name__ == '__main__':
    data = []
    for line in stdin:
        data += map(int, line.split())
    t = data[0]
    index = 1
    for _ in range(t):
        n, m = data[index], data[index + 1]
        index += 2
        a = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a[i][j] = data[index]
                index += 1
        matrix = Matrix(n, m, a)
        trans = matrix.transp()
        print(matrix * trans)
        
