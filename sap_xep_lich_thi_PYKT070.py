class MonThi:
    def __init__(self, id, name, form):
        self.__id = id
        self.__name = name
        self.__form = form

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_form(self):
        return self.__form

class CaThi:
    cnt = 0

    def __init__(self, date, time, room):
        CaThi.cnt += 1
        self.__id = f'C{CaThi.cnt:03d}'
        self.__date = date
        self.__time = time
        self.__room = room

    def get_id(self):
        return self.__id
    
    def get_date_to_int(self):
        a = self.__date.split('/')
        a = a[::-1]
        return int(''.join(a))

    def get_time_to_int(self):
        return int(self.__time[:2]) * 60 + int(self.__time[3:])

    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time
    
    def get_room(self):
        return self.__room
    
class LichThi:
    def __init__(self, idCaThi, idMonThi, group, amount):
        self.__idCaThi = idCaThi
        self.__idMonThi = idMonThi
        self.__group = group
        self.__amount = amount

    def get_id_CaThi(self):
        return self.__idCaThi

    def get_id_MonThi(self):
        return self.__idMonThi

    def set_CaThi(self, cathi):
        self.__cathi = cathi

    def set_MonThi(self, monthi):
        self.__monthi = monthi

    def get_CaThi(self):
        return self.__cathi
    
    def get_MonThi(self):
        return self.__monthi

    def __str__(self):
        return f'{self.__cathi.get_date()} {self.__cathi.get_time()} {self.__cathi.get_room()} {self.__monthi.get_name()} {self.__group} {self.__amount}'

if __name__ == '__main__':
    file = open('MONTHI.in', 'rt')
    t = int(file.readline().strip())
    lst_MonThi = []
    for _ in range(t):
        lst_MonThi.append(MonThi(file.readline().strip(), file.readline().strip(), file.readline().strip()))
    file.close()

    file = open('CATHI.in', 'rt')
    t = int(file.readline().strip())
    lst_CaThi = []
    for _ in range(t):
        lst_CaThi.append(CaThi(file.readline().strip(), file.readline().strip(), file.readline().strip()))
    file.close()

    file = open('LICHTHI.in', 'rt')
    t = int(file.readline().strip())
    lst_LichThi = []
    for _ in range(t):
        s = file.readline().strip().split()
        lichthi = LichThi(s[0], s[1], s[2], int(s[3]))
        for cathi in lst_CaThi:
            if cathi.get_id() == lichthi.get_id_CaThi():
                lichthi.set_CaThi(cathi)
                break
        
        for monthi in lst_MonThi:
                if monthi.get_id() == lichthi.get_id_MonThi():
                    lichthi.set_MonThi(monthi)
                    break

        lst_LichThi.append(lichthi)
    file.close()
    
    lst_LichThi.sort(key= lambda x : (x.get_CaThi().get_date_to_int(), x.get_CaThi().get_time_to_int(), x.get_CaThi().get_id()))

    print(*lst_LichThi, sep='\n')