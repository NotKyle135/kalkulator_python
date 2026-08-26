#Kalkulator Scientific by Kyle :P
import math
while True:
    print ("================================")
    print ("  KALKULATOR SCIENTIFIC PYTHON")
    print ("================================")
    print ("Pilih Operasinya!")
    print ("1 = Operasi Dasar (+, -, /, *)")
    print ("2 = Trigonometri  (sin, cos, tan)")
    print ("3 = Eksponen      (akar, faktorial, log , pangkat, etc)")
    print ("---------------------------------------------------")

    while True:
        pilihan = input("Masukan pilihan kamu(1-3)!\t")
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if 1 <= pilihan <= 3:
                break
            else:
                print("Masukan angka 1-3!")
        else:
            print("Masukan angka, jangan huruf!")
    match pilihan:
        case 1:#Operasi Dasar
            rumus = input("Masukan Operasinya\t")
            try:
                hasil = eval(rumus)#eval untuk operasi int di python
                print (f"Hasil dari {rumus} adalah {hasil}")
            except ZeroDivisionError:
                print("[!] Tidak bisa dibagi dengan 0!")
            except SyntaxError:
                print("[!] Penulisan angka tidak benar(Syntax Error)")
            except NameError:
                print("[!] Masukan HANYA angka, jangan huruf!")
            except Exception as e:
                print(f"[!] Error {e}")
        case 2:#Trigonometri
            print ("==============")
            print ("Pilih Operasi!")
            print ("1 = Sin")
            print ("2 = Cos")
            print ("3 = Tan")
            print ("==============")
            while True:
                tri = input("Masukan pilihan mu(1-3)!\t")
                if tri.isdigit():
                    tri = int(tri)
                    if 1 <= tri <= 3:
                        break
                    else:
                        print("Masukan angka dari 1-3!")
                else:
                    print("Masukan angka!")
            while True:
                try:
                    angka_derajat = float(input("Masukan berapa derajat!\t"))
                    radian = math.radians(angka_derajat)#biar berubah jadi radian
                    match tri:
                        case 1:
                            print(f"Hasil dari sin({angka_derajat}) adalah {math.sin(radian)}")
                            break
                        case 2:
                            print(f"Hasil dari cos({angka_derajat}) adalah {math.cos(radian)}")
                            break
                        case 3:
                            print(f"Hasil dari tan({angka_derajat}) adalah {math.tan(radian)}")
                            break
                except ValueError:
                    print("[!] Masukan angka yang benar!")
        case 3:#Eksponen
            print("==================")
            print("Pilih Operasi!")
            print(" 1 = Akar\n 2 = Pangkat\n 3 = Faktorial\n 4 = Log\n 5 = Kombinasi\n 6 = Permutasi")
            print("==================")
            while True:
                eks = input("Masukan pilihan kamu(1-6)!\t")
                if eks.isdigit():
                    eks = int(eks)
                    if 1 <= eks <= 6:
                        break
                    else:
                        print("Masukan angka dari 1-6!")
                else:
                    print("Masukan HANYA angka, bukan huruf!")
            try:
                while True:
                    if eks == 1:
                        angka = float(input("Masukan angka yang ingin diakarkan!\t"))
                        if angka < 0:
                            print("Angka tidak boleh negatif!")
                        else:
                            print(f"Hasil dari akar({angka}) adalah {math.sqrt(angka)}")
                            break
                    elif eks == 2:
                        angka = float(input("Masukan angka yang ingin dipangkatkan\t"))
                        pangkat =  float(input("Masukan pangkat berapa!\t"))
                        hasil_1 = math.pow(angka, pangkat)
                        print (f"Hasil dari {angka}^{pangkat} adalah {hasil_1}")
                        break
                    elif eks == 3:
                        angka = int(input("Masukan nilai bulat positif!\t"))
                        print(f"Hasil dari faktorial {angka} adalah {math.factorial(angka)}")
                        break
                    elif eks == 4:
                        angka = float(input("Masukan untuk Log10!\t"))
                        if angka == 0:
                            print("Angka tidak boleh 0")
                        else:
                            print(f"Hasil dari Log10{angka} adalah {math.log10(angka)}")
                            break
                    elif eks == 5:
                        n = int(input("Masukan nilai n!\t"))
                        r = int(input("Masukan nilai r!\t"))
                        if n >= r >= 0:
                            print(f"Hasil dari kombinasi({n}, {r}) adalah {math.comb(n,r)}")
                            break
                        else:
                            print("[!] n harus >= r dan tidak boleh negatif!")
                    elif eks == 6:
                        n = int(input("Masukan nilai n!\t"))
                        r = int(input("Masukan nilai r!\t"))
                        if n >= r >= 0:
                            print(f"Hasil dari permutasi({n}, {r}) adalah {math.perm(n,r)}")
                            break
                        else:
                            print("[!] n harus >= r dan tidak boleh negatif!")
            except ValueError:
                print("[!] Input tidak valid")
            except OverflowError:
                print("[!] OverFlowError")
    lagi = input("Ulangi?(y/n)")
    if lagi == 'n':
        print("Terima kasih")
        break