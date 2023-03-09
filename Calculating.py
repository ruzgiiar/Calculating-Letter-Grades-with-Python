
print('---')

Name = str(input('Ogrenci Adi: '))
Surname = str(input('Ogrenci Soyadi: '))
Number = int(input('Ogrenci No: '))
Lesson = str(input('Dersin Adi: '))

while len(Number) != 10:
    print('Hata!! 10 Haneli ogrenci numaranizi giriniz.')
    Number = int(input('Ogrenci No: '))    

print('---')

a = int(input('Vize: '))
b = int(input('Final: '))

while  a < 0 or a > 100:
    print('Hata!! Vize degerini 0 ile 100 araliginda giriniz.')
    a = int(input('Vize: '))

while b < 0 or b > 100:
    print('HATA!! Final degerini 0 ile 100 araliginda giriniz.')
    b = int(input('Final: '))

vize = ((a * 40) / 100)
final = ((b * 60) / 100)
harf = vize + final

def donem_notlar(*args, **kwards):
    notlar = 0
    for i in args:
        notlar += i
    print('---')
            
    for k,v in kwards.items():
        print(k, ':', v)
                
    print('---')

    return notlar

print(donem_notlar(vize, final, Ad = Name, Soyad = Surname, No = Number, Ders = Lesson))

if 90 <= harf <= 100:
    print("Harf Notu: AA")
elif 85 <= harf <= 89:
    print("Harf Notu: BA")
elif 80 <= harf <= 84:
    print("Harf Notu: BB")
elif 75 <= harf <= 79:
    print("Harf Notu: CB")
elif 70 <= harf <= 74:
    print("Harf Notu: CC")
elif 65 <= harf <= 69:
    print("Harf Notu: CB")
elif 60 <= harf <= 64:
    print("Harf Notu: DC")
elif 55 <= harf <= 59:
    print("Harf Notu: DD")
elif 50 <= harf <= 54:
    print("Harf Notu: DC")
elif 45 <= harf <= 49:
    print("Harf Notu: DD")
elif 40 <= harf <= 44:
    print("Harf Notu: FD")
elif 0 <= harf <= 39:
    print("Harf Notu: FF")
        



