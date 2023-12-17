class SoPhuc:
    def __init__(self, real, vir):
        self.__real = real
        self.__vir = vir

    def __add__(self, other):
        real = self.__real + other.__real
        vir = self.__vir + other.__vir
        return SoPhuc(real, vir)
    
    def __mul__(self, other):
        real = self.__real * other.__real - self.__vir * other.__vir
        vir = self.__real * other.__vir + self.__vir * other.__real
        return SoPhuc(real, vir)

    def __str__(self):
        return f'{self.__real} + {self.__vir}i' if self.__vir >= 0 else f'{self.__real} - {abs(self.__vir)}i'

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        a = SoPhuc(arr[0], arr[1])
        b = SoPhuc(arr[2], arr[3])
        print((a + b) * a, (a + b) * (a + b), sep=', ')