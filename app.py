import streamlit as st

st.set_page_config(
    page_title="AgriDetect",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AgriDetect")
st.subheader("Deteksi Penyakit Tanaman Selada")

st.write("Pilih gejala yang sesuai dengan kondisi tanaman.")

gejala = []

if st.checkbox("Daun menguning"):
    gejala.append("daun menguning")

if st.checkbox("Daun menghitam"):
    gejala.append("daun menghitam")

if st.checkbox("Daun mengering"):
    gejala.append("daun mengering")

if st.checkbox("Tanaman layu"):
    gejala.append("tanaman layu")

if st.checkbox("Daun menggulung"):
    gejala.append("daun menggulung")

if st.checkbox("Daun berlubang"):
    gejala.append("daun berlubang")

if st.button("PROSES DETEKSI"):

    if len(gejala) == 0:
        st.error("Silakan pilih gejala terlebih dahulu")

    elif "daun menghitam" in gejala and "tanaman layu" in gejala:
        st.success("Penyakit Terdeteksi: Busuk Lunak Bakteri")

        st.write("### Penyebab")
        st.write("Bakteri Erwinia carotovora")

        st.write("### Solusi")
        st.write("Kurangi kelembapan dan buang tanaman yang terinfeksi")

    elif "daun berlubang" in gejala:
        st.success("Penyakit Terdeteksi: Serangan Ulat")

        st.write("### Penyebab")
        st.write("Hama ulat pemakan daun")

        st.write("### Solusi")
        st.write("Gunakan insektisida sesuai dosis")

    else:
        st.warning("Penyakit tidak ditemukan")