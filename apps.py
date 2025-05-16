import streamlit as st

st.set_page_config(page_title="Bunga untuk Kamu", page_icon="🌸", layout="centered")

st.markdown("<h1 style='text-align: center; color: pink;'>🌸 Bunga Ini Untuk Kamu 🌸</h1>", unsafe_allow_html=True)

st.write("Bunga ini mekar hanya untukmu, menggambarkan rasa sayangku yang terus tumbuh setiap hari.")

# Menampilkan gambar bunga pink dari URL
image_url = "https://cdn.pixabay.com/photo/2017/03/27/14/56/pink-rose-2178660_1280.jpg"
st.image(image_url, caption="Mawar pink yang indah untukmu 💖", use_column_width=True)

st.caption("Dibuat dengan sepenuh hati oleh Felix 💕")
