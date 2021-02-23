#Painem ingin menikah tahun ini dan telah memiliki 3 calon potensial suami 
#Ketiga calon tersebut adalah Paijo,Paino dan Sukinem
"Kriteria utama calon suami idaman Painem adalah tinggi > 175 cm,berat <=70kg, dan mempunyai brewok "
#Kriteria utama merupakan syarat utama untuk dipenuhi agar Painem mau menerima calon suaminya
#Painem hanya ingin menikah dengan salah satu dari ketiga orang tersebut 
#Bantu Painem untuk menentukan calon suaminya dengan membuat program untuk memudahkan survey kepada calon-calon suaminya

nama = str(input("Siapakah nama anda ? :"))
nama_up = nama.upper()

if nama_up == "PAIJO" or nama_up == "PAINO" or nama_up == "SUKINEM" : 
    tinggi = float(input("Berapakah tinggi badan anda ? (dalam cm) : "))
    if tinggi > 175 :
        berat = float(input("Berapakah berat badan anda ? (dalam kg) :"))
        if berat <= 70 :
            brewok = str(input("Apakah anda memiliki brewok ? (Ya/Tidak) : "))
            brewok_up = brewok.upper()
            if brewok_up == "YA" :
                print("Lek kawini aku masss")
            elif brewok_up == "TIDAK" :
                print("Wah mas,aku senenge sing brewoken e")
            elif brewok_up != str() :
                print("Kata-kata mas sing di ketik !")
            else :
                print("Jawabane Ya/Tidak mas ojo sing liyo")
        elif berat > 70 : 
            print("Abot temen e mas")
        else :
            print("Masukke angka mas,hudu sing liane")

    elif tinggi <= 175 :
        print("Kurang duwur mas,sorry")
    else :
        print("Masukke angka mas,hudu sing liane")

else : 
    print("SOPO KOE ???")
