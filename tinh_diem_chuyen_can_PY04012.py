class Sinhvien:
    def __init__(self,dd,ma,ten,lop):
        self.dd=dd
        self.ma=ma
        self.ten=ten
        self.lop=lop
    def setdd(self,s):
        self.dd=s
    def getdd(self):
        return self.dd
    def getMa(self):
        return self.ma
    def diemchuyencan(self):
        res=self.dd
        m=res.count("m")
        v=res.count("v")
        cc=10-m-2*v
        if cc<=0:
            tmp=str(0)+" KDDK"
            return tmp
        return str(cc)
    def __str__(self):
        return self.ma+" "+self.ten+" "+self.lop+" "+self.diemchuyencan()
    
if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(Sinhvien("", input(), input(), input()))
    
    for _ in range(n):
        arr = input().split()
        for x in lst:
            if x.getMa() == arr[0]:
                x.setdd(arr[1])
                break
    
    for x in lst:
        print(x)
        