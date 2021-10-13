def kalkulator() :
    # Ambil input dan buat variabel bilangan1, operator, dan bilangan2
    bilangan1 = int(input('Bilangan pertama      : '))
    operator  = input('Operator (+, -, *, /) : ')
    bilangan2 = int(input('Bilangan kedua        : '))
    
    # Buat variabel hasil untuk menaruh hasil perhitungan
    hasil     = 0
    
    # print() untuk membuat baris baru di console (untuk merapikan console)
    print()

    # Hitung bilangan1 dan bilangan2 sesuai operator yang dipilih
    if   operator == '+' : hasil = bilangan1 + bilangan2
    elif operator == '-' : hasil = bilangan1 - bilangan2
    elif operator == '*' : hasil = bilangan1 * bilangan2
    elif operator == '/' : hasil = bilangan1 / bilangan2
    else :
        # Jika operator salah, maka ulangi proses perhitungan
        print('Mohon pilih operator yang disediakan')
        kalkulator()
        return

    # Tampilkan hasilnya
    print(f'Hasilnya {bilangan1} {operator} {bilangan2} = {hasil}')
    print('- - - - - - - - - - - - - - - - - - - -')
    
    # Jika ingin mencoba lagi, ulangi proses perhitungan
    if input('Hitung lagi? (Y/n) : ') == 'Y' :
        print()
        print('- - - - - - - - - - - - - - - - - - - -', end='')
        kalkulator()
        return
    
kalkulator()
