#cinsiyet ve boya göre mülakatı geçme programı
#pilotluk sınavından geçebilmek için kadınların boyu 1.60 tan erkeklerin boyu 1.70 ten uzun olması gerekmektedir.
while True:
    x=str(input("lütfen cinsiyetinizi giriniz: ")) #str olarak belirtmesek de olur.
    print(x)
    y=int(input("lütfen boyunuzu giriniz: "))
    print(y)
    if x=="kadın"and y>=160:
        print("tebrikler mülakatı geçtiniz!")
    elif x=="erkek" and y>=170:
        print("tebrikler mülakatı geçtiniz!")
    else:
        print("üzgünüm kaldınız...")
#kısa hali...
while True:
    x=str(input("lütfen cinsiyetinizi giriniz: ")) #str olarak belirtmesek de olur.
    print(x)
    y=int(input("lütfen boyunuzu giriniz: "))
    print(y)
    if ((x=="kadın"and y>=160) or (x=="erkek" and y>=170)):
        print("tebrikler mülakatı geçtiniz!")
    else:
        print("üzgünüm kaldınız...")

    