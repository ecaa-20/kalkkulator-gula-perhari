# simpan sebagai app.py
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

def main():
    st.title("Kalkulator Kebutuhan Gula Harian")

    umur = st.number_input("Umur (tahun)", min_value=1, max_value=100, value=25)
    tb = st.number_input("Tinggi Badan (cm)", min_value=50, max_value=250, value=170)
    bb = st.number_input("Berat Badan (kg)", min_value=10, max_value=200, value=65)
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
    aktivitas = st.selectbox("Tingkat Aktivitas", [
        "Sedentari (minim aktivitas)",
        "Ringan (olahraga ringan)",
        "Sedang (olahraga 3-5 hari/minggu)",
        "Berat (olahraga intens)"
    ])

    if st.button("Hitung Kebutuhan Gula"):
        kebutuhan_kalori = hitung_kebutuhan_kalori(umur, tb, bb, jenis_kelamin, aktivitas)
        gula_maks_10 = kebutuhan_kalori * 0.10 / 4  # 4 kalori per gram gula
        gula_ideal_5 = kebutuhan_kalori * 0.05 / 4

        st.success(f"Estimasi kebutuhan kalori: {kebutuhan_kalori:.0f} kkal/hari")
        st.info(f"Konsumsi gula maksimal (10% energi): {gula_maks_10:.1f} gram/hari")
        st.info(f"Saran konsumsi ideal (5% energi): {gula_ideal_5:.1f} gram/hari")

if __name__ == "__main__":
    main()
