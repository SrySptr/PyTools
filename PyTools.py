from pyfiglet import Figlet
import time
import os
import calendar
import datetime
from datetime import date
from datetime import datetime
from gtts import gTTS
from termcolor import colored
import random
from random import randint
import qrcode
import string


def kejawen():
    def weton():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("════════════════════════════════════════════════")
        print("❚█══════════════ TOOLS CEK WETON ══════════════█❚")
        print("════════════════════════════════════════════════")
        d1 = date(1900, 1, 1)
        def hitung():
            hari = [
                'Senin',
                'Selasa',
                'Rabu',
                'Kamis',
                'Jumat',
                'Sabtu',
                'Minggu'
            ]
    
            pasaran = [
                'Pahing',
                'Pon',
                'Wage',
                'Kliwon',
                'Legi'
            ]
    
            neptuhari = [
                "4", 
                "3", 
                "7", 
                "8", 
                "6", 
                "9", 
                "5"
            ]
    
            neptuweton = [
                "9", 
                "7", 
                "4", 
                "8", 
                "5"
            ]

            tgl = int(input("Masukkan Tanggal Lahir : "))
            bln = int(input("Masukkan Bulan Lahir   : "))
            thn = int(input("Masukkan Tahun Lahir   : "))
            d0 = date(thn,bln,tgl)
            beda = d0 - d1
            harike = (beda.days) % 7
            pasaranke = (beda.days) % 5
            hitunghari = neptuhari[harike] 
            hitungweton = neptuweton[pasaranke]
            neptu = int(hitunghari) + int(hitungweton)
            print("════════════════════════════════════════════════")
            print("Weton :", hari[harike], pasaran[pasaranke])
            print(hari[harike], ":", hitunghari)
            print(pasaran[pasaranke], ":", hitungweton)
            print("Neptu :", neptu)
            print("════════════════════════════════════════════════")
            if hari[harike] == 'Minggu' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Lintang (Lebu Katiyup Angin)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Lintang : Lemah hati, kesepian dan sengsara, 
kecenderungan tidak menetap (dalam hal pekerjaan, tempat tinggal, dan lain-lain)"""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Lebu Katiyup Angin: Serba kekurangan hidupnya, jauh 
dari keberuntungan, dan sulit mendapat kemajuan dalam pekerjaan dan usahanya. 
Sarana penolaknya adalah dengan menyebar debu."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang angkuh dan suka
membanggakan diri sendiri, serta mudah tersinggung. 
Apabila sedang bertengkar inginnya menang sendiri, 
tetapi orang dengan weton ini pandai untuk menyimpan rahasia 
( dapat dipercaya ) dan seseorang yang hemat."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                    
            if hari[harike] == 'Minggu' and pasaran[pasaranke] == 'Legi':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Pepet (Sumur Sinaba)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Pepet atau Lakuning Pandhita Sakti, sifatnya 
tertutup atau pertapa sakti: Sering prihatin, hidup menderita dan serba 
kekurangan, yang diinginkan sulit tercapai"""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Sumur Sinaba: Dicari orang karena petuah dan nasehatanya, serta banyak pengetahuannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki hati yang keras, Jika ia seorang wanita, 
maka ia berani terhadap suami, suka membuka aib/rahasia orang lain. 
Namun ia sangat jujur di dalam mengemban amanat, tidak mudah terpengaruh 
rayuan orang lain dan pandai menyimpan rahasia rumah tangganya sendiri."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Minggu' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Rembulan (Wasesa Segara)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Rembulan, sifatnya bulan: Simpatik, penuh daya tarik, serba menyenangkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah sekali tersinggung dan mudah bimbang. 
Apabila ia seorang wanita, maka ia tidak taat terhadap suami namun mempunyai 
rasa cemburu yang sangat besar. Bukan tipe orang yang suka menghambur-hamburkan uang, 
tidak boros dan mengerti tanggung jawab."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Minggu' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Kembang (Bumi Kapetak)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Kembang, sifatnya bunga: Memesona memikat lawan jenisnya."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Bumi Kapetak: Suka bekerja, kuat menahan kecewa dan penderitaan, 
rapi dan bersih hidupnya namun pendendam. Sarana penolaknya 
adalah menanam atau mengubur tanah."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat keras hati, pemberani namun sangat mudah tersinggung. 
Tapi ia pandai mengemban amanat, orang yang gemar menolong, sangat menaruh belas kasihan 
terhadap orang yang sedang kena musibah, terutama terhadap fakir miskin."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Minggu' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Angin (Satriya Wibawa)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Angin, sifatnya angin: Pandai mengambil hati orang, tetapi menakutkan jika sedang marah."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wibawa: Dihormati orang karena kemuliaan dan keluhurannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya mempunyai sifat tidak bisa menyimpanrahasi, pemboros, 
keras hati dan suka bertengkar. Tetapi ia sangat cerdik, pandai mencari 
rizki dan suka memaafkan kesalahan orang lain."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Senin' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Kembang (Satria Wirang)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Kembang, sifatnya bunga: Memesona memikat lawan jenisnya."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wirang: Luhur budinya tetapi selalu dipermalukan orang, tidak berwibawa. 
Sarana penolaknya adalah mengeluarkan darah (menyembelih ayam atau kambing)."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat cemburuan, suka kalau dipuji. Apabila ia 
seorang wanita maka ia berani terhadap suaminya, boros dan suka bepergian ( travelling ) 
dan kurang mengerti tanggung jawab. Namun ia mempunyai sifat suka menolong 
terhadap orang yang sedang kena musibah."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Senin' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Lintang (Lebu Katiyup Angin)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Lintang : Lemah hati, kesepian dan sengsara, 
kecenderungan tidak menetap (dalam hal pekerjaan, tempat tinggal, dan lain-lain)"""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Lebu Katiyup Angin: Serba kekurangan hidupnya, jauh 
dari keberuntungan, dan sulit mendapat kemajuan dalam pekerjaan dan usahanya. 
Sarana penolaknya adalah dengan menyebar debu."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat keras hati, tidak suka menerima nasihat 
dari orang lain dan tidak mudah putus asa. Tapi ia juga dipercaya memiliki 
daya ingat yang sangat baik, serta suka memaafkan kesalahan orang lain yang mengaku bersalah."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Senin' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Tuding (Sumur Sinaba)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Tuding, sifatnya telunjuk jari: Sering ditunjuk dalam hal apa pun."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Sumur Sinaba: Dicari orang karena petuah dan nasehatanya, serta banyak pengetahuannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat mudah tersinggung. Apabila sedang bertengkar, 
ia tidak mau mengalah dan tidak bisa menjaga rahasia. Apabila ia seorang wanita, 
maka ia sangat setia terhadap suaminya, tidak pernah ingkar janji, serta dipercaya pandai berhemat."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Senin' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Bumi (Lebu Katiyup Angin)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Bumi, sifatnya bumi: Pemurah, pengampun, dan pelindung."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Lebu Katiyup Angin: Serba kekurangan hidupnya, jauh dari keberuntungan, 
dan sulit mendapat kemajuan dalam pekerjaan dan usahanya. Sarana penolaknya 
adalah dengan menyebar debu."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat egois dan tidak mau menerima nasihat dari orang lain. 
Boros dan tidak pandai menyimpan rahasia, namun ia memiliki pendirian yang kuat dan 
suka mengalah jika bertengkar."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Selasa' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Tuding (Sumur Sinaba)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Tuding, sifatnya telunjuk jari: Sering ditunjuk dalam hal apa pun."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Sumur Sinaba: Dicari orang karena petuah dan nasehatanya, serta banyak pengetahuannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang suka membanggakan diri sendiri, banyak bicara 
dan mudah sekali tersinggung. Namun berhati ramah, dapat memikat hati orang lain, 
serta dapat mengemban amanah dan bisa dipercaya."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Selasa' and pasaran[pasaranke] == 'Legi':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Geni (Wasesa Segara).")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Geni, sifatnya api: Temperamental, emosional, mudah marah dan naik pitam, pemberani."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang sering kali berbuat kesalahan. Apabila ia 
seorang wanita, maka ia berani terhadap suami, ceroboh. Tapi ia memiliki pendirian 
yang teguh, tidak mudah bimbang, hemat serta mudah sadar bila menerima nasehat."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Selasa' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Kembang (Satria Wirang)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Kembang, sifatnya bunga: Memesona memikat lawan jenisnya."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wirang: Luhur budinya tetapi selalu dipermalukan orang, tidak berwibawa. 
Sarana penolaknya adalah mengeluarkan darah (menyembelih ayam atau kambing)."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang suka disanjung. Apabila ia seorang wanita 
maka ia cemburuan dan kurang bisa setia terhadap sang suami, pemboros, tapi berhati 
ramah serta daya ingatnya tangguh dan teguh pendiriannya."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Selasa' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Pepet (Satriya Wibawa)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Pepet atau Lakuning Pandhita Sakti, sifatnya tertutup 
atau pertapa sakti: Sering prihatin, hidup menderita dan serba kekurangan, 
yang diinginkan sulit tercapai."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wibawa: Dihormati orang karena kemuliaan dan keluhurannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat berhati keras, sangat mudah tersinggung, bila bertengkar 
tidak mau mengalah. Apabila ia seorang wanita, terkadang ia berani terhadap suami, 
tetapi ia sangat menaruh belas kasihan terhadap orang yang sedang kena musibah, sangat 
jujur, terus terang serta pandai menyimpan rahasia."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Selasa' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Geni (Wasesa Segara)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Geni, sifatnya api: Temperamental, emosional, mudah marah dan naik pitam, pemberani."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya mempunyai sifat bila ia wanita sangat mudah cemburu, suka dipuji, 
berhati keras, namun ia sangat menaruh perhatian terhadap orang yang kena musibah."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Rabu' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Srengenge (Lebu Katiyup Angin)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Srengenge, sifatnya matahari: Terang dan berwibawa, mencerahkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Lebu Katiyup Angin: Serba kekurangan hidupnya, jauh dari keberuntungan, 
dan sulit mendapat kemajuan dalam pekerjaan dan usahanya. Sarana penolaknya 
adalah dengan menyebar debu."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah bimbang, berhati keras dan mudah lupa. 
Tapi bila ia seorang wanita, maka sangat setia terhadap pasangan atau suami, penghemat, 
suka menerima nasihat dari orang lain dan mudah bergaul."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Rabu' and pasaran[pasaranke] == 'Legi':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Kembang (Sumur Sinaba)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Kembang, sifatnya bunga: Memesona memikat lawan jenisnya."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Sumur Sinaba: Dicari orang karena petuah dan nasehatanya, serta banyak pengetahuannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat keras hati, sangat mudah tersinggung, tidak 
pintar menyimpan rahasia dan sangat suka disanjung. Tapi berhati baik, suka 
menolong terhadap sesama, dan juga banyak menaruh welas kasihan."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Rabu' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Banyu (Wasesa Segara)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Banyu, sifatnya air: Tenang, selalu mengalir ke tempat yang 
rendah karena tahu persis di mana akan mendapatkan rezekinya, memiliki 
perencanaan yang matang."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat pemboros, sangat mudah tersinggung, mudah marah, 
tetapi banyak menaruh belas kasihan terhadap sesama. Serta sangat mudah menerima dan 
suka memberi serta tahan menerima cobaan."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Rabu' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Rembulan (Bumi Kapetak)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Rembulan, sifatnya bulan: Simpatik, penuh daya tarik, serba menyenangkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Bumi Kapetak: Suka bekerja, kuat menahan kecewa dan penderitaan, rapi dan 
bersih hidupnya namun pendendam. Sarana penolaknya adalah menanam atau mengubur tanah."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah tersinggung, bila ia seorang wanita, banyak 
cemburunya dan tidak pintar menyimpan rahasia.Tetapi suka menerima nasihat orang lain, 
berpendirian teguh serta sangat memikirkan nasib orang lain, terutama bagi orang yang sedang kena musibah."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Rabu' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Banyu (Wasesa Segara)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Banyu, sifatnya air: Tenang, selalu mengalir ke tempat 
yang rendah karena tahu persis di mana akan mendapatkan rezekinya, 
memiliki perencanaan yang matang."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah tersinggung, berhati keras dan tidak pintar 
menyimpan rahasia. Tetapi ia memiliki sifat yang ramah terhadap sesama, pandai bergaul dan 
suka menolong orang yang sedang kesusahan."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Kamis' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Banyu (Bumi Kapetak)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Banyu, sifatnya air: Tenang, selalu mengalir ke tempat 
yang rendah karena tahu persis di mana akan mendapatkan rezekinya, 
memiliki perencanaan yang matang."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Bumi Kapetak: Suka bekerja, kuat menahan kecewa dan penderitaan, 
rapi dan bersih hidupnya namun pendendam. Sarana penolaknya adalah 
menanam atau mengubur tanah."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat sombong, suka pamer dan suka membanggakan diri sendiri. 
Tetapi ia memiliki daya ingat yang sangat kuat serta bercita cita tinggi dan mudah 
menaruh belas kasihan terhadap orang lain yang sedang kesusahan."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Kamis' and pasaran[pasaranke] == 'Legi':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Lintang (Satriya Wibawa)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Lintang, sifatnya bintang: Lemah hati, kesepian dan sengsara, 
kecenderungan tidak menetap (dalam hal pekerjaan, tempat tinggal, dan lain-lain)."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wibawa: Dihormati orang karena kemuliaan dan keluhurannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat banyak bicara dan mudah tersinggung. 
Segala sesuatunya menurut kemauan diri sendiri, namun ia bersifat ramah, pandai 
bergaul serta memiliki pendirian yang teguh."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Kamis' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Bumi (Lebu Katiyup Angin)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Bumi, sifatnya bumi: Pemurah, pengampun, dan pelindung."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Lebu Katiyup Angin: Serba kekurangan hidupnya, jauh dari keberuntungan, 
dan sulit mendapat kemajuan dalam pekerjaan dan usahanya. Sarana penolaknya 
adalah dengan menyebar debu."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat berhati keras, mudah marah dan mudah tersinggung. 
Suka menolong orang lain, pandai  menyimpan rahasia, tidak mudah bimbang 
dan berpendirian teguh."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Kamis' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Srengenge (Satria Wirang)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Srengenge, sifatnya matahari: Terang dan berwibawa, mencerahkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wirang: Luhur budinya tetapi selalu dipermalukan orang, tidak berwibawa. 
Sarana penolaknya adalah mengeluarkan darah (menyembelih ayam atau kambing)."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang sangat suka disanjung, mudah tersinggung, serta 
suka berfoya foya. Namun ia juga termasuk orang yang ramah, memiliki sifat penyabar 
dan memiliki pendirian yang teguh serta suka mengalah dalam segala sesuatu."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Kamis' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Kembang (Tunggak Semi)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Kembang, sifatnya bunga: Memesona memikat lawan jenisnya."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Tunggak Semi: Penghasilannya selalu terjamin, rezeki selalu ada."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang suka berbuat hal tidak baik, pendendam, sangat mudah 
tersinggung dan berhati keras. Namun ia pandai mengambil hati orang lain, Pandai bergaul 
dan sangat hemat serta memiliki pendirian yang teguh."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Jumat' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Rembulan (Wasesa Segara)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Rembulan, sifatnya bulan: Simpatik, penuh daya tarik, serba menyenangkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Apabila ia wanita maka ia banyak cemburuannya, kehendaknya susah untuk dirubah, 
tidak pandai menyimpan rahasia, tetapi berhati mulia, pemaaf, suka menerima dan suka 
memberi serta memiliki daya ingat yang kuat."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Jumat' and pasaran[pasaranke] == 'Legi':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Tuding (Satriya Wirang)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Tuding, sifatnya telunjuk jari: Sering ditunjuk dalam hal apa pun."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wirang: Luhur budinya tetapi selalu dipermalukan orang, tidak berwibawa. 
Sarana penolaknya adalah mengeluarkan darah (menyembelih ayam atau kambing)."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat keras hati, sangat mudah tersinggung, suka dipuji serta kadang kala 
mudah putus asa. Tetapi ia suka memberi pertolongan terhadap orang lain yang kesusahan, dan 
sangat tabah dalam menghadapi cobaan."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Jumat' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Srengenge (Tunggak Semi)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Srengenge, sifatnya matahari: Terang dan berwibawa, mencerahkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Tunggak Semi: Penghasilannya selalu terjamin, rezeki selalu ada."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah menerima hasutan, banyak bicara, berhati keras. 
Namun ia menaruh belas kasihan terhadap orang yang sedang terkena musibah, sangat bijaksana, 
serta memiliki pendirian yang kuat."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Jumat' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Lintang (Lebu Katiyup Angin)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Lintang, sifatnya bintang: Lemah hati, kesepian dan sengsara, 
kecenderungan tidak menetap (dalam hal pekerjaan, tempat tinggal, dan lain-lain)."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Lebu Katiyup Angin: Serba kekurangan hidupnya, jauh dari keberuntungan, 
dan sulit mendapat kemajuan dalam pekerjaan dan usahanya. Sarana penolaknya 
adalah dengan menyebar debu."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat kurang pandai menyimpan rahasia, berhati keras, suka 
disanjung dan sangat mudah putus asa. Tetapi ia penyabar, tahan menerima cobaan, 
tidak suka mementingkan kepentingan sendiri serta teguh pendirian."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Jumat' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Aras Pepet (Sumur Sinaba)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Aras Pepet atau Lakuning Pandhita Sakti, sifatnya tertutup atau 
pertapa sakti: Sering prihatin, hidup menderita dan serba kekurangan, 
yang diinginkan sulit tercapai."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Sumur Sinaba: Dicari orang karena petuah dan nasehatanya, serta banyak pengetahuannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat mudah tersinggung, mudah bimbang, mudah putus asa, serta 
tidak pintar menyimpan rahasia. Tetapi ia juga memiliki sifat pandai bersyukur, 
berhati mulia, mau menerima nasihat orang lain, dan berpendirian teguh."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Sabtu' and pasaran[pasaranke] == 'Kliwon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Bumi (Tunggak Semi)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Bumi, sifatnya bumi: Pemurah, pengampun, dan pelindung."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Tunggak Semi: Penghasilannya selalu terjamin, rezeki selalu ada."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang keras hati, bila ia seorang wanita, maka sangat berani 
terhadap suami, pemboros dan susah diatur. Namun ia juga memiliki sifat belas kasihan 
terhadap sesama. Pemaaf dan memiliki pendirian yang teguh."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Sabtu' and pasaran[pasaranke] == 'Legi':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Rembulan (Bumi Kapetak)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Rembulan, sifatnya bulan: Simpatik, penuh daya tarik, serba menyenangkan."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Bumi Kapetak: Suka bekerja, kuat menahan kecewa dan penderitaan, rapi dan bersih 
hidupnya namun pendendam. Sarana penolaknya adalah menanam atau mengubur tanah."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah tersinggung, suka dipuji, berhati 
keras dan egois. Namun ia juga memiliki sifat pandai menyimpan rahasia, pandai 
bergaul dan pandai memikat hati orang lain."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Sabtu' and pasaran[pasaranke] == 'Pahing':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Geni (Satriya Wibawa)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Geni, sifatnya api: Temperamental, emosional, mudah marah dan naik pitam, pemberani."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wibawa: Dihormati orang karena kemuliaan dan keluhurannya."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah tersinggung, suka dipuji dan suka berfoya foya. 
Namun ia pandai bergaul, banyak memberi pertolongan terhadap orang lain dan memiliki 
daya ingat yang kuat."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Sabtu' and pasaran[pasaranke] == 'Pon':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Banyu (Wasesa Segara)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Banyu, sifatnya air: Tenang, selalu mengalir ke tempat 
yang rendah karena tahu persis di mana akan mendapatkan rezekinya, memiliki 
perencanaan yang matang."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Wasesa Segara: Pemurah, pemaaf, berwibawa, dan bertanggung jawab."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat yang mudah tersinggung, suka berfoya foya, berhati keras. 
Namun suka menerima nasehat dari orang lain, suka menolong, memiliki daya pikir 
yang cerdas serta tahan menerima cobaan."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)

            if hari[harike] == 'Sabtu' and pasaran[pasaranke] == 'Wage':
                print()
                print(">>>>> Karakter Dasar <<<<<")
                print("Lakuning Lintang (Satriya Wirang)")
                print()
                print(">>>>> Pangasaran <<<<<")
                pangasaran = """Lakuning Lintang, sifatnya bintang: Lemah hati, kesepian dan sengsara, 
kecenderungan tidak menetap (dalam hal pekerjaan, tempat tinggal, dan lain-lain)."""
                for i in pangasaran:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Pancasuda <<<<<")
                pancasuda = """Satriya Wirang: Luhur budinya tetapi selalu dipermalukan orang, tidak berwibawa. 
Sarana penolaknya adalah mengeluarkan darah (menyembelih ayam atau kambing)."""
                for i in pancasuda:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                print()
                print()
                print(">>>>> Sifat/Watak Berdasarkan Weton <<<<<")
                arti = """Dipercaya memiliki sifat suka menuruti kemauan sendiri, suka kalau dipuji, 
dan bila ia seorang wanita, maka ia berani terhadap suami, serta bersifat serakah, 
tetapi ia pandai bergaul, rendah  hati, suka menerima nasehat dan pandai menyimpan rahasia."""
                for i in arti:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
            print()
            print()
            print("════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            kejawen()
            pass

        if __name__ == '__main__':
            hitung()

    def jodoh():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        def pegat():
            arti = """Hasil perhitungan neptu pegat artinya hubungan kamu dan pasanganmu masuk kategori rawan.
Pegat menurut primbon Jawa jodoh mengindikasikan adanya kemungkinan kamu dan pasanganmu 
sering mendapat masalah dalam kehidupan."""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def ratu():
            arti = """Kategori ratu menafsirkan kamu dan pasanganmu sebagai jodoh sejati.
Kamu akan memiliki hubungan yang sangat harmonis, bahagia, dan bahkan membuat iri banyak orang di sekelilingmu!"""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def jongdoh():
            arti = """Kategori weton jodoh ini dalam primbon Jawa memiliki arti bahwa kamu dan pasanganmu berjodoh.
Lebih dari itu, kamu dan pasanganmu dapat memiliki kehidupan rumah tangga yang selalu rukun setiap waktu."""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def topo():
            arti = """Jika angka yang keluar masuk dalam kategori topo, kamu perlu ekstra waspada.
Pasalnya, primbon jodoh jawa meramalkan kamu dan pasanganmu akan mendapatkan kesulitan di awal berumah tangga."""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def tinari():
            arti = """Hasil perhitungan weton tinari ini termasuk kabar bahagia.
