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
    Aplikasi ini berfungsi untuk menghitung estimasi kebutuhan kalori harian berdasarkan
    umur, jenis kelamin, berat badan, tinggi badan, dan tingkat aktivitas seseorang.
    Selain itu, aplikasi ini juga memberikan saran tentang seberapa banyak konsumsi gula
    yang ideal, berdasarkan persentase dari total kebutuhan kalori harian.
    
    Tujuan utama aplikasi ini adalah untuk membantu kamu menjaga pola makan sehat! 🍎🍏
    """)

def tampilkan_pengenalan_kelompok():
    st.header("Pengenalan Kelompok 👩‍💻👨‍💻")
    st.write("""
    Aplikasi ini dikembangkan oleh kelompok yang terdiri dari:

    - **Nama 1**: Pengembang utama 💻
    - **Nama 2**: Desain UI/UX 🎨
    - **Nama 3**: Pengujian dan Dokumentasi 📝

    Kami bertujuan untuk membantu orang-orang menjaga pola makan sehat dengan memberikan
    informasi yang jelas dan akurat tentang konsumsi kalori dan gula. ✨
    """)

def main():
    # Set the background color to blue and text to white
    st.markdown("""
        <style>
        .reportview-container {
            background-color: #1E3A8A;  /* Blue background */
            color: white;               /* White text */
        }
        .sidebar .sidebar-content {
            background-color: #1E3A8A;  /* Blue sidebar */
            color: white;               /* White text in sidebar */
        }
        .block-container {
            background-color: white;
            color: black;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3, h4, h5, h6 {
            color: white;  /* White text for all headers */
        }
        .css-18e3th9 {
            color: white;  /* White color for other text elements */
        }
        </style>
        """, unsafe_allow_html=True)

    # Title with a fun emoji
    st.title("Kalkulator Kebutuhan Gula Harian 🍭")

    # Sidebar menu with some fun emojis
    menu = st.sidebar.radio("Pilih Menu 🤔", ["Kalkulator Kebutuhan Kalori 🧮", "Tentang Aplikasi 🌞", "Pengenalan Kelompok 👩‍💻👨‍💻"])

    # Section for Kalkulator with white background
    if menu == "Kalkulator Kebutuhan Kalori 🧮":
        # Apply white background for the calculator section
        st.markdown("""
            <style>
            .block-container {
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            </style>
            """, unsafe_allow_html=True)

        # Kalkulator Kebutuhan Kalori
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
            gula_maks_10 = kebutuhan_kalori * 0.10 / 4  # 4 kalori per gram gula
            gula_ideal_5 = kebutuhan_kalori * 0.05 / 4

            st.success(f"Estimasi kebutuhan kalori: {kebutuhan_kalori:.0f} kkal/hari 💪")
            st.info(f"Konsumsi gula maksimal (10% energi): {gula_maks_10:.1f} gram/hari 🍭")
            st.info(f"Saran konsumsi ideal (5% energi): {gula_ideal_5:.1f} gram/hari 🍬")
    
    elif menu == "Tentang Aplikasi 🌞":
        tampilkan_tentang_aplikasi()
    
    elif menu == "Pengenalan Kelompok 👩‍💻👨‍💻":
        tampilkan_pengenalan_kelompok()

if __name__ == "__main__":
    main()
