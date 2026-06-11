import streamlit as st

st.set_page_config(
    page_title="AgriDetect",
    page_icon="🌱",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(90deg, #a8d66d, #ffffff);
}
.main-title {
    text-align: center;
    color: #005500;
    font-size: 42px;
    font-weight: bold;
}
.sub-title {
    text-align: center;
    color: #005500;
    font-size: 20px;
    font-weight: bold;
}
.desc-box {
    background-color: #e9f8e9;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #8bc34a;
    font-size: 18px;
}
.result-card {
    background-color: #eaffea;
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #008000;
    margin-top: 15px;
}
.stButton > button {
    background-color: #005500;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 25px;
}
</style>
""", unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state.page = "home"

if "hasil" not in st.session_state:
    st.session_state.hasil = []


rules = {
    "Busuk Lunak Bakteri (Erwinia)": ["daun menghitam", "tanaman layu"],
    "Bercak Daun Cercospora": ["daun menguning", "bercak coklat"],
    "Hama Ulat Grayak": ["daun keriting", "pertumbuhan terhambat", "daun berlubang"],
    "Hama Kutu Daun (Aphids)": ["daun menguning", "daun keriting", "daun menggulung", "pertumbuhan terhambat"],
    "Kekurangan Air": ["tanaman layu", "daun mengering"],
    "Kekurangan Nitrogen": ["daun menguning", "pertumbuhan terhambat"],
    "Serangan Jamur Daun": ["bercak hitam", "daun menguning"],
    "Busuk Akar": ["tanaman layu", "daun menguning", "pertumbuhan terhambat"]
}

penyakit_data = {
    "Bercak Daun Cercospora": {
        "penyebab": "Jamur Cercospora longissima.",
        "solusi": "- Petik daun yang berbercak coklat.\n- Atur jarak tanam.\n- Semprot fungisida hayati."
    },
    "Busuk Akar": {
        "penyebab": "Akar terserang jamur atau bakteri karena genangan air.",
        "solusi": "- Perbaiki drainase.\n- Kurangi penyiraman berlebih.\n- Gunakan fungisida."
    },
    "Busuk Lunak Bakteri (Erwinia)": {
        "penyebab": "Bakteri Erwinia carotovora.",
        "solusi": "- Cabut tanaman yang membusuk.\n- Hindari penyiraman berlebihan.\n- Pastikan drainase baik."
    },
    "Hama Kutu Daun (Aphids)": {
        "penyebab": "Kutu hijau atau hitam kecil.",
        "solusi": "- Pasang perangkap lem kuning.\n- Semprot tanaman dengan air.\n- Gunakan larutan sabun organik."
    },
    "Hama Ulat Grayak": {
        "penyebab": "Larva atau ulat Spodoptera litura.",
        "solusi": "- Ambil ulat secara manual.\n- Pasang jaring pelindung.\n- Gunakan insektisida nabati."
    },
    "Kekurangan Air": {
        "penyebab": "Tanaman kekurangan air atau penyiraman tidak teratur.",
        "solusi": "- Siram tanaman rutin.\n- Jaga kelembapan tanah.\n- Kurangi paparan panas berlebih."
    },
    "Kekurangan Nitrogen": {
        "penyebab": "Tanaman kekurangan unsur nitrogen.",
        "solusi": "- Berikan pupuk nitrogen.\n- Perbaiki media tanam.\n- Lakukan pemupukan rutin."
    },
    "Serangan Jamur Daun": {
        "penyebab": "Infeksi jamur pada daun akibat kelembapan tinggi.",
        "solusi": "- Gunakan fungisida.\n- Buang daun yang terinfeksi.\n- Kurangi kelembapan."
    }
}


def halaman_awal():
    st.markdown('<div class="main-title">🌱 AgriDetect</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Sistem Pakar Deteksi Penyakit Tanaman Selada</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class="desc-box">
    Aplikasi ini digunakan untuk membantu mendeteksi penyakit pada tanaman selada
    berdasarkan gejala yang dipilih pengguna menggunakan metode Forward Chaining.
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("### Fitur Aplikasi")
    st.write("- Deteksi penyakit tanaman selada")
    st.write("- Menampilkan penyebab penyakit")
    st.write("- Menampilkan solusi penanganan")
    st.write("- Menggunakan metode Forward Chaining")

    st.write("")
    if st.button("Mulai Diagnosa"):
        st.session_state.page = "deteksi"
        st.rerun()


def halaman_deteksi():
    st.markdown('<div class="main-title">🌱 AgriDetect</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Pilih Gejala Tanaman</div>', unsafe_allow_html=True)

    st.info("Pilih gejala tanaman, lalu tekan tombol PROSES DETEKSI.")

    gejala_terpilih = []

    st.subheader("Perubahan Warna Daun")
    if st.checkbox("Tidak ada perubahan warna"):
        gejala_terpilih.append("tidak ada perubahan warna")
    if st.checkbox("Daun menguning"):
        gejala_terpilih.append("daun menguning")
    if st.checkbox("Daun menghitam"):
        gejala_terpilih.append("daun menghitam")
    if st.checkbox("Daun mengering"):
        gejala_terpilih.append("daun mengering")

    st.subheader("Bercak Pada Daun")
    if st.checkbox("Tidak ada bercak"):
        gejala_terpilih.append("tidak ada bercak")
    if st.checkbox("Bercak coklat"):
        gejala_terpilih.append("bercak coklat")
    if st.checkbox("Bercak hitam"):
        gejala_terpilih.append("bercak hitam")
    if st.checkbox("Bercak kuning"):
        gejala_terpilih.append("bercak kuning")

    st.subheader("Kondisi Daun")
    if st.checkbox("Daun normal"):
        gejala_terpilih.append("daun normal")
    if st.checkbox("Tanaman layu"):
        gejala_terpilih.append("tanaman layu")
    if st.checkbox("Daun keriting"):
        gejala_terpilih.append("daun keriting")
    if st.checkbox("Daun menggulung"):
        gejala_terpilih.append("daun menggulung")

    st.subheader("Pertumbuhan")
    if st.checkbox("Pertumbuhan normal"):
        gejala_terpilih.append("pertumbuhan normal")
    if st.checkbox("Pertumbuhan terhambat"):
        gejala_terpilih.append("pertumbuhan terhambat")

    st.subheader("Kerusakan Fisik")
    if st.checkbox("Daun berlubang"):
        gejala_terpilih.append("daun berlubang")
    if st.checkbox("Tepi daun kering"):
        gejala_terpilih.append("tepi daun kering")

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("PROSES DETEKSI"):
            if not gejala_terpilih:
                st.warning("Data belum lengkap! Silakan pilih gejala terlebih dahulu.")
            else:
                hasil = []

                for penyakit, daftar_gejala in rules.items():
                    if set(daftar_gejala).issubset(set(gejala_terpilih)):
                        hasil.append(penyakit)

                st.session_state.hasil = hasil
                st.session_state.page = "hasil"
                st.rerun()

    with col2:
        if st.button("Menu Utama"):
            st.session_state.page = "home"
            st.rerun()


def halaman_hasil():
    st.markdown('<div class="main-title">Hasil Deteksi Penyakit</div>', unsafe_allow_html=True)

    hasil = st.session_state.hasil

    if not hasil:
        st.warning("Penyakit tidak ditemukan berdasarkan gejala yang dipilih.")
    else:
        st.success("Hasil Deteksi Penyakit Ditemukan")

        for penyakit in hasil:
            data = penyakit_data[penyakit]

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader(f"🌿 {penyakit}")

            st.write("**Penyebab Penyakit:**")
            st.write(data["penyebab"])

            st.write("**Solusi Penanganan:**")
            st.write(data["solusi"])

            st.write("**Tingkat Kecocokan:** 100%")
            st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Diagnosis Ulang"):
            st.session_state.hasil = []
            st.session_state.page = "deteksi"
            st.rerun()

    with col2:
        if st.button("Menu Utama"):
            st.session_state.hasil = []
            st.session_state.page = "home"
            st.rerun()


if st.session_state.page == "home":
    halaman_awal()
elif st.session_state.page == "deteksi":
    halaman_deteksi()
elif st.session_state.page == "hasil":
    halaman_hasil()

st.write("---")
st.caption("AgriDetect | Sistem Pakar Tanaman Selada | Metode Forward Chaining")