Kebahagiaan tersebut hadir dalam wujud kecukupan rezeki dalam kehidupan rumah tangga kelak.
Bahkan, kamu sekeluarga akan diberi kemudahan dalam mencari rezeki."""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def padu():
            arti = """Weton jodoh padu ini mengindikasikan ramalan yang buruk bagi kehidupan rumah tangga kamu dan pasangan.
Kendati demikian, hal ini tidak akan berujung pada perceraian. Syukurlah!"""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def sunajan():
            arti = """Menurut primbon jawa jodoh, mereka yang berada di kategori ini berada dalam 
ancaman pertengkaran besar dalam rumah tangga akibat perselingkuhan."""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        def pesthi():
            arti = """Berdasarkan perhitungan weton jodoh, mereka yang berada dalam kategori pesthi konon akan memiliki rumah tangga yang rukun.
Kamu dan pasanganmu disebut akan memiliki kehidupan keluarga yang bahagia, rukun, dan harmonis."""
            for i in arti:
                print(i, end="", flush=True)
                time.sleep(0.03)

        print("══════════════════════════════════════════════════════")
        print("❚█══════════════ TOOLS CEK WETON JODOH ══════════════█❚")
        print("══════════════════════════════════════════════════════")
        kamu = input("Masukkan Jumlah Neptu Kamu          : ")
        pasangan = input("Masukkan Jumlah Neptu Pasangan Kamu : ")
        hasil = int(kamu) + int(pasangan)
        print("══════════════════════════════════════════════════════")
        print("Hasil :", hasil)
        print()
        if hasil == 1 or hasil == 9 or hasil == 10 or hasil == 18 or hasil == 19 or hasil == 27 or hasil == 28 or hasil == 3:
            print(">>>>> Nama Weton <<<")
            print("Pegat")
            print()
            print(">>>>> Arti Weton <<<<<")
            pegat()
        if hasil == 2 or hasil == 11 or hasil == 20 or hasil == 29:
            print(">>>>> Nama Weton <<<")
            print("Ratu")
            print()
            print(">>>>> Arti Weton <<<<<")
            ratu()
        if hasil == 3 or hasil == 12 or hasil == 21 or hasil == 30:
            print(">>>>> Nama Weton <<<")
            print("Jodoh")
            print()
            print(">>>>> Arti Weton <<<<<")
            jongdoh()
        if hasil == 4 or hasil == 13 or hasil == 22 or hasil == 31:
            print(">>>>> Nama Weton <<<")
            print("Topo")
            print()
            print(">>>>> Arti Weton <<<<<")
            topo()
        if hasil == 5 or hasil == 14 or hasil == 23 or hasil == 32:
            print(">>>>> Nama Weton <<<")
            print("Tinari")
            print()
            print(">>>>> Arti Weton <<<<<")
            tinari()
        if hasil == 6 or hasil == 15 or hasil == 24 or hasil == 33:
            print(">>>>> Nama Weton <<<")
            print("Padu")
            print()
            print(">>>>> Arti Weton <<<<<")
            padu()
        if hasil == 7 or hasil == 16 or hasil == 25 or hasil == 34:
            print(">>>>> Nama Weton <<<")
            print("Sunajan")
            print()
            print(">>>>> Arti Weton <<<<<")
            sunajan()
        if hasil == 8 or hasil == 17 or hasil == 26 or hasil == 35:
            print(">>>>> Nama Weton <<<")
            print("Pesthi")
            print()
            print(">>>>> Arti Weton <<<<<")
            pesthi()
        print()
        print()
        print("══════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        kejawen()
    
    def togel():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("══════════════════════════════════════════════════")
        print("❚█══════════════ TOOLS RAMAL TOGEL ══════════════█❚")
        print("══════════════════════════════════════════════════")
        print("1. TOGEL 2 ANGKA")
        print("2. TOGEL 3 ANGKA")
        print("3. TOGEL 4 ANGKA")
        print("4. KELUAR")
        print("══════════════════════════════════════════════════")
        pilih = int(input("Masukkan Pilihan Anda : "))
        print("══════════════════════════════════════════════════")
        if pilih == 1:
            nomor = "1234567890"
            togel = ""
            for i in range(3):
                time.sleep(0.1)
            tunggu = """Mohon Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(0.1)
            siluman = [
                'Siluman Kucing Garong', 
                'Siluman Pocong Gundul', 
                'Siluman Pocong Gondrong',
                'Siluman Banaspati',
                'Siluman Kera',
                'Siluman Babi Ngepet',
                'Siluman Ikan Cupang',
                'Siluman Burung Bangau',
                'Siluman Kuntilanak Ungu',
                'Siluman Tuyul Mullet',
                'Siluman Suster Koprol',
                'Siluman Serigala Berbulu Ayam',
                'Siluman Ular Anaconda',
                'Siluman Kuda Poni'
                ]
            demit = random.choice(siluman)
            jin = f"""{demit} Yang Sakti Sedang Meramalkan Nomor Togel Jitu....."""
            for i in jin:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            print()
            for i in range(3):
                time.sleep(0.1)
            print("Nomor Togel Berhasil Di Dapatkan!")
            for index in range(2):
                togel = togel + random.choice(nomor)
            for i in range(3):
                time.sleep(0.1)
            print("Nomor Togel :", togel)
        if pilih == 2:
            nomor = "1234567890"
            togel = ""
            for i in range(3):
                time.sleep(0.1)
            tunggu = """Mohon Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(0.1)
            siluman = [
                'Siluman Kucing Garong', 
                'Siluman Pocong Gundul', 
                'Siluman Pocong Gondrong',
                'Siluman Banaspati',
                'Siluman Kera',
                'Siluman Babi Ngepet',
                'Siluman Ikan Cupang',
                'Siluman Burung Bangau',
                'Siluman Kuntilanak Ungu',
                'Siluman Tuyul Mullet',
                'Siluman Suster Koprol',
                'Siluman Serigala Berbulu Ayam',
                'Siluman Ular Anaconda',
                'Siluman Kuda Poni'
                ]
            demit = random.choice(siluman)
            jin = f"""{demit} Yang Sakti Sedang Meramalkan Nomor Togel Jitu....."""
            for i in jin:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            print()
            for i in range(3):
                time.sleep(0.1)
            print("Nomor Togel Berhasil Di Dapatkan!")
            for index in range(3):
                togel = togel + random.choice(nomor)
            for i in range(3):
                time.sleep(0.1)
            print("Nomor Togel :", togel)
        if pilih == 3:
            nomor = "1234567890"
            togel = ""
            for i in range(3):
                time.sleep(0.1)
            tunggu = """Mohon Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(0.1)
            siluman = [
                'Siluman Kucing Garong', 
                'Siluman Pocong Gundul', 
                'Siluman Pocong Gondrong',
                'Siluman Banaspati',
                'Siluman Kera',
                'Siluman Babi Ngepet',
                'Siluman Ikan Cupang',
                'Siluman Burung Bangau',
                'Siluman Kuntilanak Ungu',
                'Siluman Tuyul Mullet',
                'Siluman Suster Koprol',
                'Siluman Serigala Berbulu Ayam',
                'Siluman Ular Anaconda',
                'Siluman Kuda Poni'
                ]
            demit = random.choice(siluman)
            jin = f"""{demit} Yang Sakti Sedang Meramalkan Nomor Togel Jitu....."""
            for i in jin:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            print()
            for i in range(3):
                time.sleep(0.1)
            print("Nomor Togel Berhasil Di Dapatkan!")
            for index in range(4):
                togel = togel + random.choice(nomor)
            for i in range(3):
                time.sleep(0.1)
            print("Nomor Togel :", togel)
        if pilih == 4:
            kejawen()
        if pilih > 4:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            kejawen()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            kejawen()
        print("══════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        kejawen()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("═══════════════════════════════════════════════")
    print("❚█══════════════ TOOLS KEJAWEN ══════════════█❚")
    print("═══════════════════════════════════════════════")
    print("1. CEK WETON")
    print("2. CEK WETON JODOH")
    print("3. RAMAL TOGEL")
    print("4. KELUAR")
    print("═══════════════════════════════════════════════")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        weton()
    if pilih == 2:
        jodoh()
    if pilih == 3:
        togel()
    if pilih == 4:
        menu()
    if pilih > 4:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        kejawen()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        kejawen()

def sekolah():
    def biodata():
        nama = ["", "Aiswatun Kholifah", "Aldyaz Budi Pratama", "Alfiah Nur Aini", "Alzhar Chandraditya Dewandra", "Anggita Dewi Lestari", "Anggreini Hidayatul Febriningtyas", "Ani Ghoniyyah Khairunnisa", "Apsha Arfianah", "Aryasatya Fitradhia Attaya", "Azrina Elfaradita", "Bayu Suryadinata", "Cindy Fadilah", "Dicky Widya Pergodi", "Diva Ayu Ramadhany", "Elta Prawira Ayu Lestari", "Erzha Fadilah Pradista", "Ezar Fausta Gadang Praptama", "Fifian Aqila Salmadina", "Geluh Anggit Mutmainah", "Keysha Navi'Azkiya", "Khoirunnisa Aulia Ramadhani", "Lufi Cahyanti", "Meilian Ririn Anggani", "Muhammad Fakhri Bintang Pratama", "Muhammad Naufal Allaam", "Muhammad Syarif Hidayat", "Najwa Karima", "Najwa Raya Qizzani", "Nurhayati", "Rejo Wiranata", "Suryo Saputro", "Weni Puspita Sari", "Widiana Agustiani", "Zaffa Zidni Elma", ""]
        kelas = "X PPLG 1"
        absen = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", ""]
        Jk = ["", "P", "L", "P", "L", "P", "P", "P", "P", "L", "P", "L", "P", "L", "P", "P", "L", "L", "P", "P", "P", "P", "P", "P", "L", "L", "L", "P", "P", "P", "L", "L", "P", "P", "P"]
        nis = ["", "237627", "237629", "237630", "237631", "237632", "237633", "237634", "237635", "237636", "237637", "237638", "237639", "237640", "237641", "237642", "237643", "237644", "237645", "237646", "237647", "237648", "237649", "237650", "237651", "237652", "237653", "237654", "237655", "237656", "237657", "237658", "237659", "237660", "237661", ""]
        nisn = ["", "0085015395", "0081976251", "0087219854", "0086764132", "0087456365", "0084855541", "0144402982", "0084785548", "3075729809", "0077064698", "0083426091", "0083822797", "0082874531", "0074654298", "0082587563", "0075716536", "0089517678", "0071138317", "0083623816", "0085483641", "0074977513", "0083676438", "0087011436", "0084672080", "0077270531", "0077987295", "0082754127", "0088536961", "0088315055", "0065088564", "0072094975", "0089376095", "0081732431", "0083387853", ""]
        belajar = ["", "aiswatun.kholifah41@smk.belajar.id", "aldyaz.budi19@smk.belajar.id", "alfiah.nur674@smk.belajar.id", "alzhar.chandraditya1@smk.belajar.id", "anggita.dewi523@smk.belajar.id", "anggreini.hidayatul50@smk.belajar.id", "ani.ghoniyyah32@smk.belajar.id", "apsha.arfianah24@smk.belajar.id", "aryasatya.fitradhia28@smk.belajar.id", "azrina.elfaradita28@smk.belajar.id", "bayu.suryadinata43@smk.belajar.id", "cindy.fadilah48@smk.belajar.id", "dicky.widya50@smk.belajar.id", "diva.ayu1925@smk.belajar.id", "elta.prawira37@smk.belajar.id", "erzha.fadilah26@smk.belajar.id", "ezar.fausta106@smk.belajar.id", "fifian.aqila47@smk.belajar.id", "geluh.anggit22@smk.belajar.id", "keysha.naviazkiya1@smk.belajar.id", "khoirunnisa.aulia282@smk.belajar.id", "lufi.cahyanti42@smk.belajar.id", "meilian.ririn9@smk.belajar.id", "muhammad.fakhri31971@smk.belajar.id", "muhammad.naufal105492@smk.belajar.id", "muhammad.syarif16982@smk.belajar.id", "najwa.karima341@smk.belajar.id", "najwa.raya123@smk.belajar.id", "nurhayati.17511@smk.belajar.id", "rejo.wiranata8@smk.belajar.id", "suryo.saputro68@smk.belajar.id", "weni.puspita100@smk.belajar.id", "widiana.agustiani3@smk.belajar.id", "zaffa.zidni30@smk.belajar.id", ""]
        kndmn = ["", "aiswatun237627@student.smkn1kandeman.sch.id", "aldyaz237629@student.smkn1kandeman.sch.id", " alfiah237630@student.smkn1kandeman.sch.id", "alzhar237631@student.smkn1kandeman.sch.id", "anggita237632@student.smkn1kandeman.sch.id", "anggreini237633@student.smkn1kandeman.sch.id", "anighoni237634@student.smkn1kandeman.sch.id", "apsha237635@student.smkn1kandeman.sch.id", "aryasatya237636@student.smkn1kandeman.sch.id", "azrina237637@student.smkn1kandeman.sch.id", "bayusurya237638@student.smkn1kandeman.sch.id", "cindy237639@student.smkn1kandeman.sch.id", "dicky237640@student.smkn1kandeman.sch.id", "diva237641@student.smkn1kandeman.sch.id", "elta237642@student.smkn1kandeman.sch.id", "erzha237643@student.smkn1kandeman.sch.id", "ezar237644@student.smkn1kandeman.sch.id", "fifian237645@student.smkn1kandeman.sch.id", "geluh237646@student.smkn1kandeman.sch.id", "keysha237647@student.smkn1kandeman.sch.id", "khoirunnisa237648@student.smkn1kandeman.sch.id", "lufi237649@student.smkn1kandeman.sch.id", "meilian237650@student.smkn1kandeman.sch.id", "muhfakhri237651@student.smkn1kandeman.sch.id", "muhnaufal237652@student.smkn1kandeman.sch.id", "muhsyarif237653@student.smkn1kandeman.sch.id", "najwaka237654@student.smkn1kandeman.sch.id", "najwara237655@student.smkn1kandeman.sch.id", "nurhayati237656@student.smkn1kandeman.sch.id", "rejo237657@student.smkn1kandeman.sch.id", "suryo237658@student.smkn1kandeman.sch.id", "suryo237658@student.smkn1kandeman.sch.id", "weni237659@student.smkn1kandeman.sch.id", "widiana237660@student.smkn1kandeman.sch.id", "zaffa237661@student.smkn1kandeman.sch.id", ""]
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═══════════════════════════════════════════════════════════════")
        print("❚█════════════ BIODATA SISWA X PPLG 1 (Keluar:0) ════════════█❚")
        print("═══════════════════════════════════════════════════════════════")
        absn = int(input("Masukkan Nomor Absen Siswa 1-34 : "))
        for i in range(3):
            time.sleep(0.01)
        def bio():
            print("═══════════════════════════════════════════════════════════════")
            print("Nama :", nama[absn])
            print("Kelas :", kelas)
            print("Absen :", absen[absn])
            print("Kelamin :", Jk[absn])
            print("NIS :", nis[absn])
            print("NISN :", nisn[absn])
            print("Akun Belajar :", belajar[absn])
            print("Akun SMK :", kndmn[absn])
            print("═══════════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            biodata()
        if absn > 34:
            for i in range(3):
                time.sleep(0.01)
            print("═══════════════════════════════════════════════════════════════")
            tdk = """Nomor Absen Yang Anda Masukkan Tidak Tersedia..... Silahkan Coba Lagi"""
            for i in tdk:
                print(i, end="", flush=True)
                time.sleep(0.03)
            for i in range(3):
                time.sleep(0.01)
            input()
            biodata()
        if absn == 0:
            for i in range(3):
                time.sleep(0.01)
            print("═══════════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            sekolah()
        if absn > 0 and absn < 35:
            bio()

    def jam():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═════════════════════════════════════════════════════════════════")
        print("❚█════════════ PLOT JAM PEMBELAJARAN SMKN KANDEMAN ════════════█❚")
        print("═════════════════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        print("> > > > > SENIN < < < < <")
        print("Jam ke-0 : 07:00 - 07:45 (JP : 00:45)")
        print("Jam ke-1 : 07:45 - 08:30 (JP : 00:45)")
        print("Jam ke-2 : 08:30 - 09:15 (JP : 00:45)")
        print("Istirahat 1 : 09:15 - 09:30 (JP : 00:15)")
        print("Jam ke-3 : 09:30 - 10:10 (JP : 00:40)")
        print("Jam ke-4 : 10:10 - 10:50 (JP : 00:40)")
        print("Jam ke-5 : 10:50 - 11:30 (JP : 00:40)")
        print("Istirahat 2 : 11:30 - 12:30 (JP : 1:00)")
        print("Jam ke-6 : 12:30 - 13:10 (JP : 00:40)")
        print("Jam ke-7 : 13:10 - 13:45 (JP : 00:35)")
        print("Jam ke-8 : 13:45 - 14:20 (JP : 00:35)")
        print("Jam ke-9 : 14:20 - 14:55 (JP : 00:35)")
        print("Jam ke-10 : 14:55 - 15:30 (JP : 00:35)")
        print()
        print("> > > > > SELASA-KAMIS < < < < <")
        print("Jam ke-1 : 07:00 - 07:45 (JP : 00:45)")
        print("Jam ke-2 : 07:45 - 08:30 (JP : 00:45)")
        print("Jam ke-3 : 08:30 - 09:15 (JP : 00:45)")
        print("Istirahat 1 : 09:15 - 09:30 (JP : 00:15)")
        print("Jam ke-4 : 09:30 - 10:10 (JP : 00:40)")
        print("Jam ke-5 : 10:10 - 10:50 (JP : 00:40)")
        print("Jam ke-6 : 10:50 - 11:30 (JP : 00:40)")
        print("Istirahat 2 : 11:30 - 12:30 (JP : 1:00)")
        print("Jam ke-7 : 12:30 - 13:10 (JP : 00:40)")
        print("Jam ke-8 : 13:10 - 13:45 (JP : 00:35)")
        print("Jam ke-9 : 13:45 - 14:20 (JP : 00:35)")
        print("Jam ke-10 : 14:20 - 14:55 (JP : 00:35)")
        print("Jam ke-11 : 14:55 - 15:30 (JP : 00:35)")
        print()
        print("> > > > > JUMAT < < < < <")
        print("Jam ke-0 : 07:00 - 07:45 (JP : 0:45)")
        print("Jam ke-1 : 07:45 - 08:25 (JP : 00:40)")
        print("Jam ke-2 : 08:25 - 09:05 (JP : 00:40)")
        print("Istirahat 1 : 09:05 - 09:20 (JP : 00:15)")
        print("Jam ke-3 : 09:20 - 10:05 (JP : 0:45)")
        print("Jam ke-4 : 10:05 - 10:50 (JP : 0:45)")
        print("Jam ke-5 : 10:50 - 11:35 (JP : 0:45)")
        print("Istirahat 2 : 11:35 - 12:40 (JP : 1:05)")
        print("Jam ke-6 : 12:40 - 13:20 (JP : 00:40)")
        print("Jam ke7- : 13:20 - 14:00 (JP : 00:40)")
        print("═════════════════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        sekolah()

    def jadwal():
        def KelasX():
            def PPLG():
                def PPLG1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X PPLG 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print()
                    print("Jam 1-10 : DASAR PPLG (Mukti Widodo, S.T)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print()
                    print("Jam 1-2 : DASAR PPLG (Mukti Widodo, S.T)")
                    print("Jam 3-6 : INFORMATIKA (Ismail, S.Pd., M.Pd)")
                    print("Jam 7-9 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print()
                    print("Jam 1-3 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 4-5 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print("Jam 6-7 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 8-9 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print("Jam 10-11 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print()
                    print("Jam 1-2 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 5-6 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 7-8 : SENI BUDAYA (Sigit Purnomo, S.Pd)")
                    print("Jam 9-11 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print()
                    print("Jam 1-2 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 5-7 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    PPLG()

                def PPLG2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X PPLG 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print()
                    print("Jam 1-4 : INFORMATIKA (Ismail, S.Pd., M.Pd)")
                    print("Jam 5-6 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 9-10 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print()
                    print("Jam 1-2 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 3-11 : DASAR PPLG (Mukti Widodo, S.T)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print()
                    print("Jam 1-3 : DASAR PPLG (Mukti Widodo, S.T)")
                    print("Jam 4-6 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 7-9 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print("Jam 10-11 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print()
                    print("Jam 1-3 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 4-5 : SENI BUDAYA (Sigit Purnomo, S.Pd)")
                    print("Jam 6-7 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 8-9 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print("Jam 10-11 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print()
                    print("Jam 1-2 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 3-5 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    PPLG()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN X PPLG SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. X PPLG 1")
                print("2. X PPLG 2")
                print("3. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    PPLG1()
                if pilih == 2:
                    PPLG2()
                if pilih == 3:
                    KelasX()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    PPLG()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    PPLG()

            def TE():
                def TE1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TE 1 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-6 : TAV-DASAR TE (Munifah, S.Pd)")
                    print("Jam 7 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 8-10 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : TAV-DASAR TE (Munifah, S.Pd)")
                    print("Jam 4-5 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 6-7 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 8-9 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-3 : TAV-DASAR TE (Munifah, S.Pd)")
                    print("Jam 4-6 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print("Jam 7-9 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 3-5 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Ifa Trihandayani, S.Psi)")
                    print("Jam 8-11 : INFORMATIKA (Riris Yuniaratri, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 3-4 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 5-7 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TE()

                def TE2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TE 2 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-3 : PJOK (Drs. Budi Setiyadi)")
                    print("Jam 4-6 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print("Jam 7-10 : TAV-DASAR TE (Roni Wijayanto, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 5-6 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 7 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 8-9 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 10-11 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-3 : IPAS (Vivid Ayudya Utami, S.Pd)")
                    print("Jam 4-7 : TAV-DASAR TE (Muhammad Huda, S.Pd)")
                    print("Jam 8-11 : TAV-DASAR TE (Yumaroh, S.Pd., M.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 3-4 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 5-7 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 8-9 : BIMBINGAN KONSELING (Ifa Trihandayani, S.Psi)")
                    print("Jam 10-11 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : IPAS (Vivid Ayudya Utami, S.Pd)")
                    print("Jam 4-7 : INFORMATIKA (Riris Yuniaratri, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TE()

                def TE3():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TE 3 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 5-10 : TEI-DASAR TE (Heru Nugroho, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-4 : INFORMATIKA (Riris Yuniaratri, S.Pd)")
                    print("Jam 5-7 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print("Jam 8-9 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 10-11 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 5-6 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 7-8 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 9-11 : PJOK (Drs. Budi Setiyadi)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 3-5 : IPAS (Umi Kulsum, S.Pd)")
                    print("Jam 6-11 : TEI-DASAR TE (Heru Nugroho, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : IPAS (Umi Kulsum, S.Pd)")
                    print("Jam 4-5 : BIMBINGAN KONSELING (Nanung Sutan Aribowo, S.Psi)")
                    print("Jam 6-7 : PKN (Maria Ulfa, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TE()

                def TE4():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TE 4 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 3-4 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 5-6 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 9-10 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : TEI-DASAR TE (Heru Nugroho, S.Pd)")
                    print("Jam 7-8 : BIMBINGAN KONSELING (Ariyawan Widuanto, S.Pd)")
                    print("Jam 9-11 : PJOK (Drs. Budi Setiyadi)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : TEI-DASAR TE (Heru Nugroho, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 9-11 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 3-6 : INFORMATIKA (Riris Yuniaratri, S.Pd)")
                    print("Jam 7-9 : IPAS (Umi Kulsum, S.Pd)")
                    print("Jam 10-11 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 3-4 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 5-7 : IPAS (Umi Kulsum, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TE()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN X TE SMKN KANDEMAN ════════════█❚")
                print("════════════════════════════════════════════════════════════════")
                print("1. X TE 1")
                print("2. X TE 2")
                print("3. X TE 3")
                print("4. X TE 4")
                print("5. KELUAR")
                print("════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TE1()
                if pilih == 2:
                    TE2()
                if pilih == 3:
                    TE3()
                if pilih == 4:
                    TE4()
                if pilih == 5:
                    KelasX()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TE()
                if pilih > 5:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TE()

            def TKL():
                def TKL1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TKL 1 SMKN KANDEMAN ════════════█❚")
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 5-10 : TITL-DASAR TKL (Jalli Khoirul Latif, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : TITL-DASAR TKL (Vivid Ayudya Utami, S.Pd)")
                    print("Jam 7-8 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 9-11 : IPAS (Tri Hersuci, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-3 : PJOK (Drs. Budi Setiyadi)")
                    print("Jam 4-5 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 6-9 : INFORMATIKA (Riris Yuniaratri, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-3 : PABP (Sri Harning, S.Pd.I)")
                    print("Jam 4-5 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 8-9 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : IPAS (Tri Hersuci, S.Pd)")
                    print("Jam 4-5 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Defi Listyaningrum, S.Pd)")
                    print()
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKL()

                def TKL2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TKL 2 SMKN KANDEMAN ════════════█❚")
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-3 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 4-5 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 6-7 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 8-10 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : IPAS (Yunida, S.Si)")
                    print("Jam 4-5 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 6-7 : SENI BUDAYA (Sigit Purnomo, S.Pd)")
                    print("Jam 8-11 : INFORMATIKA (Riris Yuniaratri, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 3-4 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 5-6 : BIMBINGAN KONSELING (Defi Listyaningrum, S.Pd)")
                    print("Jam 7-8 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 9-11 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-6 : TITL-DASAR TKL (Vivid Ayudya Utami, S.Pd)")
                    print("Jam 7-9 : IPAS (Yunida, S.Si)")
                    print("Jam 10-11 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 2-7 : TITL-DASAR TKL (Jalli Khoirul Latif, S.Pd)")
                    print()
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKL()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN X TKL SMKN KANDEMAN ════════════█❚")
                print("════════════════════════════════════════════════════════════════")
                print("1. X TKL 1")
                print("2. X TKL 2")
                print("3. KELUAR")
                print("════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TKL1()
                if pilih == 2:
                    TKL2()
                if pilih == 3:
                    KelasX()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKL()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKL()

            def TM():
                def TM1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TM 1 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-4 : TP-DASAR TM (Mahmudi, S.Pd)")
                    print("Jam 5-8 : TP-DASAR TM (Imron Fathony, S.T)")
                    print("Jam 9-10 : PKN (Maria Ulfa, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 3-5 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 8-11 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : TP-DASAR TM (Ibnu Khamdani, S.Pd)")
                    print("Jam 5-7 : IPAS (Yunida, S.Si)")
                    print("Jam 8-9 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 10-11 : SEJARAH (Maria Ulfa, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 3-5 : IPAS (Yunida, S.Si)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Wiwik Apriani, S.Pd)")
                    print("Jam 8-9 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 5-7 : PABP (Sri Harning, S.Pd.I)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TM()

                def TM2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TM 2 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 3-4 : SEJARAH (Maria Ulfa, S.Pd)")
                    print("Jam 5-6 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 7-8 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 9-10 : BIMBINGAN KONSELING (Wiwik Apriani, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-4 : TP-DASAR TM (Mahmudi, S.Pd)")
                    print("Jam 5-8 : TP-DASAR TM (Imron Fathony, S.T)")
                    print("Jam 9-11 : IPAS (Yunida, S.Si)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-3 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 4-5 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 6-9 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print("Jam 10-11 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-4 : TP-DASAR TM (Ibnu Khamdani, S.Pd)")
                    print("Jam 5-6 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 7-8 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 9-11 : PABP (Sri Harning, S.Pd.I)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : IPAS (Yunida, S.Si)")
                    print("Jam 4-5 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 6-7 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TM()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═══════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN X TM SMKN KANDEMAN ════════════█❚")
                print("═══════════════════════════════════════════════════════════════")
                print("1. X TM 1")
                print("2. X TM 2")
                print("3. KELUAR")
                print("═══════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TM1()
                if pilih == 2:
                    TM2()
                if pilih == 3:
                    KelasX()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TM()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TM()

            def TO():
                def TO1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TO 1 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-4 : TKR-DASAR TO (S. Mulyono, S.Pd)")
                    print("Jam 5-6 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 7-10 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 3-4 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 5-8 : TKR-DASAR TO (S. Mulyono, S.Pd)")
                    print("Jam 9-11 : IPAS (Vivid Ayudya Utami, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : TKR-DASAR TO (S. Mulyono, S.Pd)")
                    print("Jam 5-7 : IPAS (Vivid Ayudya Utami, S.Pd)")
                    print("Jam 8-9 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-3 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print("Jam 4-5 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 6-7 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 8-9 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 4-5 : BIMBINGAN KONSELING (Kusumadewi, S.Pd. M.Pd)")
                    print("Jam 6-7 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print()
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()

                def TO2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TO 2 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 5-8 : TKR-DASAR TO (Sigit Raharjo, S.Pd)")
                    print("Jam 9-10 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 4-5 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 6-7 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 8-11 : TKR-DASAR TO (Sigit Raharjo, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print("Jam 5-8 : TKR-DASAR TO (Sigit Raharjo, S.Pd)")
                    print("Jam 9-11 : IPAS (Vivid Ayudya Utami, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 5-6 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 7-9 : IPAS (Vivid Ayudya Utami, S.Pd)")
                    print("Jam 10-11 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print("Jam 4-5 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Kusumadewi, S.Pd. M.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()

                def TO3():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TO 3 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print("Jam 3-6 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print("Jam 7-8 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 9-10 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-4 : TKR-DASAR TO (Beny Agung Damayanto, S.T)")
                    print("Jam 5-7 : IPAS (Yunida, S.Si)")
                    print("Jam 8-9 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 10-11 : PKN (Maria Ulfa, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 5-6 : BIMBINGAN KONSELING (Ariyawan Widuanto, S.Pd)")
                    print("Jam 7-8 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 9-11 : PJOK (Marndiyah, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-4 : TKR-DASAR TO (Beny Agung Damayanto, S.T)")
                    print("Jam 5-6 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 7 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 8-9 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-4 : TKR-DASAR TO (Beny Agung Damayanto, S.T)")
                    print("Jam 5-7 : IPAS (Yunida, S.Si)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()

                def TO4():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TO 4 SMKN KANDEMAN ════════════█❚")
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-10 : TSM-DASAR TO (Arif Saifudin, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 4-7 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print("Jam 8-9 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 10-11 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : TSM-DASAR TO (Arif Saifudin, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 5-6 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 7-8 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 9-11 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 3-4 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 5-6 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 7-9 : IPAS (Satria Nur Karim Amrullah, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 4-5 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Zuhroh M. Albar, M.Pd.Kons)")
                    print()
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()

                def TO5():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN X TO 5 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print("Jam 3-4 : BIMBINGAN KONSELING (Zuhroh M. Albar, M.Pd.Kons)")
                    print("Jam 5-6 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 7-8 : SENI BUDAYA (Puguh Ario Sembodo, S.Pd)")
                    print("Jam 9-10 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-11 : TSM-DASAR TO (Arif Saifudin, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 3-5 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 6 : TKR-DASAR TO (Arif Saifudin, S.Pd)")
                    print("Jam 7-9 : IPAS (Tri Hersuci, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Ardiani Pratiwi, S.Pd)")
                    print("Jam 3-4 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 5-6 : B. INDONESIA (Chanifah Ulfah, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 9-11 : PJOK (Marndiyah, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-4 : INFORMATIKA (Rahadiana Zulrie Widiastuti, S.Kom)")
                    print("Jam 5-7 : IPAS (Tri Hersuci, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═══════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN X TO SMKN KANDEMAN ════════════█❚")
                print("═══════════════════════════════════════════════════════════════")
                print("1. X TO 1")
                print("2. X TO 2")
                print("3. X TO 3")
                print("4. X TO 4")
                print("5. X TO 5")
                print("6. KELUAR")
                print("═══════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TO1()
                if pilih == 2:
                    TO2()
                if pilih == 3:
                    TO3()
                if pilih == 4:
                    TO4()
                if pilih == 5:
                    TO5()
                if pilih == 6:
                    KelasX()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()
                if pilih > 6:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TO()

            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("═══════════════════════════════════════════════════════════════════")
            print("❚█════════════ JADWAL PELAJARAN KELAS X SMKN KANDEMAN ════════════█❚")
            print("═══════════════════════════════════════════════════════════════════")
            print("1. KELAS X PPLG")
            print("2. KELAS X TE")
            print("3. KELAS X TKL")
            print("4. KELAS X TM")
            print("5. KELAS X TO")
            print("6. KELUAR")
            print("═══════════════════════════════════════════════════════════════════")
            pilih = int(input("Masukkan Pilihan Anda : "))
            if pilih == 1:
                PPLG()
            if pilih == 2:
                TE()
            if pilih == 3:
                TKL()
            if pilih == 4:
                TM()
            if pilih == 5:
                TO()
            if pilih == 6:
                jadwal()
            if pilih == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                KelasX()
            if pilih > 6:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                KelasX()

        def KelasXI():
            def RPL():
                def RPL1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI RPL 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-5 : PKK (Sukarman, S.Pd)")
                    print("Jam 6-8 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print("Jam 9-10 : PJOK (Marndiyah, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : PKN (Drs. Harno Subedjo)")
                    print("Jam 3-4 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 5-6 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print("Jam 7-9 : PABP (Toffah, S.Ag., M.Pd)")
                    print("Jam 10-11 : B. JAWA (Suharti, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : SEJARAH (Arlin Pramudya Wardani, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 5-11 : KK-RPL (Alfian Faiz, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-11 : KK-RPL (Alfian Faiz, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-4 : MP PEMODELAN PERANGKAT LUNAK (Alfian Faiz, S.Pd)")
                    print("Jam 5-7 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()

                def RPL2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI RPL 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-10 : KK-RPL (Maziya Distya, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-8 : KK-RPL (Maziya Distya, S.Pd)")
                    print("Jam 9-11 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : MP PEMODELAN PERANGKAT LUNAK (Maziya Distya, S.Pd)")
                    print("Jam 5-6 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 7-11 : PKK (Sigit Purnomo, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 3-4 : SEJARAH (Arlin Pramudya Wardani, S.Pd)")
                    print("Jam 5-6 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 7-9 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print("Jam 10-11 : PKN (Drs. Harno Subedjo)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PABP (Toffah, S.Ag., M.Pd)")
                    print("Jam 4-5 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI RPL SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. XI RPL 1")
                print("2. XI RPL 2")
                print("3. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    RPL1()
                if pilih == 2:
                    RPL2()
                if pilih == 3:
                    KelasXI()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()

            def TAV():
                def TAV1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TAV 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-4 : KK-TAV (Roni Wijayanto, S.Pd)")
                    print("Jam 5-6 : SEJARAH (Dwi Haryaningrum, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 9-10 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 3-4 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 5-6 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 7-11 : PKK (Sukarman, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-5 : KK-TAV (Roni Wijayanto, S.Pd)")
                    print("Jam 6-8 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print("Jam 9-11 : MATEMATIKA (Kusnandar, S.Pd., M.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : KK-TEKNIK AUDIO VIDEO (Yumaroh, S.Pd., M.Pd)")
                    print("Jam 3-4 : BIMBINGAN KONSELING (Ifa Trihandayani, S.Psi)")
                    print("Jam 5-6 : PKN (Drs. Harno Subedjo)")
                    print("Jam 7-8 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print("Jam 9-11 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-7 : KK-TAV (Roni Wijayanto, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()

                def TAV2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TAV 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : KK-TEKNIK AUDIO VIDEO (Yumaroh, S.Pd., M.Pd)")
                    print("Jam 3-4 : PKN (Drs. Harno Subedjo)")
                    print("Jam 5-7 : MATEMATIKA (Kusnandar, S.Pd., M.Pd)")
                    print("Jam 8-10 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 5-6 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 7-11 : KK-TAV (Roni Wijayanto, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-5 : PKK (Sukarman, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 8-9 : BIMBINGAN KONSELING (Defi Listyaningrum, S.Pd)")
                    print("Jam 10-11 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-4 : KK-TAV (Roni Wijayanto, S.Pd)")
                    print("Jam 5-11 : KK-TAV (Yumaroh, S.Pd., M.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : SEJARAH (Dwi Haryaningrum, S.Pd)")
                    print("Jam 3-4 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print("Jam 5-7 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI TAV SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. XI TAV 1")
                print("2. XI TAV 2")
                print("3. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TAV1()
                if pilih == 2:
                    TAV2()
                if pilih == 3:
                    KelasXI()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()

            def TEI():
                def TEI1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TEI 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-3 : MATEMATIKA (Kusnandar, S.Pd., M.Pd)")
                    print("Jam 4-5 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 6-8 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 9-10 : BIMBINGAN KONSELING (Nanung Sutan Aribowo, S.Psi)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-5 : KK-TEI PRE (Bayu Setyo Prabowo, S.Pd)")
                    print("Jam 6-11 : KK-TEI PSE (Nur Budiono, S.Pd.T)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : PKN (Drs. Harno Subedjo)")
                    print("Jam 3-4 : SEJARAH (Wahyu Dwi Yulianti, S.P)")
                    print("Jam 5-10 : KK-TEI SKE (Mohamad Roisul Fata, S.Pd)")
                    print("Jam 11 : KK-TEI PRE (Bayu Setyo Prabowo, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 5-7 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print("Jam 8-9 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 10-11 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print("Jam 3-7 : PKK (Sukarman, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()

                def TEI2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TEI 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-6 : KK-TEI PSE (Nur Budiono, S.Pd.T)")
                    print("Jam 7-8 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print("Jam 9-10 : PJOK (Marndiyah, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : KK-TEI SKE (Mohamad Roisul Fata, S.Pd)")
                    print("Jam 7-11 : KK-TEI PRE (Bayu Setyo Prabowo, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print("Jam 3-4 : PKN (Drs. Harno Subedjo)")
                    print("Jam 5-6 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                    print("Jam 7-11 : PKK (Sukarman, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1 : KK-TEI PRE (Bayu Setyo Prabowo, S.Pd)")
                    print("Jam 2-4 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print("Jam 5-6 : SEJARAH (Arlin Pramudya Wardani, S.Pd)")
                    print("Jam 7-8 : BIMBINGAN KONSELING (Nanung Sutan Aribowo, S.Psi)")
                    print("Jam 9-11 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 3-5 : MATEMATIKA (Kusnandar, S.Pd., M.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Heksi Indarti, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI TEI SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. XI TEI 1")
                print("2. XI TEI 2")
                print("3. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TEI1()
                if pilih == 2:
                    TEI2()
                if pilih == 3:
                    KelasXI()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()

            def TITL():
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI TITL SMKN KANDEMAN ════════════█❚")
                print("═══════════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.01)
                print("> > > > > SENIN < < < < <")
                print("Jam 1 : BIMBINGAN KONSELING (Defi Listyaningrum, S.Pd)")
                print("Jam 2-4 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                print("Jam 5-6 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                print("Jam 7-8 : PKN (Drs. Harno Subedjo)")
                print("Jam 9-10 : B. INGGRIS (Wardoyo, S.Pd)")
                print()
                print("> > > > > SELASA < < < < <")
                print("Jam 1-6 : KK-TITL IPL (Kusdiono, S.T)")
                print("Jam 7-9 : PABP (M. Haris Fahmi, S.Pd.I)")
                print("Jam 10-11 : PJOK (Marndiyah, S.Pd)")
                print()
                print("> > > > > RABU < < < < <")
                print("Jam 1-2 : PILIHAN B. JEPANG (Santi Ihtiarini, S.Pd)")
                print("Jam 3-4 : SEJARAH (Dwi Haryaningrum, S.Pd)")
                print("Jam 5-6 : B. INGGRIS (Wardoyo, S.Pd)")
                print("Jam 7-11 : PKK (Anik Yulianah, S.Pd)")
                print()
                print("> > > > > KAMIS < < < < <")
                print("Jam 1-6 : KK-TITL IML (Jalli Khoirul Latif, S.Pd)")
                print("Jam 7-8 : B. JAWA (Suharti, S.Pd)")
                print("Jam 9-11 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                print()
                print("> > > > > JUMAT < < < < <")
                print("Jam 1 : BIMBINGAN KONSELING (Defi Listyaningrum, S.Pd)")
                print("Jam 2-7 : KK-TITL ITL (Bayu Setyo Prabowo, S.Pd)")
                print()
                print("═══════════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.01)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                KelasXI()

            def TKR():
                def TKR1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TKR 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 3-4 : SEJARAH (Ahmad Yusron, S.Pd)")
                    print("Jam 5-10 : KK-TKR MESIN (Moch. Tohari, S.Pd., M.Si)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 4-5 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Kusumadewi, S.Pd. M.Pd)")
                    print("Jam 8-9 : B. INGGRIS (Etty Setyaningtyas, S.S)")
                    print("Jam 10-11 : PKN (Ahmad Yusron, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : KK-TKRO SASIS (Y. Adi Priyanto, S.Pd)")
                    print("Jam 7-8 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 9-11 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-5 : PKK (Anik Yulianah, S.Pd)")
                    print("Jam 6-11 : KK-TKRO LISTRIK (Drs. Ali Mustofa)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-4 : MP MESIN SEPEDA MOTOR (Budi Purnomo, S.Pd)")
                    print("Jam 5-7 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKR()

                def TKR2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TKR 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 5 : KK-TKRO SASIS (Y. Adi Priyanto, S.Pd)")
                    print("Jam 6-7 : BIMBINGAN KONSELING (Ariyawan Widuanto, S.Pd)")
                    print("Jam 8-9 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-5 : KK-TKRO SASIS (Y. Adi Priyanto, S.Pd)")
                    print("Jam 6-11 : KK-TKR MESIN (Moch. Tohari, S.Pd., M.Si)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 3-5 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 6-11 : KK-TKRO LISTRIK (Drs. Ali Mustofa)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-3 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 4-5 : SEJARAH (Ahmad Yusron, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 8-11 : MP MESIN SEPEDA MOTOR (Sidiq Suprayogi, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-5 : PKK (Anik Yulianah, S.Pd)")
                    print("Jam 6-7 : PKN (Ahmad Yusron, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKR()

                def TKR3():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TKR 3 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 3-5 : PABP (Wahyu Permana, S.Pd.I., M.Pd)")
                    print("Jam 6-8 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 9-10 : PKN (Ahmad Yusron, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : KK-TKRO LISTRIK (Drs. Ali Mustofa)")
                    print("Jam 7-11 : PKK (Beny Agung Damayanto, S.T)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 3-4 : PJOK (Marndiyah, S.Pd)")
                    print("Jam 5-7 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 8-9 : SEJARAH (Ahmad Yusron, S.Pd)")
                    print("Jam 10-11 : B. JAWA (Suharti, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1 : BIMBINGAN KONSELING (Ariyawan Widuanto, S.Pd)")
                    print("Jam 2-5 : MP MESIN SEPEDA MOTOR (Sidiq Suprayogi, S.Pd)")
                    print("Jam 6-11 : KK-TKR MESIN (Moch. Tohari, S.Pd., M.Si)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1 : BIMBINGAN KONSELING (Ariyawan Widuanto, S.Pd)")
                    print("Jam 2-7 : KK-TKRO SASIS (Y. Adi Priyanto, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKR()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI TKR SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. XI TKR 1")
                print("2. XI TKR 2")
                print("3. XI TKR 3")
                print("4. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TKR1()
                if pilih == 2:
                    TKR2()
                if pilih == 3:
                    TKR3()
                if pilih == 4:
                    KelasXI()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKR()
                if pilih > 4:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKR()

            def TP():
                def TP1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TP 1 SMKN KANDEMAN ════════════█❚")
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-3 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print("Jam 4 : KK-TP FRAIS (Imron Fathony, S.T)")
                    print("Jam 5-6 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 7-10 : MP GT MANUFAKTUR (Ibnu Khamdani, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 3-4 : BIMBINNGAN KONSELING (Wiwik Apriani, S.Pd)")
                    print("Jam 5-7 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print("Jam 8-9 : PKK (Sunaryo, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Wardoyo, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : KK-TP BUBUT (Sunaryo, S.Pd)")
                    print("Jam 7-11 : KK-TP FRAIS (Imron Fathony, S.T)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-6 : KK-TP CNC (Eko Rachmadi, S.T)")
                    print("Jam 7-9 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Wardoyo, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PKK (Sunaryo, S.Pd)")
                    print("Jam 4-5 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 6-7 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print()
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()

                def TP2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═══════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TP 2 SMKN KANDEMAN ════════════█❚")
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 5-6 : SEJARAH (Wahyu Dwi Yulianti, S.Pd)")
                    print("Jam 7-8 : PKK (Dwi Haryaningrum, S.Pd)")
                    print("Jam 9-10 : B. JAWA (Suharti, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : BIMBINNGAN KONSELING (Wiwik Apriani, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 5-7 : PKK (Dwi Haryaningrum, S.Pd)")
                    print("Jam 8-11 : MP GT MANUFAKTUR (Ibnu Khamdani, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : KK-TP CNC (Eko Rachmadi, S.T)")
                    print("Jam 7-8 : PKN (Drs. Harno Subedjo)")
                    print("Jam 9-11 : MATEMATIKA (Dwi Herni Noviyanti, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-6 : KK-TP BUBUT (Sunaryo, S.Pd)")
                    print("Jam 7-11 : KK-TP FRAIS (Imron Fathony, S.T)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print("Jam 4-6 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 7 : KK-TP FRAIS (Imron Fathony, S.T)")
                    print()
                    print("═══════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI TP SMKN KANDEMAN ════════════█❚")
                print("═════════════════════════════════════════════════════════════════")
                print("1. XI TP 1")
                print("2. XI TP 2")
                print("3. KELUAR")
                print("═════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TP1()
                if pilih == 2:
                    TP2()
                if pilih == 3:
                    KelasXI()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()

            def TSM():
                def TSM1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TSM 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-10 : KK-TSM (Khoerur Roziqin, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-8 : KK-TSM (Khoerur Roziqin, S.Pd)")
                    print("Jam 9-11 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 3-5 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print("Jam 8-11 : MP MESIN KENDARAAN RINGAN (Y. Adi Priyanto, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : SEJARAH (Dwi Haryaningrum, S.Pd)")
                    print("Jam 3-4 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 5-6 : BIMBINGAN KONSELING (Zuhroh M. Albar, M.Pd.Kons)")
                    print("Jam 7-11 : PKK (Anik Yulianah, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : B. INDONESIA (Partono Hastho, S.Pd)")
                    print("Jam 4-5 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Ida Herlina, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TSM()

                def TSM2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XI TSM 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : PKN (Drs. Harno Subedjo)")
                    print("Jam 3-4 : PJOK (Anggara Indra Prasetyadi, S.Pd)")
                    print("Jam 5-6 : BIMBINGAN KONSELING (Zuhroh M. Albar, M.Pd.Kons)")
                    print("Jam 7-10 : MP MESIN KENDARAAN RINGAN (Y. Adi Priyanto, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : MATEMATIKA (Yudha Arviani, S.Pd)")
                    print("Jam 4-8 : PKK (Anik Yulianah, S.Pd)")
                    print("Jam 9-11 : PABP (Laely Hilalliyah, S.Fil.I, M.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-11 : KK-TSM (Syamsu Haryadi, S.T)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-7 : KK-TSM (Syamsu Haryadi, S.T)")
                    print("Jam 8-9 : SEJARAH (Dwi Haryaningrum, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (da Herlina, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : B. INDONESIA (Cicik Suwaningsih, S.Pd)")
                    print("Jam 4-5 : B. INGGRIS (da Herlina, S.Pd)")
                    print("Jam 6-7 : B. JAWA (Suharti, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TSM()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XI TSM SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. XI TSM 1")
                print("2. XI TSM 2")
                print("3. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TSM1()
                if pilih == 2:
                    TSM2()
                if pilih == 3:
                    KelasXI()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TSM()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TSM()

            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("════════════════════════════════════════════════════════════════════")
            print("❚█════════════ JADWAL PELAJARAN KELAS XI SMKN KANDEMAN ════════════█❚")
            print("════════════════════════════════════════════════════════════════════")
            print("1. KELAS XI RPL")
            print("2. KELAS XI TAV")
            print("3. KELAS XI TEI")
            print("4. KELAS XI TITL")
            print("5. KELAS XI TKR")
            print("6. KELAS XI TP")
            print("7. KELAS XI TSM")
            print("8. KELUAR")
            print("════════════════════════════════════════════════════════════════════")
            pilih = int(input("Masukkan Pilihan Anda : "))
            if pilih == 1:
                RPL()
            if pilih == 2:
                TAV()
            if pilih == 3:
                TEI()
            if pilih == 4:
                TITL()
            if pilih == 5:
                TKR()
            if pilih == 6:
                TP()
            if pilih == 7:
                TSM()
            if pilih == 8:
                jadwal()
            if pilih == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                KelasXI()
            if pilih > 8:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                KelasXI()

        def KelasXII():
            def RPL():
                def RPL1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII RPL 1 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-10 : RPL-WEB (Abdul Adjis, S.Kom)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : RPL-WEB (Abdul Adjis, S.Kom)")
                    print("Jam 4-5 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 6-7 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 8-11 : PKK (Dwi Haryaningrum, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : RPL-BASIS DATA (Alfian Faiz, S.Pd)")
                    print("Jam 5-8 : PKK (Dwi Haryaningrum, S.Pd)")
                    print("Jam 9-10 : RPL-PEMROGRAMAN OBJEK (Ismail, S.Pd., M.Pd)")
                    print("Jam 11 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-5 : RPL-PEMROGRAMAN OBJEK (Ismail, S.Pd., M.Pd)")
                    print("Jam 6-7 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 8-9 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 10-11 : B. JAWA (Silvia Putri Hadiyati, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Muji Kuat, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 5-7 : PABP (Toffah, S.Ag., M.Pd)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()

                def RPL2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII RPL 2 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 3-4 : B. JAWA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 5-8 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 9-10 : B. INDONESIA (Muji Kuat, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : PKK (Dwi Haryaningrum, S.Pd)")
                    print("Jam 4-11 : RPL-WEB (Abdul Adjis, S.Kom)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-3 : PABP (Toffah, S.Ag., M.Pd)")
                    print("Jam 4-5 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 6-7 : RPL-PEMROGRAMAN OBJEK (Ismail, S.Pd., M.Pd)")
                    print("Jam 8-11 : RPL-BASIS DATA (Maziya Distya, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-5 : RPL-WEB (Abdul Adjis, S.Kom)")
                    print("Jam 6 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print("Jam 7-11 : RPL-PEMROGRAMAN OBJEK (Ismail, S.Pd., M.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : PKN (Drs. Harno Subedjo)")
                    print("Jam 3-7 : PKK (Dwi Haryaningrum, S.Pd)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII RPL SMKN KANDEMAN ════════════█❚")
                print("═══════════════════════════════════════════════════════════════════")
                print("1. XII RPL 1")
                print("2. XII RPL 2")
                print("3. KELUAR")
                print("═══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    RPL1()
                if pilih == 2:
                    RPL2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    RPL()

            def TAV():
                def TAV1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TAV 1 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 3-4 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 5-10 : TAV-PRE (Muhammad Huda, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : TAV-PSRTV (Muhammad Huda, S.Pd)")
                    print("Jam 7-8 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 9-11 : PKK (Sigit Purnomo, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Muji Kuat, S.Pd)")
                    print("Jam 3-4 : PKN (Nur Nasetyawidodo, S.H)")
                    print("Jam 5-11 : TAV-PPPAV (Munifah, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1 : BIMBINGAN KONSELING (Ifa Trihandayani, S.Psi)")
                    print("Jam 2-3 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 4-6 : PABP (Sri Harning, S.Pd.I)")
                    print("Jam 7-11 : TAV-PISAV (Roni Wijayanto, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-5 : PKK (Sigit Purnomo, S.Pd)")
                    print("Jam 6-7 : B. JAWA (Santi Ihtiarini, S.Pd)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()

                def TAV2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TAV 2 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : PKN (Nur Nasetyawidodo, S.H)")
                    print("Jam 3-4 : B. INDONESIA (Muji Kuat, S.Pd)")
                    print("Jam 5-8 : PKK (Arlin Pramudya Wardani, S.Pd)")
                    print("Jam 9-10 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : TAV-PISAV (Yumaroh, S.Pd., M.Pd)")
                    print("Jam 7-11 : TAV-PPPAV (Munifah, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Santi Ihtiarini, S.Pd)")
                    print("Jam 5-8 : PKK (Arlin Pramudya Wardani, S.Pd)")
                    print("Jam 9-11 : PABP (Sri Harning, S.Pd.I)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-6 : TAV-PSRTV (Muhammad Huda, S.Pd)")
                    print("Jam 7 : TAV-PPPAV (Munifah, S.Pd)")
                    print("Jam 8-9 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 10-11 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-6 : TEI-PRE (Muhammad Huda, S.Pd)")
                    print("Jam 7 : BIMBINGAN KONSELING (Ifa Trihandayani, S.Psi)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII TAV SMKN KANDEMAN ════════════█❚")
                print("═══════════════════════════════════════════════════════════════════")
                print("1. XII TAV 1")
                print("2. XII TAV 2")
                print("3. KELUAR")
                print("═══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TAV1()
                if pilih == 2:
                    TAV2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TAV()

            def TBSM():
                def TBSM1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TBSM 1 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1 : BIMBINGAN KONSELING (Zuhroh M. Albar, M.Pd.Kons)")
                    print("Jam 2-4 : TBSM-SASIS (Budi Purnomo, S.Pd)")
                    print("Jam 5-10 : TBSM-BENGKEL (Budi Purnomo, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 3 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 4-5 : B. JAWA (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 6-7 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 8-11 : PKK (Arlin Pramudya Wardani, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-3 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 4-11 : TBSM-MESIN (Andi Sulistiyono, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 5-7 : PABP (Toffah, S.Ag., M.Pd)")
                    print("Jam 8-11 : PKK (Arlin Pramudya Wardani, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-7 : TBSM-KELISTRIKAN (Syamsu Haryadi, S.T)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TBSM()

                def TBSM2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TBSM 2 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 3-4 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 5-6 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 9-10 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1 : BIMBINGAN KONSELING (Ariyawan Widuanto, S.Pd)")
                    print("Jam 2-5 : TBSM-SASIS (Budi Purnomo, S.Pd)")
                    print("Jam 6-11 : TBSM-BENGKEL (Budi Purnomo, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : TBSM-KELISTRIKAN (Khoerur Roziqin, S.Pd)")
                    print("Jam 7-8 : MATEMATIKA (Meisari Dwi Setyawati, S.Pd)")
                    print("Jam 9-11 : PKK (Arlin Pramudya Wardani, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-3 : PABP (Toffah, S.Ag., M.Pd)")
                    print("Jam 4-11 : TBSM-MESIN (Andi Sulistiyono, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-5 : PKK (Arlin Pramudya Wardani, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TBSM()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("════════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII TBSM SMKN KANDEMAN ════════════█❚")
                print("════════════════════════════════════════════════════════════════════")
                print("1. XII TBSM 1")
                print("2. XII TBSM 2")
                print("3. KELUAR")
                print("════════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TBSM1()
                if pilih == 2:
                    TBSM2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TBSM()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TBSM()

            def TEI():
                def TEI1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TEI 1 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1 : BIMBINGAN KONSELING (Nanung Sutan Aribowo, S.Psi)")
                    print("Jam 2-3 : TEI-PPPE (Amri Bustami, S.Pd)")
                    print("Jam 4-6 : PABP (Sri Harning, S.Pd.I)")
                    print("Jam 7-8 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 9-10 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-5 : PKK (Supriyono, S.Pd)")
                    print("Jam 6-7 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 8-9 : PKN (Nur Nasetyawidodo, S.H)")
                    print("Jam 10-11 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : TEI-SPE (Bayu Setyo Prabowo, S.Pd)")
                    print("Jam 7-11 : TEI-PRE (Nur Budiono, S.Pd.T)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-6 : TEI-PSR (Mohamad Roisul Fata, S.Pd)")
                    print("Jam 7-11 : TEI-PPPE (Amri Bustami, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PKK (Supriyono, S.Pd)")
                    print("Jam 4-5 : B. INDONESIA (Muji Kuat, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()

                def TEI2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("═════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TEI 2 SMKN KANDEMAN ════════════█❚")
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-6 : TEI-PSR (Mohamad Roisul Fata, S.Pd)")
                    print("Jam 7 : BIMBINGAN KONSELING (Nanung Sutan Aribowo, S.Psi)")
                    print("Jam 8-10 : PABP (Sri Harning, S.Pd.I)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-3 : PKK (Sigit Purnomo, S.Pd)")
                    print("Jam 4-5 : B. JAWA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 8-9 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 10-11 : PKN (Nur Nasetyawidodo, S.H)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-5 : PKK (Sigit Purnomo, S.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 8-9 : B. INDONESIA (Muji Kuat, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-5 : TEI-PRE (Nur Budiono, S.Pd.T)")
                    print("Jam 6-11 : TEI-PSE (Bayu Setyo Prabowo, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-7 : TEI-PPPE (Amri Bustami, S.Pd)")
                    print()
                    print("═════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("═══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII TEI SMKN KANDEMAN ════════════█❚")
                print("═══════════════════════════════════════════════════════════════════")
                print("1. XII TEI 1")
                print("2. XII TEI 2")
                print("3. KELUAR")
                print("═══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TEI1()
                if pilih == 2:
                    TEI2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TEI()

            def TITL():
                def TITL1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TITL 1 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 3 : PKK (Supriyono, S.Pd)")
                    print("Jam 4-5 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 6-7 : PKN (Nur Nasetyawidodo, S.H)")
                    print("Jam 8-10 : TITL-ITL (Kusdiono, S.T)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : TITL-IML (Jalli Khoirul Latif, S.Pd)")
                    print("Jam 7-11 : TITL-PPL (Supriyono, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-7 : TITL-IPL (Kusdiono, S.T)")
                    print("Jam 8-10 : TITL-ITL (Kusdiono, S.T)")
                    print("Jam 11 : BIMBINGAN KONSELING (Defi Listyaningrum, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 3-4 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 5-11 : PKK (Supriyono, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-3 : PABP (Sri Harning, S.Pd.I)")
                    print("Jam 4-5 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 6-7 : B. JAWA ((Silvia Putri Hadiyati, S.Pd))")
                    print()
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TITL()

                def TITL2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TITL 2 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-3 : PABP (Sri Harning, S.Pd.I)")
                    print("Jam 4-8 : PKK (Supriyono, S.Pd)")
                    print("Jam 9-10 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Drs. Y. Anggoro Triharyanto, M.Eng)")
                    print("Jam 3-4 : PKN (Nur Nasetyawidodo, S.H)")
                    print("Jam 5-6 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 7-8 : B. INDONESIA (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 9-11 : TITL-ITL (Kusdiono, S.T)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-6 : TITL-IML (Jalli Khoirul Latif, S.Pd)")
                    print("Jam 7-11 : TITL-PPL (Supriyono, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-7 : TITL-IPL (Kusdiono, S.T)")
                    print("Jam 8-10 : TITL-ITL (Kusdiono, S.T)")
                    print("Jam 11 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Wardoyo, S.Pd)")
                    print("Jam 3-4 : (Silvia Putri Hadiyati, S.Pd)")
                    print("Jam 5-7 : PKK (Supriyono, S.Pd)")
                    print()
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TITL()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("════════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII TITL SMKN KANDEMAN ════════════█❚")
                print("════════════════════════════════════════════════════════════════════")
                print("1. XII TITL 1")
                print("2. XII TITL 2")
                print("3. KELUAR")
                print("════════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TITL1()
                if pilih == 2:
                    TITL2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TITL()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TITL()

            def TKRO():
                def TKRO1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TKRO 1 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-5 : TKRO-MESIN (Beny Agung Damayanto, S.T)")
                    print("Jam 6-10 : TKRO-SASIS (Cahya Basuki Sumarno, S.T)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-2 : PKN (Ahmad Yusron, S.Pd)")
                    print("Jam 3-5 : PABP (Toffah, S.Ag., M.Pd)")
                    print("Jam 6-7 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 8-11 : TKRO-KELISTRIKAN (Sidiq Suprayogi, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : TKRO-MESIN (Beny Agung Damayanto, S.T)")
                    print("Jam 5 : BIMBINGAN KONSELING (Kusumadewi, S.Pd., M.Pd)")
                    print("Jam 6-7 : TKRO-PEMELIHARAAN SASIS (Cahya Basuki Sumarno, S.T)")
                    print("Jam 8-11 : TKRO-KELISTRIKAN (Sidiq Suprayogi, S.Pd)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 3-5 : PKK (Drs. Ali Mustofa)")
                    print("Jam 6-7 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 8-9 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 10-11 : B. JAWA (Rinta Dwi Jayanti, S.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 3-7 : PKK (Drs. Ali Mustofa)")
                    print()
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKRO()

                def TKRO2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("══════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TKRO 2 SMKN KANDEMAN ════════════█❚")
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-2 : TKRO-PEMELIHARAAN KELISTRIKAN (Sidiq Suprayogi, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 5-6 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 7-8 : PKN (Maria Ulfa, S.Pd)")
                    print("Jam 9-10 : B. INDONESIA (Karnadi, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-5 : TKRO-MESIN (Cahya Basuki Sumarno, S.T)")
                    print("Jam 6-11 : TKRO-SASIS (Cahya Basuki Sumarno, S.T)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-5 : TKRO-KELISTRIKAN (Sidiq Suprayogi, S.Pd)")
                    print("Jam 6-7 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 8-11 : PKK (Moch. Tohari, S.Pd., M.Si)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-4 : TKRO-MESIN (Cahya Basuki Sumarno, S.T)")
                    print("Jam 5-6 : TKRO-PEMELIHARAAN SASIS (Cahya Basuki Sumarno, S.T)")
                    print("Jam 7-8 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 9-11 : PABP (Toffah, S.Ag., M.Pd)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Yuli Rahayu, S.Pd)")
                    print("Jam 3 : BIMBINGAN KONSELING (Kusumadewi, S.Pd., M.Pd)")
                    print("Jam 4-7 : PKK (Moch. Tohari, S.Pd., M.Si)")
                    print()
                    print("══════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKRO()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("════════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII TKRO SMKN KANDEMAN ════════════█❚")
                print("════════════════════════════════════════════════════════════════════")
                print("1. XII TKRO 1")
                print("2. XII TKRO 2")
                print("3. KELUAR")
                print("════════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TKRO1()
                if pilih == 2:
                    TKRO2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKRO()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TKRO()

            def TP():
                def TP1():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TP 1 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-5 : TP-BUBUT (Sunaryo, S.Pd)")
                    print("Jam 6-10 : TP-FRAIS (Mahmudi, S.Pd)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-6 : TP-CNC (Ibnu Khamdani, S.Pd)")
                    print("Jam 7 : BIMBINGAN KONSELING (Yeni Sri Utami, S.Pd)")
                    print("Jam 8-9 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 10-11 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-4 : TP-GT MANUFAKTUR (Mohammad Aziz Assidiq, S.Pd.T)")
                    print("Jam 5-11 : PKK (Mohammad Aziz Assidiq, S.Pd.T)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-2 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 3-4 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 5-6 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 7-8 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 9-11 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-4 : TP-GERINDA (Imron Fathony, S.T)")
                    print("Jam 5 : PKK (Mohammad Aziz Assidiq, S.Pd.T)")
                    print("Jam 6-7 : PKN (Drs. Harno Subedjo)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()

                def TP2():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.02)
                    print("════════════════════════════════════════════════════════════════════")
                    print("❚█════════════ JADWAL PELAJARAN XII TP 2 SMKN KANDEMAN ════════════█❚")
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    print("> > > > > SENIN < < < < <")
                    print("Jam 1-6 : TP-CNC (Ibnu Khamdani, S.Pd)")
                    print("Jam 7 : PKK (Mohammad Aziz Assidiq, S.Pd.T)")
                    print("Jam 8-10 : PABP (M. Haris Fahmi, S.Pd.I)")
                    print()
                    print("> > > > > SELASA < < < < <")
                    print("Jam 1-5 : TP-BUBUT (Sunaryo, S.Pd)")
                    print("Jam 6-10 : TP-FRAIS (Mahmudi, S.Pd)")
                    print("Jam 11 : BIMBINGAN KONSELING (Wiwik Apriani, S.Pd)")
                    print()
                    print("> > > > > RABU < < < < <")
                    print("Jam 1-2 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 3-4 : B. JAWA (Suharti, S.Pd)")
                    print("Jam 5 : TP-GERINDA (Mahmudi, S.Pd)")
                    print("Jam 6-7 : B. INDONESIA (Karnadi, S.Pd)")
                    print("Jam 8-9 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 10-11 : PKN (Drs. Harno Subedjo)")
                    print()
                    print("> > > > > KAMIS < < < < <")
                    print("Jam 1-4 : TP-GT MANUFAKTUR (Mohammad Aziz Assidiq, S.Pd.T)")
                    print("Jam 5-11 : PKK (Mohammad Aziz Assidiq, S.Pd.T)")
                    print()
                    print("> > > > > JUMAT < < < < <")
                    print("Jam 1-2 : B. INGGRIS (Ida Rochmah Yulia, S.Pd)")
                    print("Jam 3-4 : MATEMATIKA (Dian Ekowati, S.Pd)")
                    print("Jam 5-7 : TP-GERINDA (Mahmudi, S.Pd)")
                    print()
                    print("════════════════════════════════════════════════════════════════════")
                    for i in range(3):
                        time.sleep(0.01)
                    lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                    for i in lanjut:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()

                os.system('cls' if os.name == 'nt' else 'clear')
                for i in range(2):
                    time.sleep(0.02)
                print("══════════════════════════════════════════════════════════════════")
                print("❚█════════════ JADWAL PELAJARAN XII TP SMKN KANDEMAN ════════════█❚")
                print("══════════════════════════════════════════════════════════════════")
                print("1. XII TP 1")
                print("2. XII TP 2")
                print("3. KELUAR")
                print("══════════════════════════════════════════════════════════════════")
                pilih = int(input("Masukkan Pilihan Anda : "))
                if pilih == 1:
                    TP1()
                if pilih == 2:
                    TP2()
                if pilih == 3:
                    KelasXII()
                if pilih == 0:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()
                if pilih > 3:
                    unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                    for i in unknow:
                        print(i, end="", flush=True)
                        time.sleep(0.02)
                    input()
                    TP()

            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("═════════════════════════════════════════════════════════════════════")
            print("❚█════════════ JADWAL PELAJARAN KELAS XII SMKN KANDEMAN ════════════█❚")
            print("═════════════════════════════════════════════════════════════════════")
            print("1. KELAS XII RPL")
            print("2. KELAS XII TAV")
            print("3. KELAS XII TBSM")
            print("4. KELAS XII TEI")
            print("5. KELAS XII TITL")
            print("6. KELAS XII TKRO")
            print("7. KELAS XII TP")
            print("8. KELUAR")
            print("═════════════════════════════════════════════════════════════════════")
            pilih = int(input("Masukkan Pilihan Anda : "))
            if pilih == 1:
                RPL()
            if pilih == 2:
                TAV()
            if pilih == 3:
                TBSM()
            if pilih == 4:
                TEI()
            if pilih == 5:
                TITL()
            if pilih == 6:
                TKRO()
            if pilih == 7:
                TP()
            if pilih == 8:
                jadwal()
            if pilih == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                KelasXII()
            if pilih > 8:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                KelasXII()

        def piket():
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("═════════════════════════════════════════════════════════════")
            print("❚█════════════ JADWAL GURU PIKET SMKN KANDEMAN ════════════█❚")
            print("═════════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            print("> > > > > SENIN < < < < <")
            print("-----Sesi 1")
            print("Satria Nur Karim Amrullah, S.Pd.")
            print("Riris Yuniaratri, S.pd.")
            print("Yunida, S.Si.")
            print()
            print("-----Sesi 2")
            print("Sigit Purnomo, S.Pd.")
            print("Toffah, S.Ag., M.Pd.")
            print("Tri Hersuci, S.Pd.")
            print()
            print("-----BK")
            print("Wiwik Apriani, S.Pd.")
            print("Defi Listyaningrum, S.Pd.")
            print()
            print("═════════════════════════════════════════════════════════════")
            print("> > > > > SELASA < < < < <")
            print("-----Sesi 1")
            print("Karnadi, S.Pd., Gr.")
            print("Ida Herlina, S.Pd.")
            print("M. Haris Fahmi, S.Pd.I")
            print()
            print("-----Sesi 2")
            print("Wahyu Permana, S.Pd.I., M.Pd")
            print("Sri Harning, S.Pd.I.")
            print("Santi Ihtiarini, S.Pd.")
            print()
            print("-----BK")
            print("Ifa Trihandayani, S.Psi.")
            print("Nanung Sutan Aribowo, S.Psi.")
            print()
            print("═════════════════════════════════════════════════════════════")
            print("> > > > > RABU < < < < <")
            print("-----Sesi 1")
            print("Abdul Adjis, S.Kom.")
            print("Anik Yulianah, S.Pd.")
            print("Cicik Suwaningsih, S.Pd.")
            print()
            print("-----Sesi 2")
            print("Budi Purnomo, S.Pd.")
            print("Umi Kulsum, S.Pd.")
            print("Puguh Ario Sembodo, S.Pd.")
            print()
            print("-----BK")
            print("Yeni Sri Utami, S.Pd.")
            print()
            print("═════════════════════════════════════════════════════════════")
            print("> > > > > KAMIS < < < < <")
            print("-----Sesi 1")
            print("Khoerur Roziqin, S.Pd.")
            print("Rahadiana Zulrie Widiastuti, S.Kom.")
            print("Laely Hilalliyah, S.Fil.I.")
            print()
            print("-----Sesi 2")
            print("Mukti Widodo, S.T.")
            print("Ahmad Yusron, S.Pd.")
            print("Maziya Distya, S.Pd.")
            print()
            print("-----BK")
            print("Kusumadewi, S.Pd., M.Pd.")
            print("Ariyawan Widuanto, S.Pd.")
            print()
            print("═════════════════════════════════════════════════════════════")
            print("> > > > > JUMAT < < < < <")
            print("-----Sesi 1")
            print("Mohamad Roisul Fata, S.Pd.")
            print("Dwi Herni Noviyanti, S.Pd.")
            print("Anggara Indra Prasetyadi, S.Pd.")
            print()
            print("-----Sesi 2")
            print("Ibnu Khamdani, S.Pd.")
            print("Marndiyah, S.Pd.")
            print("Meisari Dwi Setyawati, S.Pd.")
            print()
            print("-----BK")
            print("Zuhroh M.Albar, M.Pd.Kons.")
            print()
            print("═════════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            print(">>>>>>>>>> Keterangan <<<<<<<<<<")
            print("Sesi 1 : Jam Pelajaran Ke-1 s.d Ke-6, Kecuali Jumat (Jam Pelajaran Ke-1 s.d Ke-4)")
            print("Sesi 2 : Jam Pelajaran Ke-7 s.d Ke-11, Kecuali Jumat (Jam Pelajaran Ke-5 s.d Ke-7)")
            print("BK : Bimbingan Konseling")
            for i in range(3):
                time.sleep(0.01)
            print("═════════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            jadwal()

        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═══════════════════════════════════════════════════════════")
        print("❚█════════════ JADWAL PELAJARAN SMKN KANDEMAN ════════════█❚")
        print("═══════════════════════════════════════════════════════════")
        print("1. JADWAL KELAS X")
        print("2. JADWAL KELAS XI")
        print("3. JADWAL KELAS XII")
        print("4. JADWAL GURU PIKET")
        print("5. KELUAR")
        print("═══════════════════════════════════════════════════════════")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            KelasX()
        if pilih == 2:
            KelasXI()
        if pilih == 3:
            KelasXII()
        if pilih == 4:
            piket()
        if pilih == 5:
            sekolah()
        if pilih > 5:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            jadwal()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            jadwal()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("═════════════════════════════════════════════")
    print("❚█══════════════ TOOLS SEKOLAH ══════════════█❚")
    print("═════════════════════════════════════════════")
    print("1. JADWAL SEKOLAH SMKN KANDEMAN")
    print("2. BIODATA SISWA X PPLG 1")
    print("3. PLOT JAM SMKN KANDEMAN")
    print("4. KELUAR")
    print("═════════════════════════════════════════════")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        jadwal()
    if pilih == 2:
        biodata()
    if pilih == 3:
        jam()
    if pilih == 4:
        menu()
    if pilih > 4:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        sekolah()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        sekolah()

def zodiak():
    def bintang():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═════════════════════════════════════════════════════")
        print("❚█══════════════ ZODIAK RASI BINTANG ══════════════█❚")
        print("═════════════════════════════════════════════════════")
        tgl = int(input("Masukkan Tanggal Lahir Anda : "))
        bln = int(input("Masukkan Bulan Lahir Anda   : "))
        print("═════════════════════════════════════════════════════")
        if bln == 1 and tgl > 19 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Aquarius")
            aaa = """Pemilik rasi bintang satu ini konon merupakan sosok yang 
independen dan penuh dengan teka-teki. Idealismenya pun tinggi 
sehingga dalam kamusnya tidak ada kata “cukup baik”. Namun, mereka 
memiliki kecendrungan untuk memerhatikan orang lain sehingga mampu 
melihat sisi terbaik dalam diri seseorang. Sebagai catatan, meski 
simbolnya adalah pembawa air, bintang zodiak Aquarius merupakan elemen udara."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Udara")
            penjelasan = """Terkenal sebagai pribadi yang pintar bergaul, senang bertualang,
mempunyai keingintahuan tinggi, dan multitasking."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dalam urusan asmara, rasi bintang zodiak Aquarius paling 
cocok dengan sesama elemen udara, yakni Aquarius, Libra, dan Gemini.
Selain itu, mereka juga cocok dengan elemen api, yakni Leo, Sagitarius, 
dan Aries karena mereka dapat berbicara dalam tingkat intelektual yang sama.
Sementara yang harus dihindari adalah elemen air, yakni Cancer, Scorpio, dan 
Pisces, serta elemen tanah, yakni Taurus, Virgo dan Capricorn."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 2 and tgl > 0 and tgl < 19:
            print()
            print(">>>>> Zodiak Anda : Aquarius")
            aaa = """Pemilik rasi bintang satu ini konon merupakan sosok yang 
independen dan penuh dengan teka-teki. Idealismenya pun tinggi 
sehingga dalam kamusnya tidak ada kata “cukup baik”. Namun, mereka 
memiliki kecendrungan untuk memerhatikan orang lain sehingga mampu 
melihat sisi terbaik dalam diri seseorang. Sebagai catatan, meski 
simbolnya adalah pembawa air, bintang zodiak Aquarius merupakan elemen udara."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Udara")
            penjelasan = """Terkenal sebagai pribadi yang pintar bergaul, senang bertualang,
mempunyai keingintahuan tinggi, dan multitasking."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dalam urusan asmara, rasi bintang zodiak Aquarius paling 
cocok dengan sesama elemen udara, yakni Aquarius, Libra, dan Gemini.
Selain itu, mereka juga cocok dengan elemen api, yakni Leo, Sagitarius, 
dan Aries karena mereka dapat berbicara dalam tingkat intelektual yang sama.
Sementara yang harus dihindari adalah elemen air, yakni Cancer, Scorpio, dan 
Pisces, serta elemen tanah, yakni Taurus, Virgo dan Capricorn."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 2 and tgl > 18 and tgl < 30:
            print()
            print(">>>>> Zodiak Anda : Pisces")
            aaa = """Si ikan yang gemar berkhayal dan memiliki daya imajinasi tinggi.
Para Pisces juga terkenal mempunyai firasat dan intuisi tajam 
karena dapat merasakan segala hal dengan dalam. Oleh sebab itu, 
mereka bisa menjadi pemberi saran dan pendengar yang baik mengenai berbagai hal.
Simbol dari zodiak Pisces adalah ikan, sejalan dengan elemennya, yakni air."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Air")
            penjelasan = """Sifatnya cenderung perasa, emosional, serta memiliki imajinasi tinggi."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Karakter Pisces yang emosional dan sensitif membuat rasi 
bintang ini kurang cocok dengan elemen api dan udara. Karena itu 
sebaiknya hindari individu dengan bintang zodiak Aries, Leo, Sagitarius, 
Gemini, Libra, dan Aquarius. Namun, jika seorang Pisces ingin tumbuh 
di luar zona nyamannya, keenam zodiak tersebut adalah pasangan yang ideal.
Pasalnya, mereka memiliki karakter yang tangguh dan keras sebagai pasangan."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 3 and tgl > 0 and tgl < 21:
            print()
            print(">>>>> Zodiak Anda : Pisces")
            aaa = """Si ikan yang gemar berkhayal dan memiliki daya imajinasi tinggi.
Para Pisces juga terkenal mempunyai firasat dan intuisi tajam 
karena dapat merasakan segala hal dengan dalam. Oleh sebab itu, 
mereka bisa menjadi pemberi saran dan pendengar yang baik mengenai berbagai hal.
Simbol dari zodiak Pisces adalah ikan, sejalan dengan elemennya, yakni air."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Air")
            penjelasan = """Sifatnya cenderung perasa, emosional, serta memiliki imajinasi tinggi."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Karakter Pisces yang emosional dan sensitif membuat rasi 
bintang ini kurang cocok dengan elemen api dan udara. Karena itu 
sebaiknya hindari individu dengan bintang zodiak Aries, Leo, Sagitarius, 
Gemini, Libra, dan Aquarius. Namun, jika seorang Pisces ingin tumbuh 
di luar zona nyamannya, keenam zodiak tersebut adalah pasangan yang ideal.
Pasalnya, mereka memiliki karakter yang tangguh dan keras sebagai pasangan."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 3 and tgl > 20 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Aries")
            aaa = """Mereka kabarnya merupakan pribadi yang memegang teguh nilai 
kejujuran sehingga ucapannya sering terdengar kasar dan blak-blakan.
Tidak hanya itu, para Aries dikenal hanya akan melakukan sesuatu yang 
ia inginkan dan cenderung tempramental.Sebagai catatan, rasi bintang 
ini dilambangkan dengan bentuk domba jantan."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Api")
            penjelasan = """Memiliki karakter yang berapi-api, impulsif, agresif, kreatif, serta penuh semangat."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Ada tiga rasi bintang yang paling cocok dengan Aries, yakni 
Gemini, Leo, dan Sagitarius yang sama-sama tergolong elemen api.
Pasangan ini akan menghasilkan hubungan yang harmonis, kuat, 
dan tahan lama karena energi mereka serupa. Sementara zodiak yang 
paling tidak cocok dengan Aries adalah Capricorn dan Cancer, baik 
dalam hubungan pertemanan maupun asmara. Ini karena mereka memiliki 
gaya berkomunikasi, nilai-nilai, serta pendangan yang berbeda secara keseluruhan."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 4 and tgl > 0 and tgl < 21:
            print()
            print(">>>>> Zodiak Anda : Aries")
            aaa = """Mereka kabarnya merupakan pribadi yang memegang teguh nilai 
kejujuran sehingga ucapannya sering terdengar kasar dan blak-blakan.
Tidak hanya itu, para Aries dikenal hanya akan melakukan sesuatu yang 
ia inginkan dan cenderung tempramental.Sebagai catatan, rasi bintang 
ini dilambangkan dengan bentuk domba jantan."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Api")
            penjelasan = """Memiliki karakter yang berapi-api, impulsif, agresif, kreatif, serta penuh semangat."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Ada tiga rasi bintang yang paling cocok dengan Aries, yakni 
Gemini, Leo, dan Sagitarius yang sama-sama tergolong elemen api.
Pasangan ini akan menghasilkan hubungan yang harmonis, kuat, 
dan tahan lama karena energi mereka serupa. Sementara zodiak yang 
paling tidak cocok dengan Aries adalah Capricorn dan Cancer, baik 
dalam hubungan pertemanan maupun asmara. Ini karena mereka memiliki 
gaya berkomunikasi, nilai-nilai, serta pendangan yang berbeda secara keseluruhan."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 4 and tgl > 20 and tgl < 31:
            print()
            print(">>>>> Zodiak Anda : Taurus")
            aaa = """Taurus, yang dilambangkan dengan banteng.
Pemilik rasi bintang satu ini terkenal pintar, dapat dipercaya, 
serta memiliki pendirian yang teguh berdasarkan kompas hidupnya sendiri.
Oleh sebab itu, Taurus bisa tampak malas saat melakukan sesuatu untuk 
memenuhi keinginan orang lain. Sisi baiknya, ia tak terpengaruh oleh 
berbagai gosip maupun drama dan memercayai orang terdekatnya dengan sepenuh hati."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Tanah")
            penjelasan = """Sifatnya realistis, membumi, dan lebih mengutamakan logika daripada intuisi atau kata hati."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Sebagai pencari ketenangan dan kestabilan emosional, Taurus paling 
cocok dengan rasi bintang Virgo dan Capricorn. Mereka memiliki potensi 
untuk membangun hubungan yang harmonis dan saling mendukung, jauh dari konflik.
Adapun bintang zodiak yang harus Taurus hindari adalah Aquarius dan Leo.
Ini karena kedua rasi bintang tersebut menyukai inovasi dan kerap mencari 
tantangan baru dalam hidup. Akibatnya, prinsip hidupnya sangat berbeda 
dengan para pemilik zodiak Taurus."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 5 and tgl > 0 and tgl < 21:
            print()
            print(">>>>> Zodiak Anda : Taurus")
            aaa = """Taurus, yang dilambangkan dengan banteng.
Pemilik rasi bintang satu ini terkenal pintar, dapat dipercaya, 
serta memiliki pendirian yang teguh berdasarkan kompas hidupnya sendiri.
Oleh sebab itu, Taurus bisa tampak malas saat melakukan sesuatu untuk 
memenuhi keinginan orang lain. Sisi baiknya, ia tak terpengaruh oleh 
berbagai gosip maupun drama dan memercayai orang terdekatnya dengan sepenuh hati."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Tanah")
            penjelasan = """Sifatnya realistis, membumi, dan lebih mengutamakan logika daripada intuisi atau kata hati."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Sebagai pencari ketenangan dan kestabilan emosional, Taurus paling 
cocok dengan rasi bintang Virgo dan Capricorn. Mereka memiliki potensi 
untuk membangun hubungan yang harmonis dan saling mendukung, jauh dari konflik.
Adapun bintang zodiak yang harus Taurus hindari adalah Aquarius dan Leo.
Ini karena kedua rasi bintang tersebut menyukai inovasi dan kerap mencari 
tantangan baru dalam hidup. Akibatnya, prinsip hidupnya sangat berbeda 
dengan para pemilik zodiak Taurus."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 5 and tgl > 20 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Gemini")
            aaa = """Gemini dengan lambang anak kembar
Para Gemini konon memiliki dua sisi kepribadian yang dapat ia 
tampilkan pada dunia. Karakternya dapat berubah dengan cepat sesuai 
dengan lingkungan dan energi yang ia dapat, mirip karakter anak kedua.
Hal ini berkat intuisinya yang tajam dan kemampuan untuk membaca situasi."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Udara")
            penjelasan = """Terkenal sebagai pribadi yang pintar bergaul, senang bertualang, mempunyai keingintahuan tinggi, dan multitasking."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Menurut astrologi, Gemini paling cocok berhubungan dengan Libra dan Aquarius.
Ini karena mereka memiliki kesamaan dari segi pandangan sosial yang luas, 
kepandaian berbicara, dan minat dalam ide-ide baru. Karena itu dalam hubungan 
mereka bisa saling menginspirasi dan mendukung untuk eksplorasi. Sementara bintang 
zodiak yang dianggap paling tidak cocok dengan Gemini adalah Pisces dan Virgo karena 
karakter mereka yang rumit."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 6 and tgl > 0 and tgl < 21:
            print()
            print(">>>>> Zodiak Anda : Gemini")
            aaa = """Gemini dengan lambang anak kembar
Para Gemini konon memiliki dua sisi kepribadian yang dapat ia 
tampilkan pada dunia. Karakternya dapat berubah dengan cepat sesuai 
dengan lingkungan dan energi yang ia dapat, mirip karakter anak kedua.
Hal ini berkat intuisinya yang tajam dan kemampuan untuk membaca situasi."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Udara")
            penjelasan = """Terkenal sebagai pribadi yang pintar bergaul, senang bertualang, mempunyai keingintahuan tinggi, dan multitasking."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Menurut astrologi, Gemini paling cocok berhubungan dengan Libra dan Aquarius.
Ini karena mereka memiliki kesamaan dari segi pandangan sosial yang luas, 
kepandaian berbicara, dan minat dalam ide-ide baru. Karena itu dalam hubungan 
mereka bisa saling menginspirasi dan mendukung untuk eksplorasi. Sementara bintang 
zodiak yang dianggap paling tidak cocok dengan Gemini adalah Pisces dan Virgo karena 
karakter mereka yang rumit."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 6 and tgl > 20 and tgl < 31:
            print()
            print(">>>>> Zodiak Anda : Cancer")
            aaa = """Rasi bintang zodiak dengan lambang kepiting ini memiliki banyak 
hal yang tersembunyi dari pandangan orang lain. Ia memiliki intuisi yang 
kuat, sehingga dapat memutuskan sesuatu dengan baik tanpa mendengar seluruh 
fakta yang ada. Sayangnya, zodiak Cancer tampak sombong dan sulit bergaul 
pada pertemuan pertama sehingga orang cenderung takut padanya."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Air")
            penjelasan = """Sifatnya cenderung perasa, emosional, serta memiliki imajinasi tinggi."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Para Cancer paling cocok behubungan dengan Scorpio dan Pisces.
Ini karena mereka sama-sama memiliki rasa empati dan kepekaan yang kuat.
Karena itulah sebagai pasangan, mereka bisa saling memahami dengan baik.
Sementara urutan zodiak yang tidak cocok dengan Cancer adalah Aries dan 
Libra karena karakter mereka yang agresif."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 7 and tgl > 0 and tgl < 21:
            print()
            print(">>>>> Zodiak Anda : Cancer")
            aaa = """Rasi bintang zodiak dengan lambang kepiting ini memiliki banyak 
hal yang tersembunyi dari pandangan orang lain. Ia memiliki intuisi yang 
kuat, sehingga dapat memutuskan sesuatu dengan baik tanpa mendengar seluruh 
fakta yang ada. Sayangnya, zodiak Cancer tampak sombong dan sulit bergaul 
pada pertemuan pertama sehingga orang cenderung takut padanya."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Air")
            penjelasan = """Sifatnya cenderung perasa, emosional, serta memiliki imajinasi tinggi."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Para Cancer paling cocok behubungan dengan Scorpio dan Pisces.
Ini karena mereka sama-sama memiliki rasa empati dan kepekaan yang kuat.
Karena itulah sebagai pasangan, mereka bisa saling memahami dengan baik.
Sementara urutan zodiak yang tidak cocok dengan Cancer adalah Aries dan 
Libra karena karakter mereka yang agresif."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 7 and tgl > 20 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Leo")
            aaa = """Seorang dengan rasi bintang zodiak Leo memiliki rasa percaya diri 
tinggi, sehingga ia akan menjadi orang pertama yang memuji dirinya sendiri.
Inilah yang membuat zodiak bulan Juli-Agustus satu ini memiliki naluri alamiah 
sebagai seorang pemimpin. Namun karena rasa percaya diri yang tinggi ini Leo 
sangat keras dalam mengkritik dirinya sendiri."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Api")
            penjelasan = """Memiliki karakter yang berapi-api, impulsif, agresif, kreatif, serta penuh semangat."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Zodiak yang paling tidak cocok dengan Leo adalah Taurus dan Scorpio 
karena perbedaan pendekatan hidup dan nilai-nilai yang mereka miliki. Lebih baik, 
seseorang dengan bintang kelahiran Leo mencari pasangan dengan zodiak Aries dan 
Sagittarius. Ini karena mereka memiliki semangat yang sama-sama tinggi serta 
cendrung antusias menjalani hidup. Efeknya, hubungan mereka akan menciptakan 
keharmonisan komunikasi dan energi."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 8 and tgl > 0 and tgl < 22:
            print()
            print(">>>>> Zodiak Anda : Leo")
            aaa = """Seorang dengan rasi bintang zodiak Leo memiliki rasa percaya diri 
tinggi, sehingga ia akan menjadi orang pertama yang memuji dirinya sendiri.
Inilah yang membuat zodiak bulan Juli-Agustus satu ini memiliki naluri alamiah 
sebagai seorang pemimpin. Namun karena rasa percaya diri yang tinggi ini Leo 
sangat keras dalam mengkritik dirinya sendiri."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Api")
            penjelasan = """Memiliki karakter yang berapi-api, impulsif, agresif, kreatif, serta penuh semangat."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Zodiak yang paling tidak cocok dengan Leo adalah Taurus dan Scorpio 
karena perbedaan pendekatan hidup dan nilai-nilai yang mereka miliki. Lebih baik, 
seseorang dengan bintang kelahiran Leo mencari pasangan dengan zodiak Aries dan 
Sagittarius. Ini karena mereka memiliki semangat yang sama-sama tinggi serta 
cendrung antusias menjalani hidup. Efeknya, hubungan mereka akan menciptakan 
keharmonisan komunikasi dan energi."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 8 and tgl > 21 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Virgo")
            aaa = """Mereka memiliki karakter yang cerdas dan baik hati sehingga senang 
memberikan bantuan untuk orang lain. Bahkan sebagai seorang teman, para 
Virgo sering menempatkan dirinya sebagai prioritas terakhir. Adapun 
simbol zodiak Virgo adalah seorang perempuan yang tampak tenang dan damai."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Tanah")
            penjelasan = """Sifatnya realistis, membumi, dan lebih mengutamakan logika daripada intuisi atau kata hati."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Bintang zodiak yang paling ideal sebagai pasangan Virgo adalah Taurus 
dan Capricorn. Ini karena mereka sama-sama menyukai pendekatan hidup yang 
realistis dan praktis. Hubungan di antara zodiak ini akan menciptakan energi 
yang stabil dan tenang, jauh dari drama. Adapun zodiak yang harus Virgo hindari 
adalah Gemini dan Sagittarius karena mereka tergolong orang yang komunikatif dan 
berjiwa petualang."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 9 and tgl > 0 and tgl < 23:
            print()
            print(">>>>> Zodiak Anda : Virgo")
            aaa = """Mereka memiliki karakter yang cerdas dan baik hati sehingga senang 
memberikan bantuan untuk orang lain. Bahkan sebagai seorang teman, para 
Virgo sering menempatkan dirinya sebagai prioritas terakhir. Adapun 
simbol zodiak Virgo adalah seorang perempuan yang tampak tenang dan damai."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Tanah")
            penjelasan = """Sifatnya realistis, membumi, dan lebih mengutamakan logika daripada intuisi atau kata hati."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Bintang zodiak yang paling ideal sebagai pasangan Virgo adalah Taurus 
dan Capricorn. Ini karena mereka sama-sama menyukai pendekatan hidup yang 
realistis dan praktis. Hubungan di antara zodiak ini akan menciptakan energi 
yang stabil dan tenang, jauh dari drama. Adapun zodiak yang harus Virgo hindari 
adalah Gemini dan Sagittarius karena mereka tergolong orang yang komunikatif dan 
berjiwa petualang."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 9 and tgl > 22 and tgl < 31:
            print()
            print(">>>>> Zodiak Anda : Libra")
            aaa = """Seorang dengan bintang kelahiran Libra menjunjung tinggi harmoni 
dalam segala aspek kehidupan, sesuai dengan simbolnya, yakni timbangan.
Ini sebabnya mereka lihai dalam hal kompromi dan diplomasi sehingga dapat 
menjadi penengah yang baik. Zodiak ini juga menyukai lingkaran sosial yang 
luas dan senang berada bersama banyak orang. Namun, seringkali ia terlalu 
fokus pada kebahagiaan orang sekitarnya, sehingga mengabaikan keinginannya sendiri."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Udara")
            penjelasan = """Terkenal sebagai pribadi yang pintar bergaul, senang bertualang, mempunyai keingintahuan tinggi, dan multitasking."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Jika kamu memiliki rasi bintang Libra, maka carilah pasangan 
dengan zodiak Gemini dan Aquarius. Ini akrena mereka memiliki kesamaan 
dalam pandangan sosial, cara komunikasi, dan minat dengan dirimu.
Oleh sebab itu, di dalam hubungan kalian akan saling melengkapi serta 
memberi dukungan untuk menjadi lebih baik. Sementara zodiak yang perlu 
kamu hindari adalah Cancer dan Capricorn karena cara komunikasi mereka 
yang kadang terlalu emosional."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 10 and tgl > 0 and tgl < 23:
            print()
            print(">>>>> Zodiak Anda : Libra")
            aaa = """Seorang dengan bintang kelahiran Libra menjunjung tinggi harmoni 
dalam segala aspek kehidupan, sesuai dengan simbolnya, yakni timbangan.
Ini sebabnya mereka lihai dalam hal kompromi dan diplomasi sehingga dapat 
menjadi penengah yang baik. Zodiak ini juga menyukai lingkaran sosial yang 
luas dan senang berada bersama banyak orang. Namun, seringkali ia terlalu 
fokus pada kebahagiaan orang sekitarnya, sehingga mengabaikan keinginannya sendiri."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Udara")
            penjelasan = """Terkenal sebagai pribadi yang pintar bergaul, senang bertualang, mempunyai keingintahuan tinggi, dan multitasking."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Jika kamu memiliki rasi bintang Libra, maka carilah pasangan 
dengan zodiak Gemini dan Aquarius. Ini akrena mereka memiliki kesamaan 
dalam pandangan sosial, cara komunikasi, dan minat dengan dirimu.
Oleh sebab itu, di dalam hubungan kalian akan saling melengkapi serta 
memberi dukungan untuk menjadi lebih baik. Sementara zodiak yang perlu 
kamu hindari adalah Cancer dan Capricorn karena cara komunikasi mereka 
yang kadang terlalu emosional."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 10 and tgl > 22 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Scorpio")
            aaa = """Scorpio yang menyukai perdebatan serta tidak takut kontroversi.
Zodiak bulan Oktober-November ini dilambangkan dengan kalajengking.
Konon, ia merupakan pribadi yang tidak takut untuk memilih jalannya 
sendiri tanpa peduli apapun yang orang lain pikirkan. Meski terlihat 
sulit didekati, bintang zodiak Scorpio memiliki perasaan yang sensitif 
dan sangat loyal pada lingkaran terdekatnya."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Air")
            penjelasan = """Sifatnya cenderung perasa, emosional, serta memiliki imajinasi tinggi."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dalam hubungan asmara, Scorpio sangat cocok dengan mereka yang 
memiliki rasi bintang Cancer dan Pisces. Ini karena mereka memiliki 
energi yang sama, yakni sensitif, penuh empati, dan intuitif.
Karena itu hubungan yang terjalin akan memberi kestabilan emosional 
untuk satu sama lain. Sementara bintang zodiak yang tidak cocok dengan 
Scorpio adalah Taurus dan Leo karena karakter mereka tangguh dan agresif.
Akibatnya, kedua zodiak ini cendrung kesulitan untuk memvalidasi emosi para Scorpio."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 11 and tgl > 0 and tgl < 23:
            print()
            print(">>>>> Zodiak Anda : Scorpio")
            aaa = """Scorpio yang menyukai perdebatan serta tidak takut kontroversi.
Zodiak bulan Oktober-November ini dilambangkan dengan kalajengking.
Konon, ia merupakan pribadi yang tidak takut untuk memilih jalannya 
sendiri tanpa peduli apapun yang orang lain pikirkan. Meski terlihat 
sulit didekati, bintang zodiak Scorpio memiliki perasaan yang sensitif 
dan sangat loyal pada lingkaran terdekatnya."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Air")
            penjelasan = """Sifatnya cenderung perasa, emosional, serta memiliki imajinasi tinggi."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dalam hubungan asmara, Scorpio sangat cocok dengan mereka yang 
memiliki rasi bintang Cancer dan Pisces. Ini karena mereka memiliki 
energi yang sama, yakni sensitif, penuh empati, dan intuitif.
Karena itu hubungan yang terjalin akan memberi kestabilan emosional 
untuk satu sama lain. Sementara bintang zodiak yang tidak cocok dengan 
Scorpio adalah Taurus dan Leo karena karakter mereka tangguh dan agresif.
Akibatnya, kedua zodiak ini cendrung kesulitan untuk memvalidasi emosi para Scorpio."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 11 and tgl > 22 and tgl < 31:
            print()
            print(">>>>> Zodiak Anda : Sagitarius")
            aaa = """Sagitarius yang disimbolkan dengan bentuk centaur, makhluk mitologi 
Yunani berwujuda manusia setengah kuda. Konon, karakter utama para 
Sagitarian adalah kemauannya yang kuat dan tidak suka mengikuti jalan 
yang sudah ada. Ia adalah seorang independen yang tidak takut untuk berjalan 
sendiri dan berpetualang, terpisah dari kawanan. Namun, di sisi lain, ia adalah
seorang yang loyal dan pandai menjaga rahasia bagi teman-temannya."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Api")
            penjelasan = """Memiliki karakter yang berapi-api, impulsif, agresif, kreatif, serta penuh semangat."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dari segi asmara, Sagitarius sangat cocok dengan Aries dan Leo karena 
mereka sama-sama independen. Efeknya, mereka tidak akan mengekang pasangannya 
dan justru menjadi teman bertualang terbaik bagi satu sama lain. Energi hidup 
mereka pun sama-sama tinggi sehingga cenderung bersemangat menghadapi tantangan.
Adapun bintang zodiak yang tidak cocok dengan Sagitarius adalah Virgo dan Pisces 
karena karakter mereka yang praktis dan sensitif."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 12 and tgl > 0 and tgl < 21:
            print()
            print(">>>>> Zodiak Anda : Sagitarius")
            aaa = """Sagitarius yang disimbolkan dengan bentuk centaur, makhluk mitologi 
Yunani berwujuda manusia setengah kuda. Konon, karakter utama para 
Sagitarian adalah kemauannya yang kuat dan tidak suka mengikuti jalan 
yang sudah ada. Ia adalah seorang independen yang tidak takut untuk berjalan 
sendiri dan berpetualang, terpisah dari kawanan. Namun, di sisi lain, ia adalah
seorang yang loyal dan pandai menjaga rahasia bagi teman-temannya."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Api")
            penjelasan = """Memiliki karakter yang berapi-api, impulsif, agresif, kreatif, serta penuh semangat."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dari segi asmara, Sagitarius sangat cocok dengan Aries dan Leo karena 
mereka sama-sama independen. Efeknya, mereka tidak akan mengekang pasangannya 
dan justru menjadi teman bertualang terbaik bagi satu sama lain. Energi hidup 
mereka pun sama-sama tinggi sehingga cenderung bersemangat menghadapi tantangan.
Adapun bintang zodiak yang tidak cocok dengan Sagitarius adalah Virgo dan Pisces 
karena karakter mereka yang praktis dan sensitif."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)

        if bln == 12 and tgl > 20 and tgl < 32:
            print()
            print(">>>>> Zodiak Anda : Capricorn")
            aaa = """Capricorn, kambing gunung yang karakternya terkenal kaku dan dingin.
Ini karena mereka sangat tunduk pada aturan, hirarki, dan memiliki pakem 
untuk melakukan sesuatu. Mereka juga kerap berfokus pada bagaimana sesuatu 
terlihat, bukan terasa, sehingga tampak dingin dan tidak peka. Selain itu, 
pemilik zodiak Capricorn bisa tampak sangat keras kepala di mata orang lain."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Tanah")
            penjelasan = """Sifatnya realistis, membumi, dan lebih mengutamakan logika daripada intuisi atau kata hati."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dalam hubungan asmara, rasi bintang yang paling ideal untuk Capricorn 
adalah Taurus dan Virgo. Mereka sama-sama memiliki pendekatan hidup yang 
realistis dan praktis. Oleh sebab itu, sebagai pasangan mereka akan memberimu 
kenyamanan serta kestabilan emosional yang diinginkan. Sementara zodiak yang 
sebaiknya Capricorn hindari adalah Aries dan Libra yang berjiwa petualang dan agresif."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if bln == 1 and tgl > 0 and tgl < 20:
            print()
            print(">>>>> Zodiak Anda : Capricorn")
            aaa = """Capricorn, kambing gunung yang karakternya terkenal kaku dan dingin.
Ini karena mereka sangat tunduk pada aturan, hirarki, dan memiliki pakem 
untuk melakukan sesuatu. Mereka juga kerap berfokus pada bagaimana sesuatu 
terlihat, bukan terasa, sehingga tampak dingin dan tidak peka. Selain itu, 
pemilik zodiak Capricorn bisa tampak sangat keras kepala di mata orang lain."""
            for i in aaa:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Elemen : Tanah")
            penjelasan = """Sifatnya realistis, membumi, dan lebih mengutamakan logika daripada intuisi atau kata hati."""
            for i in penjelasan:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print()
            print(">>>>> Urusan Asmara :")
            asmara = """Dalam hubungan asmara, rasi bintang yang paling ideal untuk Capricorn 
adalah Taurus dan Virgo. Mereka sama-sama memiliki pendekatan hidup yang 
realistis dan praktis. Oleh sebab itu, sebagai pasangan mereka akan memberimu 
kenyamanan serta kestabilan emosional yang diinginkan. Sementara zodiak yang 
sebaiknya Capricorn hindari adalah Aries dan Libra yang berjiwa petualang dan agresif."""
            for i in asmara:
                print(i, end="", flush=True)
                time.sleep(0.02)
        print()
        print()
        print("═════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        zodiak()

    def cina():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("══════════════════════════════════════════════════")
        print("❚█═════════════════ ZODIAK CINA ═════════════════█❚")
        print("══════════════════════════════════════════════════")
        thn = int(input("Masukkan Tahun Lahir Anda : "))
        print("══════════════════════════════════════════════════")
        print()
        if thn == 1936 or thn == 1948 or thn == 1960 or thn == 1972 or thn == 1984 or thn == 1996 or thn == 2008 or thn == 2020:
            print(">>>>> Shio : Tikus")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Tikus terkenal banget sama pesonanya dan kreativitas. Gak neko-neko 
dan super penasaran, mereka selalu update. Gimana caranya? Mereka punya 
cara tanya yang bener-bener jujur sampe kita gak tahan buat rahasiain. Asik, 
bisa diandelin, dan jago banget nyari promo, Tikus bakal murah hati cuma buat 
yang bener-bener deket sama mereka."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1937 or thn == 1949 or thn == 1961 or thn == 1973 or thn == 1985 or thn == 1997 or thn == 2009 or thn == 2021:
            print(">>>>> Shio : Sapi")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Sapi simbol keberuntungan dari kerja keras dan tekad murni. Sabar 
banget dan gak pernah lelah, Sapi suka sama rutinitas mereka. Meski 
dengerannya baik, susah banget ngerubah pendapat mereka. Kalo lagi kacau, 
ini tanda yang lo butuhin buat bantu ngerestorin keteraturan."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1938 or thn == 1950 or thn == 1962 or thn == 1974 or thn == 1986 or thn == 1998 or thn == 2010 or thn == 2022:
            print(">>>>> Shio : Harimau")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Pemberontak, warna-warni, dan nggak bisa ditebak, Harimau tuh bikin 
kagum dan dihormatin. Petarung yang penuh semangat ini dianggep sebagai 
tanda pembela. Harimau selalu siap bertindak, tapi mereka bisa bingung ambil keputusan."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1939 or thn == 1951 or thn == 1963 or thn == 1975 or thn == 1987 or thn == 1999 or thn == 2011 or thn == 2023:
            print(">>>>> Shio : Kelinci")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Kelinci itu kayak jadi sosok yang anggun dan selalu ada saran yang oke 
banget. Lo yang lahir di tanda ini bakalan punya hidup yang santai, karena 
lo berusaha hindarin drama sebisa mungkin. Sebaliknya, lo suka banget dikelilingi 
keindahan. Meski kadang suka mood swing, bisa terlihat cuek buat orang yang bukan 
bagian dari circle lo."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1940 or thn == 1952 or thn == 1964 or thn == 1976 or thn == 1988 or thn == 2000 or thn == 2012 or thn == 2024:
            print(">>>>> Shio : Naga")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Naga yang kuat dan keren dari mitos kuno ini enggak pernah bosan buat 
mempesona kita. Orang-orang Naga selalu penuh energi dan kekuatan. Hidup mereka
itu kaya warna-warni, dan mereka selalu asik. Ciri khas mereka tuh eksentrik dan
punya tuntutan tinggi, tapi mereka selalu punya temen atau pengagum. Penting buat
mereka punya tujuan atau misi khusus dalam hidup. Mereka butuh alasan buat berjuang, 
tujuan buat dicapai, atau kesalahan buat diperbaiki."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1941 or thn == 1953 or thn == 1965 or thn == 1977 or thn == 1989 or thn == 2001 or thn == 2013 or thn == 2025:
            print(">>>>> Shio : Ular")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Ular tuh orangnya bisa merenung dan bisa keliatan misterius awalnya. 
Beberapa Ular bisa terlihat cuek atau kayak lagi hilang dalam dunia mereka sendiri, 
tapi sebenernya itu cuma gaya hidup mereka. Mereka punya intuisi tinggi dan gak suka 
dipaksa kalo lagi analisis suatu situasi. Gaya mereka itu anggun dan lembut bicaranya, 
dan secara alami mereka tertarik sama hal-hal yang mewah dalam hidup."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1942 or thn == 1954 or thn == 1966 or thn == 1978 or thn == 1990 or thn == 2002 or thn == 2014 or thn == 2026:
            print(">>>>> Shio : Kuda")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Orang yang lahir di tahun Kuda itu penuh optimisme dan semangat tinggi, 
meski suasana hati mereka bisa bikin mereka marah-marah. Mereka punya intuisi 
yang tajam dan suka ngobrol, bisa mengajak orang yang paling pemalu buat membuka 
diri tentang hidup mereka. Kaya kepala mereka secepat mereka aktif secara fisik, 
Kuda punya refleks sosial yang lihai dan bisa atasi tekanan dengan mudah."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1943 or thn == 1955 or thn == 1967 or thn == 1979 or thn == 1991 or thn == 2003 or thn == 2015 or thn == 2027:
            print(">>>>> Shio : Kambing")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Kambing dikenal punya hati yang besar dan komitmen tinggi buat bantu orang lain. 
Seringkali pemalu, mereka biasanya tertarik sama bidang kreatif, kayak seni dan mode. 
Baik dan penyayang, mereka punya tekad yang kuat yang keliatannya bertentangan sama 
kepribadian lembut mereka. Kalo diancem, mereka bisa merespon dengan semangat dan tegas, 
meski sebenernya mereka benci banget sama pertengkaran."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1944 or thn == 1956 or thn == 1968 or thn == 1980 or thn == 1992 or thn == 2004 or thn == 2016 or thn == 2028:
            print(">>>>> Shio : Monyet")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Monyet itu tanda penemu; orang yang lahir di tahun Monyet suka tantangan. 
Mereka itu kayak entertainer alami, suka berkreasi dan bikin orang terpesona. 
Monyet bisa nanggepin masalah rumit dengan mudah dan punya daya tembus yang tinggi. 
Orang yang lahir di tanda ini secara alami ambisius dan bisa mencapai hal-hal yang 
orang lain enggak berani coba."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1945 or thn == 1957 or thn == 1969 or thn == 1981 or thn == 1993 or thn == 2005 or thn == 2017 or thn == 2029:
            print(">>>>> Shio : Ayam")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Ayam adalah yang paling misunderstood dan eksentrik dari semua tanda. 
Mereka kadang keliatan sombong dan terlalu percaya diri, tapi sebenernya di 
hati mereka bisa sangat humble. Ayam itu penampil yang luar biasa, dan mereka 
beneran bersinar pas jadi pusat perhatian. Karismatik banget, Ayam itu juga 
story-teller yang berbakat."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1946 or thn == 1958 or thn == 1970 or thn == 1982 or thn == 1994 or thn == 2006 or thn == 2018 or thn == 2030:
            print(">>>>> Shio : Anjing")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Orang yang lahir di tahun Anjing itu pintar dan langsung. Mereka punya 
rasa loyalitas yang dalam dan semangat buat keadilan dan kesetaraan. Orang yang 
lahir di tanda ini secara alami tau cara menghubungkan orang dan kerja sama sama 
orang lain, gak peduli walaupun mereka semua berbeda-beda."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1947 or thn == 1959 or thn == 1971 or thn == 1983 or thn == 1995 or thn == 2007 or thn == 2019 or thn == 2040:
            print(">>>>> Shio : Babi")
            print()
            print(">>>>> Ciri Kepribadian :")
            gaya = """Tanda Babi tuh simbol kejujuran, kesederhanaan, dan keberanian. Babi dikenal 
banget suka hidup di ujung-ujung. Baik dalam cinta, persahabatan, kebaikan hati, 
atau style. Babi enggak pernah ngelakuin sesuatu setengah-setengah! Dengan kepribadian 
yang besar dan semangat buat berekspresi, Babi enggak pernah kehabisan temen atau 
undangan. Tantangan terbesar buat tanda ini tuh nolak aja susah banget."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        print()
        print()
        if thn == 1970 or thn == 1971 or thn == 1980 or thn == 1981 or thn == 1990 or thn == 1991 or thn == 2000 or thn == 2001 or thn == 2010 or thn == 2011 or thn == 2020:
            print(">>>>> Elemen : Metal")
            print()
            print(">>>>> Karakteristik :")
            gaya = """Penuh semangat, keras kepala, punya tujuan, gigih, mandiri."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1972 or thn == 1973 or thn == 1982 or thn == 1983 or thn == 1992 or thn == 1993 or thn == 2002 or thn == 2003 or thn == 2012 or thn == 2013 or thn == 2022 or thn == 2023:
            print(">>>>> Elemen : Air")
            print()
            print(">>>>> Karakteristik :")
            gaya = """Banyak omong, kreatif, emosional, pengamat, cuek, persuasif."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1974 or thn == 1975 or thn == 1984 or thn == 1985 or thn == 1994 or thn == 1995 or thn == 2004 or thn == 2005 or thn == 2014 or thn == 2015 or thn == 2024 or thn == 2025:
            print(">>>>> Elemen : Kayu")
            print()
            print(">>>>> Karakteristik :")
            gaya = """Moral kuat, penasaran, percaya diri, suka kerjasama, maju, murah hati."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1976 or thn == 1977 or thn == 1986 or thn == 1987 or thn == 1996 or thn == 1997 or thn == 2006 or thn == 2007 or thn == 2016 or thn == 2017 or thn == 2026 or thn == 2027:
            print(">>>>> Elemen : Api")
            print()
            print(">>>>> Karakteristik :")
            gaya = """Tegas, tegas, suka petualangan, inovatif, berani, impulsif."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        if thn == 1978 or thn == 1979 or thn == 1988 or thn == 1989 or thn == 1998 or thn == 1999 or thn == 2008 or thn == 2009 or thn == 2018 or thn == 2019:
            print(">>>>> Elemen : Tanah")
            print()
            print(">>>>> Karakteristik :")
            gaya = """Praktis, kreatif, teratur, pintar, berwirausaha, santai."""
            for i in gaya:
                print(i, end="", flush=True)
                time.sleep(0.02)
        print()
        print()
        print("══════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        zodiak()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("═════════════════════════════════════════════")
    print("❚█══════════════ TOOLS ZODIAK ══════════════█❚")
    print("═════════════════════════════════════════════")
    print("1. ZODIAK RASI BINTANG")
    print("2. ZODIAK CINA")
    print("3. KELUAR")
    print("═════════════════════════════════════════════")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        bintang()
    if pilih == 2:
        cina()
    if pilih == 3:
        menu()
    if pilih > 3:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        zodiak()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        zodiak()

def game():
    def angka():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.1)
        print("════════════════════════════════════════════════════════════")
        print("❚█═══════════════ NUMBERQUEST (QUIT : 123) ═══════════════█❚")
        print("════════════════════════════════════════════════════════════")
        print("WELCOME TO NUMBERQUEST!")
        print()
        for i in range(3):
            time.sleep(0.1)
        bot = """Bot : Saya telah memilih sebuah angka antara 1-100
Silahkan tebak angka yang saya pilih dalam 5 kesempatan!"""
        for i in bot:
            print(i, end="", flush=True)
            time.sleep(0.03)
        for i in range(3):
            time.sleep(0.1)
        print()
        print()
        print("════════════════════════════════════════════════════════════")
        angka_rahasia = random.randint(1, 100)
        tebakan = 0
        kesempatan = 5
        keluar = 123
        while tebakan != angka_rahasia and kesempatan > 0:
            try:
                print()
                tebakan = int(input("Masukkan tebakan Anda: "))
            except ValueError:
                print("Tolong masukkan angka yang valid.")
                continue

            if tebakan < angka_rahasia:
                print("Tebakan Anda terlalu rendah.")
            if tebakan > angka_rahasia:
                print("Tebakan Anda terlalu tinggi.")
            if tebakan == angka_rahasia:
                print(f"Selamat! Anda berhasil menebak angka rahasianya: {angka_rahasia}")
            if tebakan == keluar:
                print()
                print("════════════════════════════════════════════════════════════")
                print()
                lnjt = input("Yakin Ingin Keluar? y/N : ")
                if lnjt == "y" or lnjt == "Y":
                    for i in range(3):
                        time.sleep(1)
                    game()
                if lnjt == "n" or lnjt == "N":
                    for i in range(3):
                        time.sleep(1)
                    angka()
    
            kesempatan -= 1
            if kesempatan > 0 and tebakan != angka_rahasia:
                print(f"Anda memiliki {kesempatan} kesempatan lagi.")

        if tebakan != angka_rahasia:
            print(f"Sayang sekali, Anda gagal menebak angka rahasianya. Angka rahasianya adalah {angka_rahasia}.")
        print()
        print("════════════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        game()

    def huruf():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.1)
        print("═════════════════════════════════════════════════════════")
        print("❚█═══════════ LETTER MASTERMIND (QUIT : QT) ═══════════█❚")
        print("═════════════════════════════════════════════════════════")
        print("WELCOME TO LETTER MASTERMIND!")
        print()
        for i in range(3):
            time.sleep(0.1)
        bot = """Bot : Saya telah memilih sebuah huruf secara acak
Silahkan tebak huruf yang saya pilih dengan benar!"""
        for i in bot:
            print(i, end="", flush=True)
            time.sleep(0.03)
        for i in range(3):
            time.sleep(0.1)
        print()
        print()
        print("═════════════════════════════════════════════════════════")
        hrf = 'abcdefghijklmnopqrstuvwxyz'
        huruf_rahasia = random.choice(hrf)
        while True:
            print()
            tebakan = input("Masukkan tebakan huruf Anda: ")
            if tebakan == "QT" or tebakan == "Qt" or tebakan == "qT" or tebakan == "qt":
                print()
                print("═════════════════════════════════════════════════════════")
                print()
                lnjt = input("Yakin Ingin Keluar? y/N : ")
                if lnjt == "y" or lnjt == "Y":
                    for i in range(2):
                        time.sleep(1)
                    game()
                if lnjt == "n" or lnjt == "N":
                    for i in range(2):
                        time.sleep(1)
                    huruf()
            if tebakan.lower() == huruf_rahasia:
                print()
                print("Anda benar! Huruf yang saya pilih adalah", huruf_rahasia)
                break
            else:
                print("Tebakan Anda salah. Coba lagi.")

        print()
        print("═════════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        game()

    def bkg():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.1)
        print("══════════════════════════════════════════════════════════")
        print("❚█════════════════ MIGHTY SCISSORS PAPER ════════════════█❚")
        print("══════════════════════════════════════════════════════════")
        print("WELCOME TO MIGHTY SCISSORS PAPER!")
        print()
        for i in range(3):
            time.sleep(0.1)
        bot = """Bot : Saya telah memilih salah satu antara batu, kertas, 
dan gunting. Silahkan tebak huruf yang saya pilih dengan benar!"""
        for i in bot:
            print(i, end="", flush=True)
            time.sleep(0.03)
        print()
        print()
        print("B (Batu)")
        print("K (Kertas)")
        print("G (Gunting)")
        print("══════════════════════════════════════════════════════════")
        tebakan = ['Batu', 'Kertas', 'Gunting']
        robot = random.choice(tebakan)
        usr = str(input("Masukkan  Tebakan Anda : "))
        print("══════════════════════════════════════════════════════════")
        print()
        if usr == 'B' and robot == 'Batu':
            print("Pilihan Anda : Batu")
            print("Pilihan Bot  : Batu")
            print()
            print("Batu Melawan Batu")
            for i in range(2):
                time.sleep(0.1)
            print("SERI!!!")
        if usr == 'B' and robot == 'Kertas':
            print("Pilihan Anda : Batu")
            print("Pilihan Bot  : Kertas")
            print()
            print("Batu Melawan Kertas")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Kalah!!!")
        if usr == 'B' and robot == 'Gunting':
            print("Pilihan Anda : Batu")
            print("Pilihan Bot  : Gunting")
            print()
            print("Batu Melawan Gunting")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Menang!!!")
        if usr == 'b' and robot == 'Batu':
            print("Pilihan Anda : Batu")
            print("Pilihan Bot  : Batu")
            print()
            print("Batu Melawan Batu")
            for i in range(2):
                time.sleep(0.1)
            print("SERI!!!")
        if usr == 'b' and robot == 'Kertas':
            print("Pilihan Anda : Batu")
            print("Pilihan Bot  : Kertas")
            print()
            print("Batu Melawan Kertas")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Kalah!!!")
        if usr == 'b' and robot == 'Gunting':
            print("Pilihan Anda : Batu")
            print("Pilihan Bot  : Gunting")
            print()
            print("Batu Melawan Gunting")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Menang!!!")

        if usr == 'K' and robot == 'Batu':
            print("Pilihan Anda : Kertas")
            print("Pilihan Bot  : Batu")
            print()
            print("Kertas Melawan Batu")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Menang!!!")
        if usr == 'K' and robot == 'Kertas':
            print("Pilihan Anda : Kertas")
            print("Pilihan Bot  : Kertas")
            print()
            print("Kertas Melawan Kertas")
            for i in range(2):
                time.sleep(0.1)
            print("SERI!!!")
        if usr == 'K' and robot == 'Gunting':
            print("Pilihan Anda : Kertas")
            print("Pilihan Bot  : Gunting")
            print()
            print("Kertas Melawan Gunting")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Kalah!!!")
        if usr == 'k' and robot == 'Batu':
            print("Pilihan Anda : Kertas")
            print("Pilihan Bot  : Batu")
            print()
            print("Kertas Melawan Batu")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Menang!!")
        if usr == 'k' and robot == 'Kertas':
            print("Pilihan Anda : Kertas")
            print("Pilihan Bot  : Kertas")
            print()
            print("Kertas Melawan Kertas")
            for i in range(2):
                time.sleep(0.1)
            print("SERI!!!")
        if usr == 'k' and robot == 'Gunting':
            print("Pilihan Anda : Kertas")
            print("Pilihan Bot  : Gunting")
            print()
            print("Batu Melawan Gunting")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Kalah!!!")

        if usr == 'G' and robot == 'Batu':
            print("Pilihan Anda : Gunting")
            print("Pilihan Bot  : Batu")
            print()
            print("Gunting Melawan Batu")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Kalah!!!")
        if usr == 'G' and robot == 'Kertas':
            print("Pilihan Anda : Gunting")
            print("Pilihan Bot  : Kertas")
            print()
            print("Gunting Melawan Kertas")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Menang!!!")
        if usr == 'G' and robot == 'Gunting':
            print("Pilihan Anda : Gunting")
            print("Pilihan Bot  : Gunting")
            print()
            print("Kertas Melawan Gunting")
            for i in range(2):
                time.sleep(0.1)
            print("SERI!!!")
        if usr == 'g' and robot == 'Batu':
            print("Pilihan Anda : Gunting")
            print("Pilihan Bot  : Batu")
            print()
            print("Gunting Melawan Batu")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Kalah!!")
        if usr == 'g' and robot == 'Kertas':
            print("Pilihan Anda : Gunting")
            print("Pilihan Bot  : Kertas")
            print()
            print("Gunting Melawan Kertas")
            for i in range(2):
                time.sleep(0.1)
            print("Anda Menang!!!")
        if usr == 'g' and robot == 'Gunting':
            print("Pilihan Anda : Gunting")
            print("Pilihan Bot  : Gunting")
            print()
            print("Gunting Melawan Gunting")
            for i in range(2):
                time.sleep(0.1)
            print("SERI!!!")
        print()
        print("══════════════════════════════════════════════════════════")
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        game()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("════════════════════════════════════════════")
    print("❚█══════════════ TOOLS GAME ══════════════█❚")
    print("════════════════════════════════════════════")
    print("1. NUMBERQUEST")
    print("2. LETTER MASTERMIND")
    print("3. MIGHTY SCISSORS PAPER")
    print("4. KELUAR")
    print("════════════════════════════════════════════")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        angka()
    if pilih == 2:
        huruf()
    if pilih  == 3:
        bkg()
    if pilih == 4:
        menu()
    if pilih > 4:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        game()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        game()

def generator():
    def pw():
        def angka():
            os.system('cls' if os.name == 'nt' else 'clear')
            karakter = "1234567890"
            password = ""
            print("═" * 43)
            print("❚█════════════ PASSWORD ANGKA ════════════█❚")
            print("═" * 43)
            jml = (int(input("Masukkan Berapa Karakter Yang Anda Inginkan : ")))
            if jml < 8:
                for i in range(3):
                    time.sleep(0.2)
                print("Password Minimal 8 Karakter!")
                for i in range(2):
                    time.sleep(0.2)
                print()
                enter = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                input()
                angka()
            if jml > 7:
                for i in range(3):
                    time.sleep(0.3)
                for index in range(jml):
                    password = password + random.choice(karakter)
                for i in range(3):
                    time.sleep(0.2)
                print("Password generated: {}".format(password))
                for i in range(3):
                    time.sleep(0.2)
                print()
                for i in range(3):
                    time.sleep(0.2)
                print("═" * 44)
                enter = """Ingin Melanjutkan? (Y/N) """
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                lnjt = input()
                if lnjt == "Y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    angka()
                if lnjt == "N":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
                if lnjt == "y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    angka()
                if lnjt == "n":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
    
        def kecil():
            os.system('cls' if os.name == 'nt' else 'clear')
            karakter = "abcdefghijklmnopqrstuvwxyz"
            password = ""
            print("═" * 49)
            print("❚█════════════ PASSWORD HURUF KECIL ════════════█❚")
            print("═" * 49)
            jml = (int(input("Masukkan Berapa Karakter Yang Anda Inginkan : ")))
            if jml < 8:
                for i in range(3):
                    time.sleep(0.2)
                print("Password Minimal 8 Karakter!")
                for i in range(2):
                    time.sleep(0.2)
                print()
                enter = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                input()
                kecil()
            if jml > 7:
                for i in range(3):
                    time.sleep(0.3)
                for index in range(jml):
                    password = password + random.choice(karakter)
                for i in range(3):
                    time.sleep(0.2)
                print("Password generated: {}".format(password))
                for i in range(3):
                    time.sleep(0.2)
                print()
                for i in range(3):
                    time.sleep(0.2)
                print("═" * 44)
                enter = """Ingin Melanjutkan? (Y/N) """
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                lnjt = input()
                if lnjt == "Y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    kecil()
                if lnjt == "N":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
                if lnjt == "y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    kecil()
                if lnjt == "n":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
    
        def besar():
            os.system('cls' if os.name == 'nt' else 'clear')
            karakter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            password = ""
            print("═" * 49)
            print("❚█════════════ PASSWORD HURUF BESAR ════════════█❚")
            print("═" * 49)
            jml = (int(input("Masukkan Berapa Karakter Yang Anda Inginkan : ")))
            if jml < 8:
                for i in range(3):
                    time.sleep(0.2)
                print("Password Minimal 8 Karakter!")
                for i in range(2):
                    time.sleep(0.2)
                print()
                enter = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                input()
                besar()
            if jml > 7:
                for i in range(3):
                    time.sleep(0.3)
                for index in range(jml):
                    password = password + random.choice(karakter)
                for i in range(3):
                    time.sleep(0.2)
                print("Password generated: {}".format(password))
                for i in range(3):
                    time.sleep(0.2)
                print()
                for i in range(3):
                    time.sleep(0.2)
                print("═" * 44)
                enter = """Ingin Melanjutkan? (Y/N) """
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                lnjt = input()
                if lnjt == "Y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    besar()
                if lnjt == "N":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
                if lnjt == "y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    besar()
                if lnjt == "n":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
    
        def rendem():
            os.system('cls' if os.name == 'nt' else 'clear')
            karakter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$&*+/?_#^`~(){[]}'
            password = ""
            print("═" * 44)
            print("❚█════════════ PASSWORD RANDOM ════════════█❚")
            print("═" * 44)
            jml = (int(input("Masukkan Berapa Karakter Yang Anda Inginkan : ")))
            if jml < 8:
                for i in range(3):
                    time.sleep(0.2)
                print("Password Minimal 8 Karakter!")
                for i in range(2):
                    time.sleep(0.2)
                print()
                enter = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                input()
                rendem()
            if jml > 7:
                for i in range(3):
                    time.sleep(0.3)
                for index in range(jml):
                    password = password + random.choice(karakter)
                for i in range(3):
                    time.sleep(0.2)
                print("Password generated: {}".format(password))
                for i in range(3):
                    time.sleep(0.2)
                print()
                for i in range(3):
                    time.sleep(0.2)
                print("═" * 44)
                enter = """Ingin Melanjutkan? (Y/N) """
                for i in enter:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                lnjt = input()
                if lnjt == "Y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    rendem()
                if lnjt == "N":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
                if lnjt == "y":
                    for i in range(2):
                        time.sleep(0.1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for i in range(2):
                        time.sleep(0.2)
                    rendem()
                if lnjt == "n":
                    for i in range(2):
                        time.sleep(0.2)
                    pw()
    
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.2)
        print("═" * 48)
        print("❚█════════════ PASSWORD GENERATOR ════════════█❚")
        print("═" * 48)
        print("1. PASSWORD ANGKA")
        print("2. PASSWORD HURUF KECIL")
        print("3. PASSWORD HURUF KAPITAL")
        print("4. PASSWORD RANDOM")
        print("5. KELUAR")
        print("═" * 48)
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            angka()
        if pilih == 2:
            kecil()
        if pilih == 3:
            besar()
        if pilih == 4:
            rendem()
        if pilih == 5:
            generator()
        if pilih > 5:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            pw()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            pw()

    def qr():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.2)
        print("═" * 46)
        print("❚█════════════ QRCODE GENERATOR ════════════█❚")
        print("═" * 46)
        print("SELAMAT DATANG DI TOOLS QR GENERATOR!")
        print()
        bot = """Pada Tools ini, kami akan membuat sebuah QrCode
sesuai dengan link/karakter yang anda masukkan"""
        for i in bot:
            print(i, end="", flush=True)
            time.sleep(0.02)
        print()
        print("═" * 46)
        link = input("Masukkan Link Anda      : ")
        nama = input("Masukkan Nama File Anda : ")
        print("═" * 46)
        print()
        for i in range(2):
            time.sleep(0.1)
        wait = """Mohon Tunggu Sebentar.....
QrCode anda sedang kami proses....."""
        for i in wait:
            print(i, end="", flush=True)
            time.sleep(0.02)
        for i in range(5):
            time.sleep(0.1)
        img = qrcode.make(link)
        img.save(f"{nama}.png")
        print()
        print()
        print("QrCode anda berhasil dibuat!")
        for i in range(2):
            time.sleep(0.1)
        cek = """Silahkan cek QrCode pada folder dimana anda
menyimpan PyTools"""
        for i in cek:
            print(i, end="", flush=True)
            time.sleep(0.02)
        print()
        print()
        print("═" * 46)
        for i in range(3):
            time.sleep(0.01)
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        generator()

    def nomor():
        def XL():
            def satu():
                awal = '0859'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═══════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                XL()

            def dua():
                awal = '0877'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═══════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                XL()

            def tiga():
                awal = '0878'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═══════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                XL()

            def empat():
                awal = '0817'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═══════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                XL()

            def lima():
                awal = '0818'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═══════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                XL()

            def enam():
                awal = '0819'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═══════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                XL()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("═══════════════════════════════════════════════")
            print("❚█════════════ NOMOR OPERATOR XL ════════════█❚")
            print("═══════════════════════════════════════════════")
            print("1. 0859")
            print("2. 0877")
            print("3. 0878")
            print("4. 0817")
            print("5. 0818")
            print("6. 0819")
            print("7. KELUAR")
            print("═══════════════════════════════════════════════")
            awal = int(input("Masukkan Awalan Nomor Yang Anda Inginkan : "))
            print("═══════════════════════════════════════════════")
            if awal == 1:
                satu()
            if awal == 2:
                dua()
            if awal == 3:
                tiga()
            if awal == 4:
                empat()
            if awal == 5:
                lima()
            if awal == 6:
                enam()
            if awal == 7:
                nomor()
            if awal > 7:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                XL()
            if awal == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                XL()

        def indosat():
            def satu():
                awal = '0814'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            def dua():
                awal = '0815'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            def tiga():
                awal = '0816'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            def empat():
                awal = '0855'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            def lima():
                awal = '0856'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            def enam():
                awal = '0857'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            def tujuh():
                awal = '0858'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                indosat()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("════════════════════════════════════════════════════════════")
            print("❚█════════════ NOMOR OPERATOR INDOSAT OOREDOO ════════════█❚")
            print("════════════════════════════════════════════════════════════")
            print("1. 0814")
            print("2. 0815")
            print("3. 0816")
            print("4. 0855")
            print("5. 0856")
            print("6. 0857")
            print("7. 0858")
            print("8. KELUAR")
            print("════════════════════════════════════════════════════════════")
            awal = int(input("Masukkan Awalan Nomor Yang Anda Inginkan : "))
            print("════════════════════════════════════════════════════════════")
            if awal == 1:
                satu()
            if awal == 2:
                dua()
            if awal == 3:
                tiga()
            if awal == 4:
                empat()
            if awal == 5:
                lima()
            if awal == 6:
                enam()
            if awal == 6:
                tujuh()
            if awal == 8:
                nomor()
            if awal > 8:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                indosat()
            if awal == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                indosat()

        def Tri():
            def satu():
                awal = '0898'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                Tri()

            def dua():
                awal = '0899'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                Tri()

            def tiga():
                awal = '0895'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                Tri()

            def empat():
                awal = '0896'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                Tri()

            def lima():
                awal = '0897'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                Tri()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("════════════════════════════════════════════════")
            print("❚█════════════ NOMOR OPERATOR TRI ════════════█❚")
            print("════════════════════════════════════════════════")
            print("1. 0898")
            print("2. 0899")
            print("3. 0895")
            print("4. 0896")
            print("5. 0897")
            print("6. KELUAR")
            print("════════════════════════════════════════════════")
            awal = int(input("Masukkan Awalan Nomor Yang Anda Inginkan : "))
            print("════════════════════════════════════════════════")
            if awal == 1:
                satu()
            if awal == 2:
                dua()
            if awal == 3:
                tiga()
            if awal == 4:
                empat()
            if awal == 5:
                lima()
            if awal == 6:
                nomor()
            if awal > 6:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                Tri()
            if awal == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                Tri()

        def axis():
            def satu():
                awal = '0832'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                axis()

            def dua():
                awal = '0833'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                axis()

            def tiga():
                awal = '0838'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                axis()

            def empat():
                awal = '0831'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("═════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                axis()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("═════════════════════════════════════════════════")
            print("❚█════════════ NOMOR OPERATOR AXIS ════════════█❚")
            print("═════════════════════════════════════════════════")
            print("1. 0832")
            print("2. 0833")
            print("3. 0838")
            print("4. 0831")
            print("5. KELUAR")
            print("═════════════════════════════════════════════════")
            awal = int(input("Masukkan Awalan Nomor Yang Anda Inginkan : "))
            print("═════════════════════════════════════════════════")
            if awal == 1:
                satu()
            if awal == 2:
                dua()
            if awal == 3:
                tiga()
            if awal == 4:
                empat()
            if awal == 5:
                nomor()
            if awal > 5:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                axis()
            if awal == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                axis()

        def telkomsel():
            def satu():
                awal = '0811'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def dua():
                awal = '0812'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def tiga():
                awal = '0813'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def empat():
                awal = '0821'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def lima():
                awal = '0822'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def enam():
                awal = '0823'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def tujuh():
                awal = '0851'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def delapan():
                awal = '0852'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            def sembilan():
                awal = '0853'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                telkomsel()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("══════════════════════════════════════════════════════")
            print("❚█════════════ NOMOR OPERATOR TELKOMSEL ════════════█❚")
            print("══════════════════════════════════════════════════════")
            print("1. 0811")
            print("2. 0812")
            print("3. 0813")
            print("4. 0821")
            print("5. 0822")
            print("6. 0823")
            print("7. 0851")
            print("8. 0852")
            print("9. 0853")
            print("10. KELUAR")
            print("══════════════════════════════════════════════════════")
            awal = int(input("Masukkan Awalan Nomor Yang Anda Inginkan : "))
            print("══════════════════════════════════════════════════════")
            if awal == 1:
                satu()
            if awal == 2:
                dua()
            if awal == 3:
                tiga()
            if awal == 4:
                empat()
            if awal == 5:
                lima()
            if awal == 6:
                enam()
            if awal == 7:
                tujuh()
            if awal == 8:
                delapan()
            if awal == 9:
                sembilan()
            if awal == 10:
                nomor()
            if awal > 10:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                telkomsel()
            if awal == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                telkomsel()

        def smartfren():
            def satu():
                awal = '0889'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def dua():
                awal = '0881'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def tiga():
                awal = '0882'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def empat():
                awal = '0883'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def lima():
                awal = '0886'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def enam():
                awal = '0887'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def tujuh():
                awal = '0888'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def delapan():
                awal = '0884'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            def sembilan():
                awal = '0885'
                nomor1 = '1234567890'
                nomor2 = '1234567890'
                nomor3 = '1234567890'
                nomor4 = '1234567890'
                nomor5 = '1234567890'
                nomor6 = '1234567890'
                nomor7 = '1234567890'
                nomor8 = '1234567890'
                rendem1 = random.choice(nomor1)
                rendem2 = random.choice(nomor2)
                rendem3 = random.choice(nomor3)
                rendem4 = random.choice(nomor4)
                rendem5 = random.choice(nomor5)
                rendem6 = random.choice(nomor6)
                rendem7 = random.choice(nomor7)
                rendem8 = random.choice(nomor8)
                tengah = rendem1+rendem2+rendem3+rendem4
                akhir = rendem5+rendem6+rendem7+rendem8
                hasil = awal + "-" + tengah + "-" + akhir
                print("Tunggu Sebentar.....")
                for i in range(5):
                    time.sleep(0.1)
                print()
                print("Nomor Anda :", hasil)
                print("══════════════════════════════════════════════════════")
                for i in range(3):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                smartfren()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("══════════════════════════════════════════════════════")
            print("❚█════════════ NOMOR OPERATOR SMARTFREN ════════════█❚")
            print("══════════════════════════════════════════════════════")
            print("1. 0889")
            print("2. 0881")
            print("3. 0882")
            print("4. 0883")
            print("5. 0886")
            print("6. 0887")
            print("7. 0888")
            print("8. 0884")
            print("9. 0885")
            print("10. KELUAR")
            print("══════════════════════════════════════════════════════")
            awal = int(input("Masukkan Awalan Nomor Yang Anda Inginkan : "))
            print("══════════════════════════════════════════════════════")
            if awal == 1:
                satu()
            if awal == 2:
                dua()
            if awal == 3:
                tiga()
            if awal == 4:
                empat()
            if awal == 5:
                lima()
            if awal == 6:
                enam()
            if awal == 7:
                tujuh()
            if awal == 8:
                delapan()
            if awal == 9:
                sembilan()
            if awal == 10:
                nomor()
            if awal > 10:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                smartfren()
            if awal == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                smartfren()

        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.2)
        print("═" * 52)
        print("❚█════════════ NUMBER PHONE GENERATOR ════════════█❚")
        print("═" * 52)
        print("1. NOMOR OPERATOR XL")
        print("2. NOMOR OPERATOR TELKOMSEL")
        print("3. NOMOR OPERATOR TRI")
        print("4. NOMOR OPERATOR INDOSAT OOREDOO")
        print("5. NOMOR OPERATOR SMARTFREN")
        print("6. NOMOR OPERATOR AXIS")
        print("7. KELUAR")
        print("═" * 52)
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            XL()
        if pilih == 2:
            telkomsel()
        if pilih == 3:
            Tri()
        if pilih == 4:
            indosat()
        if pilih == 5:
            smartfren()
        if pilih == 6:
            axis()
        if pilih == 7:
            generator()
        if pilih > 7:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            nomor()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            nomor()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("═════════════════════════════════════════════════")
    print("❚█══════════════ TOOLS GENERATOR ══════════════█❚")
    print("═════════════════════════════════════════════════")
    print("1. PASSWORD GENERATOR")
    print("2. QRCODE GENERATOR")
    print("3. NUMBER PHONE GENERATOR")
    print("4. KELUAR")
    print("═════════════════════════════════════════════════")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        pw()
    if pilih == 2:
        qr()
    if pilih == 3:
        nomor()
    if pilih == 4:
        menu()
    if pilih > 4:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        generator()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        generator()

def rendem():
    def cinta():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("══════════════════════════════════════════════")
        print("❚█═════════════ LOVE CALCULATOR ═════════════█❚")
        print("══════════════════════════════════════════════")
        anda = str(input("Masukkan Nama Anda     : "))
        pasangan = str(input("Masukkan Nama Pasangan : "))
        print("══════════════════════════════════════════════")
        print()
        hsl = random.randint(0, 100)
        for i in range(2):
            time.sleep(0.2)
        print("Hasilnya adalah", hsl,"%")
        if hsl > 80 or hsl == 80:
            pesan = """BURUAN NIKAH!"""
            for i in pesan:
                print(i, end="", flush=True)
                time.sleep(0.03)
        if hsl > 50 and hsl < 80 or hsl == 50:
            pesan = """PERTAHANKAN KAWAN!"""
            for i in pesan:
                print(i, end="", flush=True)
                time.sleep(0.03)
        if hsl > 10 and hsl < 50 or hsl == 10:
            pesan = """CARI YANG LAIN BRO!"""
            for i in pesan:
                print(i, end="", flush=True)
                time.sleep(0.03)
        if hsl < 10:
            pesan = """BADUT!!"""
            for i in pesan:
                print(i, end="", flush=True)
                time.sleep(0.03)
        for i in range(2):
            time.sleep(0.2)
        print()
        print()
        print("══════════════════════════════════════════════")
        lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
        for i in lanjut:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        rendem()

    def textvoice():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═══════════════════════════════════════════")
        print("❚█════════════ TEXT TO VOICE ════════════█❚")
        print("═══════════════════════════════════════════")
        print("1. BAHASA INDONESIA")
        print("2. BAHASA ITALIA")
        print("3. BAHASA INGGRIS")
        print("4. BAHASA JEPANG")
        print("5. BAHASA AFRIKA")
        print("6. BAHASA ARAB")
        print("7. BAHASA GERMAN")
        print("8. BAHASA SPANYOL")
        print("9. BAHASA INDIA")
        print("10. BAHASA JAWA")
        print("11. BAHASA KOREA")
        print("12. BAHASA RUSIA")
        print("13. BAHASA SUNDA")
        print("14. BAHASA FILIPINA")
        print("15. BAHASA THAILAND")
        print("16. BAHASA CHINA")
        print("17. BAHASA UKRAINA")
        print("18. BAHASA TURKI")
        print("19. BAHASA VIETNAM")
        print("20. BAHASA KANADA")
        print("21. KELUAR")
        print("═══════════════════════════════════════════")
        pilih = int(input("Masukkan Pilihan Anda : "))
        print("═══════════════════════════════════════════")
        if pilih == 1:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'id'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 2:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'it'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 3:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'en'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 4:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'ja'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 5:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'af'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 6:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'ar'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 7:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'de'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 8:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'es'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 9:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'hi'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 10:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'jw'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 11:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'ko'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 12:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'ru'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 13:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'su'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 14:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'tl'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 15:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'th'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 16:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'zh'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 17:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'uk'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 18:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'tr'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 19:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'vi'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 20:
            print()
            text = input("Masukkan Text Anda      : ")
            judul = input("Masukkan Nama File Anda : ")
            print()
            for i in range(3):
                time.sleep(1)
            tunggu = """Tunggu Sebentar....."""
            for i in tunggu:
                print(i, end="", flush=True)
                time.sleep(0.02)
            language = 'kn'
            speech = gTTS(text=text, lang=language, slow=False)
            speech.save(f"{judul}.mp3")
            for i in range(5):
                time.sleep(1)
            print()
            print("Proses Telah Selesai!")
            print()
            for i in range(3):
                time.sleep(1)
            cek = """Hasilnya berada ditempat anda menyimpan PyTools"""
            for i in cek:
                print(i, end="", flush=True)
                time.sleep(0.03)
            print()
            for i in range(3):
                time.sleep(1)
            print()
            print("═══════════════════════════════════════════")
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textvoice()
        if pilih == 21:
            rendem()
        if pilih > 21:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            textvoice()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            textvoice()

    def textasci():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═══════════════════════════════════════════")
        print("❚█════════════ TEXT TO ASCII ════════════█❚")
        print("═══════════════════════════════════════════")
        print("1. STANDARD")
        print("2. BLOCK")
        print("3. SLANT")
        print("4. DOH")
        print("5. ALLIGATOR")
        print("6. BULBHEAD")
        print("7. CYBER LARGE")
        print("8. BANNER 3D")
        print("9. ALPHABET")
        print("10. KELUAR")
        print("═══════════════════════════════════════════")
        pilih = int(input("Masukkan Pilihan Anda : "))
        print("═══════════════════════════════════════════")
        if pilih == 1:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='standard')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 2:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='block')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 3:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='slant')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 4:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='doh')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 5:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='alligator')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 6:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='bulbhead')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 7:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='cyberlarge')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 8:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='banner3-D')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 9:
            text = input("Masukkan Text : ")
            print("Tunggu Sebentar.....")
            print()
            for i in range(3):
                time.sleep(1)
            f = Figlet(font='alphabet')
            ascii_art = f.renderText(text)
            print(ascii_art)
            print()
            print("═══════════════════════════════════════════")
            for i in range(3):
                time.sleep(0.01)
            lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
            for i in lanjut:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            textasci()
        if pilih == 10:
            rendem()
        if pilih > 10:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            textasci()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            textasci()

    def ddos():
        def ip():
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("═════════════════════════════════════════════════════════════")
            print("❚█════════════ IP ADDRES DDOS ATTACK SIMULATOR ════════════█❚")
            print("═════════════════════════════════════════════════════════════")
            adres = input("Masukkan Ip Address Target : ")
            pkg = int(input("Masukkan Jumlah Serangan   : "))
            print("═════════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(1)
            mulai = str(input("Mulai Serangan?(Y/N) : "))
            if mulai == 'Y' or mulai == 'y':
                for i in range(3):
                    time.sleep(1)
                for i in range(pkg):
                    print(colored(f"Serangan Dikirimkan Menuju {adres} Sebanyak {i+1} Serangan", "red"))
                print()
                print("═════════════════════════════════════════════════════════════")
                for i in range(5):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                input()
                ddos()
            if mulai == 'N' or mulai == 'n':
                ddos()

        def web():
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("═══════════════════════════════════════════════════════════")
            print("❚█════════════ WEBSITE DDOS ATTACK SIMULATOR ════════════█❚")
            print("═══════════════════════════════════════════════════════════")
            wb = input("Masukkan Url Website Target : ")
            pkg = int(input("Masukkan Jumlah Serangan    : "))
            print("═══════════════════════════════════════════════════════════")
            for i in range(3):
                time.sleep(1)
            mulai = str(input("Mulai Serangan?(Y/N) : "))
            if mulai == 'Y' or mulai == 'y':
                for i in range(3):
                    time.sleep(1)
                for i in range(pkg):
                    print(colored(f"Serangan Dikirimkan Menuju {wb} Sebanyak {i+1} Serangan", "red"))
                print()
                print("═══════════════════════════════════════════════════════════")
                for i in range(5):
                    time.sleep(0.1)
                lanjut = """Tekan [Enter] Untuk Melanjutkan....."""
                for i in lanjut:
                    print(i, end="", flush=True)
                    time.sleep(0.03)
                input()
                ddos()
            if mulai == 'N' or mulai == 'n':
                ddos()

        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═══════════════════════════════════════════════════")
        print("❚█════════════ DDOS ATTACK SIMULATOR ════════════█❚")
        print("═══════════════════════════════════════════════════")
        print("1. DDOS ATTACK MENGGUNAKAN IP")
        print("2. DDOS ATTACK MENGGUNAKAN URL WEBSITE")
        print("3. KELUAR")
        print("═══════════════════════════════════════════════════")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            ip()
        if pilih == 2:
            web()
        if pilih == 3:
            rendem()
        if pilih > 3:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            ddos()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            ddos()

    def umur():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("════════════════════════════════════════════")
        print("❚█════════════ TOOLS CEK UMUR ════════════█❚")
        print("════════════════════════════════════════════")
        tgl = int(input("Masukkan Tanggal Lahir : "))
        bln = int(input("Masukkan Bulan Lahir   : "))
        thn = int(input("Masukkan Tahun Lahir   : "))
        print("════════════════════════════════════════════")
        def calculate_usia(lahir):
            current_date = datetime.now()
            usia = current_date - lahir
            thnn = usia.days // 365
            blnn = (usia.days % 365) // 30
            tgll = (usia.days % 365) % 30

            return thnn, blnn, tgll

        lahir = datetime(thn, bln, tgl)
        thnn, blnn, tgll = calculate_usia(lahir)
        
        print()
        print(f"Usia Anda Saat Ini : {thnn} Tahun, {blnn} Bulan, {tgll} Hari")
        print()
        print("════════════════════════════════════════════")
        for i in range(2):
            time.sleep(1)
        lnjt = str(input("Ingin Melanjutkan?(Y/N) : "))
        if lnjt == 'y' or lnjt == 'Y':
            umur()
        if lnjt == 'n' or lnjt == 'N':
            rendem()

    def kalen():
        def bulan():
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("════════════════════════════════════════════════════")
            print("❚█════════════ TOOLS KALENDER (BULAN) ════════════█❚")
            print("════════════════════════════════════════════════════")
            bln = int(input("Masukkan Bulan   : "))
            thn = int(input("Masukkan Tahun   : "))
            print("════════════════════════════════════════════════════")
            if bln > 12 or bln == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                bulan()
            if thn == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                bulan()
            print()
            kalender = (calendar.month(thn, bln))
            for i in kalender:
                print(i, end="", flush=True)
                time.sleep(0.02)
            print()
            print("════════════════════════════════════════════════════")
            for i in range(2):
                time.sleep(0.05)
            lnjt = str(input("Ingin Melanjutkan?(Y/N) : "))
            if lnjt == 'y' or lnjt == 'Y':
                bulan()
            if lnjt == 'n' or lnjt == 'N':
                kalen()

        def tahun():
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(2):
                time.sleep(0.02)
            print("════════════════════════════════════════════════════════════════════════════")
            print("❚█════════════════════════ TOOLS KALENDER (TAHUN) ════════════════════════█❚")
            print("════════════════════════════════════════════════════════════════════════════")
            thn = int(input("Masukkan Tahun   : "))
            print("════════════════════════════════════════════════════════════════════════════")
            if thn == 0:
                unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
                for i in unknow:
                    print(i, end="", flush=True)
                    time.sleep(0.02)
                input()
                for i in range(5):
                    time.sleep(0.01)
                tahun()
            print()
            kalender = (calendar.calendar(thn))
            for i in kalender:
                print(i, end="", flush=True)
                time.sleep(0.01)
            print()
            print("════════════════════════════════════════════════════════════════════════════")
            for i in range(2):
                time.sleep(0.05)
            lnjt = str(input("Ingin Melanjutkan?(Y/N) : "))
            if lnjt == 'y' or lnjt == 'Y':
                tahun()
            if lnjt == 'n' or lnjt == 'N':
                kalen()

        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("══════════════════════════════════════")
        print("❚█════════════ KALENDER ════════════█❚")
        print("══════════════════════════════════════")
        print("1. KALENDER (BULAN)")
        print("2. KALENDER (TAHUN)")
        print("3. KELUAR")
        print("══════════════════════════════════════")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1:
            bulan()
        if pilih == 2:
            tahun()
        if pilih == 3:
            rendem()
        if pilih > 3:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            kalen()
        if pilih == 0:
            unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
            for i in unknow:
                print(i, end="", flush=True)
                time.sleep(0.02)
            input()
            for i in range(5):
                time.sleep(0.01)
            kalen()

    def kabisat():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("═══════════════════════════════════════════════")
        print("❚█════════════ CEK TAHUN KABISAT ════════════█❚")
        print("═══════════════════════════════════════════════")
        tahun = int(input("Masukkan Tahun : "))
        if tahun % 4 != 0:
            print(f'{tahun} Bukan Tahun Kabisat')
        else:
            if tahun % 100 == 0:
                print(f'{tahun} Bukan Tahun Kabisat')
            else:
                print(f'{tahun} Merupakan Tahun Kabisat')
        print("═══════════════════════════════════════════════")
        for i in range(2):
            time.sleep(1)
        lnjt = str(input("Ingin Melanjutkan?(Y/N) : "))
        if lnjt == 'y' or lnjt == 'Y':
            kabisat()
        if lnjt == 'n' or lnjt == 'N':
            rendem()

    def GanjilGenap():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(2):
            time.sleep(0.02)
        print("══════════════════════════════════════════════")
        print("❚█════════════ CEK GANJIL/GENAP ════════════█❚")
        print("══════════════════════════════════════════════")
        bil = int(input("Masukkan Bilangan : "))
        if bil % 2 == 0:
            print(f'{bil} Merupakan Bilangan Genap')
        else:
            print(f'{bil} Merupakan Bilangan Ganjil')
        print("══════════════════════════════════════════════")
        for i in range(2):
            time.sleep(1)
        lnjt = str(input("Ingin Melanjutkan?(Y/N) : "))
        if lnjt == 'y' or lnjt == 'Y':
            GanjilGenap()
        if lnjt == 'n' or lnjt == 'N':
            rendem()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("══════════════════════════════════════════════")
    print("❚█══════════════ TOOLS RANDOM ══════════════█❚")
    print("══════════════════════════════════════════════")
    print("1. KALKULATOR CINTA")
    print("2. TEXT TO VOICE")
    print("3. TEXT TO ASCII")
    print("4. DDOS ATTACK SIMULATOR")
    print("5. CEK UMUR")
    print("6. KALENDER")
    print("7. CEK TAHUN KABISAT")
    print("8. CEK BILANGAN GANJIL/GENAP")
    print("9. KELUAR")
    print("══════════════════════════════════════════════")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        cinta()
    if pilih == 2:
        textvoice()
    if pilih == 3:
        textasci()
    if pilih == 4:
        ddos()
    if pilih == 5:
        umur()
    if pilih == 6:
        kalen()
    if pilih == 7:
        kabisat()
    if pilih == 8:
        GanjilGenap()
    if pilih == 9:
        menu()
    if pilih > 9:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        rendem()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        rendem()

def credit():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2):
        time.sleep(0.02)
    print("═════════════════════════════════════════════════")
    print("❚█══════════════════ CREDITS ══════════════════█❚")
    print("═════════════════════════════════════════════════")
    for i in range(2):
        time.sleep(1)
    balik = """
>>>>> Sosok Dibalik PyTools 
Suryo Saputro : Developer
Alzhar Chandraditya Dewandra : Pembuat Proposal
Mukti Widodo, S.T : Motivator

>>>>> Inspirasi PyTools
Kami membuat PyTools ini bukan ke tanpasengajaan.
Kami membuat PyTools ini terinspirasi dari slogan
Wali Kelas kami Bapak Mukti Widodo, S.T yaitu
"Berbeda Dari Yang Beda"
Jujur saja, saat kami menerima perintah dari
pak Mukti untuk membuat aplikasi command line
python untuk projek akhir semester kami sempat
merasa bingung, tapi akhirnya kami teringat
dengan slogan dari pak Mukti tersebut dan 
akhirnya kami pun ter motivasi.

>>>>> Penjelasan PyTools
Tools ini dibuat dengan penuh perasaan dan niat
dan juga diimbangi dengan doa agar disaat proses
pembuatan kami tidak stress maupun tumbang. Tujuan
dibuatnya PyTools yaitu untuk mengisi waktu luang
sang pengguna dan juga memudahkan pengguna untuk
mencari beberapa pengetahuan baru.

>>>>> Module/Packages Yang Harus Diinstal
Sebelum menggunakan PyTools ini, pengguna diwajibkan
menginstal beberapa module/packages terlebih dahulu. 
Entah itu pengguna Windows, Linux, atau MacOS. Berikut 
beberapa module/packages yang harus diinstal :

    -pip
    -pyfiglet
    -termcolor
    -qrcode
    -gtts

Untuk pip kalian bisa download di Google untuk pengguna 
Windows dan MacOS, sedangkan untuk pengguna Linux bisa 
menggunakan perintah berikut :

    $ sudo su 
    $ apt install pip
    $ pip install pyfiglet
    $ pip install termcolor
    $ pip install qrcode
    $ pip install gtts


Dan untuk module/packages lainnya bisa diinstall melalui 
pip di command prompt bawaan masing-masing OS. Memang
terkesan ribet, tapi percayalah hasil terbaik berasal
dari proses yang rumit.

>>>>> Contact
** Suryo Saputro **
Instagram : www39.srysptr.go.blok
WhatsApp  : 081945327691
Email     : suryo237658@student.smkn1kandeman.sch.id

** Alzhar Chandaditya Dewandra **
Instagram : zhrchndradtyad
WhatsApp  : 082324308225
Email     : alzhar237631@student.smkn1kandeman.sch.id

©Copyright By X PPLG 1 - 2024"""
    for i in balik:
        print(i, end="", flush=True)
        time.sleep(0.02)
    print()
    print()
    print("═════════════════════════════════════════════════")
    for i in range(2):
        time.sleep(1)
    lnjt = str(input("Ingin Melanjutkan?(Y/N) : "))
    if lnjt == 'y' or lnjt == 'Y':
        menu()
    if lnjt == 'n' or lnjt == 'N':
        credit()

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(3):
        time.sleep(0.1)
    print("❚█","═" * 60,"█❚")
    for i in range(3):
        time.sleep(0.1)
    f = Figlet(font='cyberlarge')
    ascii_art = f.renderText(' PyTools')
    print(ascii_art)
    for i in range(3):
        time.sleep(0.1)
    print("❚█","═" * 60,"█❚")
    for i in range(3):
        time.sleep(0.1)
    print("1. TOOLS SEKOLAH")
    print("2. TOOLS KEJAWEN")
    print("3. TOOLS ZODIAK")
    print("4. GAME")
    print("5. GENERATOR TOOLS")
    print("6. RANDOM TOOLS")
    print("7. CREDITS")
    print("8. KELUAR")
    print("❚█","═" * 60,"█❚")
    for i in range(3):
        time.sleep(0.1)
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1:
        sekolah()
    if pilih == 2:
        kejawen()
    if pilih == 3:
        zodiak()
    if pilih == 4:
        game()
    if pilih == 5:
        generator()
    if pilih == 6:
        rendem()
    if pilih == 7:
        credit()
    if pilih == 8:
        print("❚█","═" * 60,"█❚")
        for i in range(2):
            time.sleep(1)
        lnjt = str(input("Yakin Ingin Keluar?(Y/N) : "))
        if lnjt == 'y' or lnjt == 'Y':
            thanks = """
Terimakasih karena sudah menggunakan PyTools. Mohon maaf
jika aplikasi PyTools ini kurang memuaskan. Semoga hari-hari
anda menyenangkan dan semoga anda selalu beruntung. Dan jangan
lupa untuk selalu tampil berdeda dari yang beda!"""
            for i in thanks:
                print(i, end="", flush=True)
                time.sleep(0.03)
            for i in range(3):
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(3):
                time.sleep(0.01)
            exit()
        if lnjt == 'n' or lnjt == 'N':
            menu()
    if pilih > 8:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        menu()
    if pilih == 0:
        unknow = """Perintah tidak diketahui, Tekan [Enter] untuk melanjutkan....."""
        for i in unknow:
            print(i, end="", flush=True)
            time.sleep(0.02)
        input()
        for i in range(5):
            time.sleep(0.01)
        menu()

menu()