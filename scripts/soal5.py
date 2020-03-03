num = 1234
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("angka = ",num)
print("Jumlah dari angka = ", x+x1+x2+x3)