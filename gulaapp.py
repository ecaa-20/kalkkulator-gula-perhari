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
            color: pink !important;
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
            st.info(f"Berikut adalah rincian estimasi kandungan gula alami dan tambahan (jika ada) dalam setiap makanan/minuman pada contoh menu sehari rendah gula tadi:
- Sarapan
1. Oatmeal dengan pisang & kayu manis; Gula alami dari pisang (1/2 buah): ± 6–7 gram
        Oatmeal tanpa gula: 0 gram
        Kayu manis: 0 gram

2. Telur rebus
0 gram gula
3. Teh hijau tanpa gula
0 gram gula

Total gula sarapan: ± 6–7 gram (alami, bukan tambahan)
---

Snack Pagi
1. Apel (ukuran sedang)
Gula alami: ± 19 gram
2. Segenggam kacang almond (sekitar 28 gram)
0 gram gula (jika tanpa tambahan)
Total gula snack pagi: ± 19 gram

Makan Siang:
1. Nasi merah (150 gram)
Gula alami dari karbohidrat kompleks: ± 0–1 gram
2. Ayam panggang tanpa kulit
0 gram gula
3. Tumis bayam & wortel
Wortel: ± 2–3 gram gula alami per 1/2 cangkir
Bayam: <1 gram

Total gula makan siang: ± 3–4 gram
---

Snack Sore
1. Yogurt plain tanpa pemanis (150 ml)
Gula alami dari laktosa: ± 5–6 gram
Tambahan buah segar (misal 2 potong stroberi): ± 1 gram

Total gula snack sore: ± 6–7 gram
---

Makan Malam
1. Sup sayur (wortel, buncis, tahu)
Wortel & buncis: ± 3 gram gula alami
Tahu: <1 gram gula
2. Tempe panggang
± 1–2 gram gula alami dari fermentasi kedelai
3. Nasi merah (opsional, 100 gram)
± <1 gram

Total gula makan malam: ± 5–6 gram
---
Total Estimasi Gula Sehari: ± 39–43 gram")

        st.markdown('</div>', unsafe_allow_html=True)

    elif menu == "Tentang Aplikasi 🌞":
        tampilkan_tentang_aplikasi()

    elif menu == "Pengenalan Kelompok 👩‍💻👨‍💻":
        tampilkan_pengenalan_kelompok()

if __name__ == "__main__":
    main()
