import streamlit as st
import random

# WAJIB PALING ATAS
st.set_page_config(page_title="Aya Celestia 💖", page_icon="🌸", layout="centered")

# Musik Latar
st.audio("https://www.bensound.com/bensound-music/bensound-dreams.mp3", autoplay=True)

# CSS Cantik
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Handlee&family=Poppins:wght@300;500&display=swap');

    html, body, .stApp {
        background-color: #ffe6f0;
        font-family: 'Poppins', cursive;
        color: #4b2e2e;
        padding: 15px;
    }

    h1 {
        text-align: center;
        color: #d63384;
        font-family: 'Handlee', cursive;
        font-size: 40px;
    }

    .heart {
        font-size: 35px;
        text-align: center;
        animation: pulse 1.5s infinite;
        color: #ff69b4;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }

    .section {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 10px #f8c8dc;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown("<h1>Hai Aya Celestia! 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Cuma ingin bikin kamu senyum sebentar hari ini 💖</p>", unsafe_allow_html=True)

# Nama & Sambutan
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    name = st.text_input("Tulis nama kamu di sini 😚")
    if name:
        st.success(f"Halo {name}! Kamu cantik banget hari ini 😍")
    st.markdown("</div>", unsafe_allow_html=True)

# Pujian
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    if st.button("Klik untuk dapat pujian 💌"):
        compliments = [
            "Kamu seperti matahari pagi, selalu membawa semangat 🌞",
            "Tawa kamu menular banget, bikin hati hangat 💕",
            "Setiap hari jadi lebih indah kalau ada kamu 🫶",
            "Kamu itu kayak lagu favorit, nggak pernah bosen didengerin 🎵",
            "Lucunya kamu tuh nggak ada obat 🐰"
        ]
        st.info(random.choice(compliments))
    st.markdown("</div>", unsafe_allow_html=True)

# Ilustrasi Hati
st.markdown("<div class='heart'>💗 💖 💞 💕 💘</div>", unsafe_allow_html=True)

# Surat Felix
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("### 📜 Surat dari Felix")
    st.write("""
    Dear Aya,

    Kamu itu seperti senja yang selalu dinanti.
    Kehadiranmu bikin semuanya terasa hangat dan nyaman.
    Aku cuma pengin bilang satu hal:
    Aku seneng banget kenal kamu 🥹

    🌸 Salam hangat,  
    Felix
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Pesan ke Felix
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("### ✉️ Kirim Pesan ke Felix")
    msg = st.text_input("Mau nitip pesan ke Felix?")
    if msg:
        st.success("Hehe noted~ Felix pasti baca 😎🫶")
    st.markdown("</div>", unsafe_allow_html=True)

# Fun Fact
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("### 🐣 Fun Fact Tentang Felix")
    facts = [
        "Suka banget nasi goreng jam 11 malam 🍛",
        "Nggak bisa minum kopi tapi sok ngopi ☕",
        "Pernah nulis puisi, terus malu sendiri 🙈"
    ]
    if st.button("Fun Fact Hari Ini"):
        st.info(random.choice(facts))
    st.markdown("</div>", unsafe_allow_html=True)

# Hadiah
if st.button("Buka hadiah dari Felix 🎁"):
    st.balloons()
    st.success("Kamu dapet peluk virtual terhangat hari ini 🤗💗")
