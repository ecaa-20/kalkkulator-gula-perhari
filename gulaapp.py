import streamlit as st

def hitung_kebutuhan_kalori(umur, tb, bb, jenis_kelamin, aktivitas):
    if jenis_kelamin == "Pria":
        bmr = 66 + (13.7 * bb) + (5 * tb) - (6.8 * umur)
    else:
        bmr = 655 + (9.6 * bb) + (1.8 * tb) - (4.7 * umur)

    faktor_aktivitas = {
        "Sedentari (minim aktivitas)": 1.2,
        "Ringan (olahraga ringan)": 1.375,
        "Sedang (olahraga 3-5 hari/minggu)": 1.55,
        "Berat (olahraga intens)": 1.725,
    }

    return bmr * faktor_aktivitas[aktivitas]

def tampilkan_tentang_aplikasi():
    st.header("Tentang Aplikasi 🌞")
    st.write("""
    Aplikasi ini membantu menghitung kebutuhan kalori dan konsumsi gula ideal berdasarkan
    data pribadi dan tingkat aktivitas harian. Cocok untuk kamu yang ingin hidup lebih sehat! 🍏💪
    Meningkatkan Kesadaran Gizi dan Pola Makan Sehat. Banyak orang belum menyadari berapa banyak gula yang mereka konsumsi setiap hari. 
     Aplikasi ini membantu pengguna memahami batas konsumsi gula maksimal dan ideal berdasarkan kondisi tubuh dan aktivitas mereka.

Kalkulator kebutuhan gula harian adalah alat (bisa berupa aplikasi, situs web, atau tabel manual) yang digunakan untuk memperkirakan berapa banyak gula tambahan yang dapat dikonsumsi seseorang dalam sehari tanpa membahayakan kesehatan, berdasarkan faktor-faktor seperti:
- Usia 🎂
- Jenis kelamin 👦👧
- Berat badan ⚖️
- Tinggi badan 📏
- Tingkat aktivitas fisik 🏃

Gula tambahan sebaiknya tidak lebih dari 10% dari total kalori harian (lebih ideal jika di bawah 5%). Misalnya, jika kebutuhan kalori harian seseorang adalah 2000 kkal, maka:
- 10% dari 2000 kkal = 200 kkal = sekitar 50 gram gula tambahan per hari. 🍫
- 5% dari 2000 kkal = 100 kkal = sekitar 25 gram gula tambahan per hari. 🧁
    """)

def tampilkan_pengenalan_kelompok():
    st.header("Pengenalan Kelompok 👩‍💻👨‍💻")
    st.write("""
    Aplikasi ini dikembangkan oleh kelompok 12:

    - *Allysia Rahma Putri*: 2420570  🐈
    - *I Gede Hilmi Krisna Hadinata*: 2420604 🐔
    - *Khaesa Shafa Nuraini*: 2420608 🐼
    - *Pramudya Bayu Perkasa*: 2420640  🐆
    - *Rahmawati Syafitri*: 2420645 🦓

    
   Kelompok Kami hadir untuk membantu kamu lebih peduli terhadap pola makan! 😄
    """)
    
def main():
    # Styling for whole app + kalkulator pink background
    st.markdown("""
        <style>
        /* Background putih dan teks hitam untuk seluruh aplikasi */
        .reportview-container, .main, .sidebar .sidebar-content {
            background-color: #1E3A8A;
            color: black;
        }

        /* Header dan teks umum putih */
        h1, h2, h3, h4, h5, h6, p, label, .css-1cpxqw2, .css-qrbaxs {
            color: red !important;
        }

        /* Kalkulator section: hitam dengan teks putih */
        .kalkulator-container {
            background-color: #000000; /* Hitam */
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Ubah input label dan tulisan dalam kalkulator */
        .kalkulator-container label, .kalkulator-container span, .kalkulator-container p {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Kalkulator Kebutuhan Gula Harian 🍭")

    menu = st.sidebar.radio("Pilih Menu 🤔", ["Kalkulator Kebutuhan Gula 🧮", "Tentang Aplikasi 🌞", "Pengenalan Kelompok 👩‍💻👨‍💻"])

    if menu == "Kalkulator Kebutuhan Gula 🧮":
        st.markdown('<div class="kalkulator-container">', unsafe_allow_html=True)

        umur = st.number_input("Umur (tahun) 🎂", min_value=1, max_value=100, value=25)
        tb = st.number_input("Tinggi Badan (cm) 📏", min_value=50, max_value=250, value=170)
        bb = st.number_input("Berat Badan (kg) ⚖️", min_value=10, max_value=200, value=65)
        jenis_kelamin = st.selectbox("Jenis Kelamin 👦👧", ["Pria", "Wanita"])
        aktivitas = st.selectbox("Tingkat Aktivitas 🏃", [
            "Sedentari (minim aktivitas)",
            "Ringan (olahraga ringan)",
            "Sedang (olahraga 3-5 hari/minggu)",
            "Berat (olahraga intens)"
        ])

        if st.button("Hitung Kebutuhan Gula 🍬"):
            kebutuhan_kalori = hitung_kebutuhan_kalori(umur, tb, bb, jenis_kelamin, aktivitas)
            gula_maks_10 = kebutuhan_kalori * 0.10 / 4
            gula_ideal_5 = kebutuhan_kalori * 0.05 / 4

            st.success(f"Estimasi kebutuhan kalori: {kebutuhan_kalori:.0f} kkal/hari 💪")
            st.info(f"Konsumsi gula maksimal (10% energi): {gula_maks_10:.1f} gram/hari 🍭")
            st.info(f"Saran konsumsi ideal (5% energi): {gula_ideal_5:.1f} gram/hari 🍬")
            st.success(f"saran dan contoh makanan rendah gula beserta kandungan gula nya :") 
            (f"sayuran hijau(brokoli,bayam,selada)🥬🥦 : <1 gram/100 gram")
            (f"telur : 0 gram")
            (f"Greek Yogurt Plain (tanpa pemanis)🍦 : 3–4 gram per 100 gram (laktosa alami)")
            (f"tahu dan tempe : <1 gram/100 gram")
            (f"buah : avokad 🥑(0,2 gram), tomat🍅 (2,6 gram), strawberry 🍓(4,9 gram), belimbing (3,6 gram), raspberry🫐(4,4 gram)")
        
        st.markdown('</div>', unsafe_allow_html=True)

    elif menu == "Tentang Aplikasi 🌞":
        tampilkan_tentang_aplikasi()

    elif menu == "Pengenalan Kelompok 👩‍💻👨‍💻":
        tampilkan_pengenalan_kelompok()

if __name__ == "__main__":
    main()
