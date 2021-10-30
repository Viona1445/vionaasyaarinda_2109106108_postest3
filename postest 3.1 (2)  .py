#TOKO_BEBEK_LEPAS
#program_kasir

pilihan="ya"
while pilihan=="ya":
    print('''
    ==================================
             BEBEK LEPAS
    Dapat Diskon Jika Membeli Pada Hari:
    senin = 10 %
    jumat = 25 %
    ==================================''')
    def total(harga,jumlah):
        return(harga*jumlah) 
    print ("1. ayam bakar")
    print ("2. ayam geprek")
    print ("3. ayam goreng")
    print ("4. ayam guling")
    menu  = int(input("pilih kode menu yang diinginkan: "))
    if    menu == 1 :
          print("ayam bakar 25000")
          menu = 25000
    elif  menu == 2 :
          print ("ayam geprek 20000")
          menu = 20000
    elif  menu == 3 : 
          print ("ayam goreng 10000")
          menu = 10000
    elif  menu == 4 :
          print ("ayam guling 30000")
          menu == 30000 
    else:
          while True :
             print("===maaf menu tidak ada===")
             menu  = int(input("pilih kode menu yang diinginkan: "))
             if    menu == 1 or menu == 2 or menu == 3 or menu == 4 :
                  if    menu == 1 :
                        print("ayam bakar 25000")
                        menu = 25000
                  elif  menu == 2 :
                        print ("ayam geprek 20000")
                        menu = 20000
                  elif  menu == 3 : 
                        print ("ayam goreng 10000")
                        menu = 10000
                  elif  menu == 4 :
                        print ("ayam guling 30000")
                        menu == 30000 
                  break

    
    Jumlah = int(input("masukan jumlah menu yang dibeli: "))
    Total = menu*Jumlah 
    Hari = input('masukan hari pembelian: ')

    if    Hari == 'senin':
          Total=int(Total-(0.1*Total))
          print('-Diskon 10 %-')
    elif  Hari == 'jumat':
          Total=int(Total-(0.25*Total))
          print('-Diskon 25 %-')
    else:
          print('maaf,tidak dapat diskon')
    
    print("Total Harga = ", "Rp.",Total)
    Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
    Kembalian= (Bayar-Total)
    print("Uang Kembalian = ", "Rp.",Kembalian)
    pilihan=input("Apakah anda ingin Membeli Tambahan Ya/Tidak= ")
pilihan="tidak"
print('Terima Kasih Telah Makan di BEBEK LEPAS')
