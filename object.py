class segitiga:

    def __init__(selfself, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi



    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = segitiga(6, 12)
segitiga2 = segitiga(9, 13)

print('luas segitiga 1 : ', segitiga1.get_luas())
print('luaas segitiga 2 :', segitiga2.get_luas())