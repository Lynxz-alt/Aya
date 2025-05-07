import streamlit as st
import random

# 🎵 Musik lembut
st.audio("https://www.bensound.com/bensound-music/bensound-dreams.mp3", autoplay=True)

# 🌸 Konfigurasi halaman
st.set_page_config(page_title="Aya Celestia 💖", page_icon="🌸", layout="centered")

# 🌷 CSS untuk tampilan cantik & rapi
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
    
    html, body, .stApp {
        background-color: #fff0f5;
        font-family: 'Poppins', sans-serif;
        color: #4b2e2e;
        padding: 10px;
    }

    h1, h2, h3 {
        color: #d63384;
    }

    .heart {
        font-size: 40px;
        text-align: center;
        animation: pulse 1.5s infinite;
        color: #ff69b4;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# 🌼 Judul
st.markdown("<h1 style='text-align: center;'>Hai Aya Celestia! 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Cuma ingin bikin kamu senyum sebentar hari ini 💖</p>", unsafe_allow_html=True)

# 💕 Bagian 1: Nama & Pujian
st.markdown("### 💕 Sambutan & Pujian")
name = st.text_input("Tulis nama kamu di sini 😚")
if name:
    st.success(f"Halo {name}! Kamu cantik banget hari ini 😍")

if st.button("Klik untuk dapat pujian 💌"):
    compliments = [
        "Kamu seperti matahari pagi, selalu membawa semangat 🌞",
        "Tawa kamu menular banget, bikin hati hangat 💕",
        "Setiap hari jadi lebih indah kalau ada kamu 🫶",
        "Kamu itu kayak lagu favorit, nggak pernah bosen didengerin 🎵",
        "Lucunya kamu tuh nggak ada obat 🐰"
    ]
    st.info(random.choice(compliments))

st.markdown("---")

# 💖 Bagian 2: Mood Booster
st.markdown("### ❤️ Mood Booster")
st.markdown("<div class='heart'>💗 💖 💞 💕 💘</div>", unsafe_allow_html=True)

st.markdown("---")

# ✉️ Bagian 3: Pesan untuk Felix
st.markdown("### ✉️ Kirim Pesan ke Felix")
msg = st.text_input("Mau nitip pesan ke Felix?")
if msg:
    st.success("Hehe noted~ Felix pasti baca 😎🫶")

st.markdown("---")

# 📜 Bagian 4: Surat dari Felix
with st.expander("📜 Buka Surat dari Felix"):
    st.write("""
    Dear Aya,

    Kamu itu seperti senja yang selalu dinanti.
    Kehadiranmu bikin semuanya terasa hangat dan nyaman.
    Aku cuma pengin bilang satu hal:
    Aku seneng banget kenal kamu 🥹

    🌸 Salam hangat,
    Felix
    """)

# 🐣 Bagian 5: Fun Fact
with st.expander("🐣 Fun Fact Tentang Felix"):
    facts = [
        "Suka banget nasi goreng jam 11 malam 🍛",
        "Nggak bisa minum kopi tapi sok ngopi ☕",
        "Pernah nulis puisi, terus malu sendiri 🙈"
    ]
    if st.button("Fun Fact Hari Ini"):
        st.info(random.choice(facts))

# 🎁 Bagian 6: Hadiah
if st.button("Buka hadiah dari Felix 🎁"):
    st.balloons()
    st.success("Kamu dapet peluk virtual terhangat hari ini 🤗💗")

st.markdown("---")

# 💌 Bagian 7: Pesan Harian
with st.expander("💌 Pesan Spesial Hari Ini"):
    daily_messages = [
        "Semoga harimu seindah senyummu hari ini 💕",
        "Kalau kamu cape, istirahat ya. Dunia tetap nunggu kamu bersinar 🌟",
        "Felix percaya kamu bisa lewatin semuanya 💪💗",
        "Kamu pantas dapetin semua hal baik di dunia ini 😚"
    ]
    st.success(random.choice(daily_messages))

# 💞 Bagian 8: Kutipan Romantis
with st.expander("💞 Kutipan Romantis dari Felix"):
    quotes = [
        "Cinta itu bukan tentang seberapa sering kamu bilang 'aku cinta kamu', tapi seberapa besar kamu membuktikannya. 💖",
        "Kalau kamu senyum, dunia Felix auto terang 🌍✨",
        "Kalau ada 100 alasan buat nyerah, Felix punya 101 alasan buat tetap sayang kamu. 😘"
    ]
    st.markdown(f"<div style='text-align: center; font-style: italic; color: #d63384;'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# 🎲 Bagian 9: Mini Game
with st.expander("🎲 Tebak Angka dari Felix"):
    angka = random.randint(1, 5)
    tebakan = st.number_input("Tebak angka dari 1 - 5", min_value=1, max_value=5, step=1)
    if st.button("Tebak Sekarang!"):
        if tebakan == angka:
            st.balloons()
            st.success("Yeay! Kamu bener! Felix bangga banget 😍")
        else:
            st.error("Belum tepat 😅 Coba lagi yaa!")
