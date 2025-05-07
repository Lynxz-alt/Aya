import streamlit as st
import random

# HARUS di atas
st.set_page_config(page_title="Aya Celestia 💖", page_icon="🌸", layout="centered")

# CSS untuk nuansa manis & lembut
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Handlee&family=Quicksand:wght@400;600&display=swap');

html, body, .stApp {
    background-color: #fff0f5;
    font-family: 'Quicksand', sans-serif;
    color: #3f2b2b;
}

h1, h3 {
    font-family: 'Handlee', cursive;
    text-align: center;
    color: #d63384;
}

p {
    text-align: center;
}

.heart {
    text-align: center;
    font-size: 32px;
    margin-top: 10px;
    animation: pulse 1.5s infinite;
    color: #ff69b4;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.15); }
  100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Judul utama
st.markdown("<h1>Hai Aya Celestia! 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p>Cuma ingin bikin kamu senyum sebentar hari ini 💖</p>", unsafe_allow_html=True)

# Nama
name = st.text_input("Tulis nama kamu di sini 😚")
if name:
    st.success(f"Halo {name}! Kamu cantik banget hari ini 😍")

# Tombol pujian
if st.button("Klik untuk dapat pujian 💌"):
    compliments = [
        "Kamu seperti matahari pagi, selalu membawa semangat 🌞",
        "Tawa kamu menular banget, bikin hati hangat 💕",
        "Setiap hari jadi lebih indah kalau ada kamu 🫶",
        "Kamu itu kayak lagu favorit, nggak pernah bosen didengerin 🎵",
        "Lucunya kamu tuh nggak ada obat 🐰"
    ]
    st.info(random.choice(compliments))

# Ilustrasi hati
st.markdown("<div class='heart'>💗 💖 💞 💕 💘</div>", unsafe_allow_html=True)

# Kotak Pesan ke Felix
st.markdown("### ✉️ Kirim Pesan ke Felix")
msg = st.text_input("Mau nitip pesan ke Felix?")
if msg:
    st.success("Hehe noted~ Felix pasti baca 😎🫶")

# Surat dari Felix (TIDAK langsung terbuka)
with st.expander("📜 Buka surat dari Felix"):
    st.markdown("""
    Dear Aya,

    Kamu itu seperti senja yang selalu dinanti.  
    Kehadiranmu bikin semuanya terasa hangat dan nyaman.  
    Aku cuma pengin bilang satu hal:  
    Aku seneng banget kenal kamu 🥹  

    🌸 Salam hangat,  
    Felix
    """)

# Fun Fact
st.markdown("### 🐣 Fun Fact Tentang Felix")
facts = [
    "Suka banget nasi goreng jam 11 malam 🍛",
    "Nggak bisa minum kopi tapi sok ngopi ☕",
    "Pernah nulis puisi, terus malu sendiri 🙈"
]
if st.button("Fun Fact Hari Ini"):
    st.info(random.choice(facts))

# Hadiah
if st.button("Buka hadiah dari Felix 🎁"):
    st.balloons()
    st.success("Kamu dapet peluk virtual terhangat hari ini 🤗💗")
