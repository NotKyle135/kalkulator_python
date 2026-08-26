#Kalkulator v2 pakek 'def'
import math
import operator

operator_map = {'+': operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.truediv
}
def input_int (prompt, min_pilihan, max_pilihan):
    while True:
        nilai = input(prompt)
        if nilai.isdigit():
            nilai = int(nilai)
            if min_pilihan <= nilai <= max_pilihan:
                return nilai
            else:
                print (f"Masukan nilai dari rentang {min_pilihan} - {max_pilihan}!")
        else:
            print("Masukan HANYA angka, bukan huruf!")
def input_float (prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print ("[!] Masukan angka yang BENAR!")

def operasi_dasar ():
    print ("\n --- Operasi Dasar ---")
    try:
        a = input_float("Angka pertama: ")
        work = input("Operator (+, -, *, /): ")
        b = input_float("Angka kedua: ")
        if work not in operator_map:
            print ("Masukan operasi yang benar!")
            return
        if work  == '/' and b == 0.0:
            print ("Tidak bisa dibagi dengan NOL!")
            return
        hasil = operator_map[work](a,b)
        print (f" {a} {work} {b} = {hasil}")
    except Exception as e: 
        print (f"[!] Error {e}")

def trigonometri ():
    print ("\n --- Trigonometri ---")
    menu_tri = {1 : "Sin",
                2 : "Cos",
                3: "Tan",
                4 : "Arcsin",
                5 : "ArcCos",
                6 : "ArcTan"
    }
    for k, v in menu_tri.items():
        print (f"   {k} = {v}")
    pilihan = input_int("Pilihan (1-6): ",1,6)
    pilihan_2 = menu_tri[pilihan]
    if pilihan == 4 or pilihan == 5:
        while True:
            angka = input_float(f"Masukan nilai untuk {pilihan_2} (-1 sampai 1): ")
            if -1 <= angka <= 1:
                break
            else:
                print ("[!] Nilai hanya dari -1 sampai 1!")
        fungsi = {4 : math.asin, 5 : math.acos}
        hasil = math.degrees(fungsi[pilihan](angka))
        print (f"{pilihan_2}({angka}) = {hasil}°")
    else:
        angka = input_float("Masukan derajat: ")
        radian = math.radians(angka)
        fungsi = {1 : math.sin, 2 : math.cos, 3 : math.tan, 6 : math.atan}
        hasil = fungsi[pilihan](radian) if pilihan != 6 else math.degrees(math.atan(radian))
        print (f"    {pilihan_2}({angka}) = {hasil}")
def eksponen():
    menu_eks = {1 : "Akar",
                2 : "Pangkat",
                3 : "Faktorial",
                4 : "Log",
                5 : "Kombinasi",
                6 : "Permutasi"
    }
    print ("\n --- Eksponen ---")
    for k, v in menu_eks.items():
        print (f"   {k} = {v}")
    pilihan = input_int("Pilihan (1-6)", 1, 6)
    try:
        match pilihan:
            case 1:
                a = input_float("Angka: ")
                if a < 0:
                    raise ValueError("Angka tidak boleh negatif!")
                print (f"  √{a} = {math.sqrt(a)}")
            case 2:
                a = input_float("Angka: ")
                b = input_float("Pangkat: ")
                print (f" {a}^{b} = {math.pow(a,b)}")
            case 3:
                a = int(input_float("Angka bulat positif: "))
                if a < 0: 
                    raise ValueError("Angka tidak boleh negatif!")
                print (f"  {a}! = {math.factorial(a)}")
            case 4: 
                a = input_float("Angka (>0): ")
                if a <= 0: 
                    raise ValueError("Angka harus lebih dari nol")
                print (f" Log₁₀({a}) = {math.log10(a)}")
            case 5:
                n = int(input_float("n: "))
                r = int(input_float("r: "))
                if n < 0 or r < 0 or r > n:
                    raise ValueError("Nilai tidak valid untuk kombinasi")
                print (f" C({n}, {r}) = {math.comb(n, r)}")
            case 6:
                n = int(input_float("n: "))
                r = int(input_float("r: "))
                if n < 0 or r < 0 or r > n:
                    raise ValueError("Nilai tidak valid untuk permutasi")
                print (f" P({n}, {r}) = {math.perm(n, r)}")
    except (ValueError, OverflowError) as e:
        print(f"[!] {e}")
def main():
    print ("==================================")
    print (" Kaltulator Scientific V2 by Kyle")
    print ("==================================")
    while True:
        print ("\nPilih jenis operasi:")
        print ("1. Operasi Dasar")
        print ("2. Trigonometri")
        print ("3. Eksponen")
        print ("4. Keluar")
        pilihan = input_int("Pilihan (1-4): ", 1, 4)
        if pilihan == 1:
            operasi_dasar()
        elif pilihan == 2:
            trigonometri()
        elif pilihan == 3:
            eksponen()
        else:
            print("Terima kasih telah menggunakan Kaltulator Scientific V2!")
            break

        
if __name__ == "__main__": # agar bisa diimport tanpa langsung menjalankan main()
    main()