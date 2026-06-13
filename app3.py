# Jalankan dengan
# >>> streamlit run <nama file>
#
# Atau
# >>> python -m streamlit run <nama file>
#

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# 1. Konfigurasi Halaman (Harus dipanggil paling pertama)
st.set_page_config(
    page_title="Konseling Fun",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto"
)

load_dotenv()

# 2. Kustomisasi CSS untuk tampilan yang lebih premium
st.markdown("""
<style>
    /* Menyembunyikan menu default streamlit dan footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Styling judul utama */
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #FF6B9E;
        text-shadow: 2px 2px 4px rgba(255, 107, 158, 0.2);
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.markdown('<div class="main-title">✨ Curhat & Konseling Fun</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Teman cerita yang asyik, hangat, dan siap dukung kamu kapan aja! 💖 <br><span style="font-size: 0.9rem;"><i>Demo chatbot oleh Rizki Juliadi</i></span></div>', unsafe_allow_html=True)

# 3. Sidebar untuk API Key dan Info Tambahan
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063206.png", width=100)
    st.header("Pengaturan")
    
    api_key_missing = (
        os.environ.get("GOOGLE_API_KEY", "") == ""
        and os.environ.get("GROQ_API_KEY", "") == ""
    )
    
    if api_key_missing:
        st.warning("Silakan masukkan API Key untuk memulai sesi.")
        input_api_key = st.text_input("API Key", type="password")
        submit_key = st.button("Simpan Key")
        
        if submit_key and input_api_key:
            os.environ["GOOGLE_API_KEY"] = input_api_key
            os.environ["GROQ_API_KEY"] = input_api_key
            st.success("API Key tersimpan!")
            st.rerun()
    else:
        st.success("Sistem siap digunakan.")
        if st.button("Hapus Riwayat Obrolan"):
            st.session_state["chat_history"] = []
            st.rerun()
            
    st.markdown("---")
    st.markdown("**Privasi & Keamanan**\n\nSemua percakapan bersifat privat dan riwayat akan hilang saat memuat ulang halaman.")

# Jika API key belum ada, hentikan eksekusi
if api_key_missing:
    st.info("👈 Masukkan API Key di panel sebelah kiri untuk memulai sesi konsultasi.")
    st.stop()

# 4. Inisialisasi LLM Client
client = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
# client = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 5. Inisialisasi Chat History
if "chat_history" not in st.session_state or len(st.session_state["chat_history"]) == 0:
    st.session_state["chat_history"] = [
        SystemMessage("Anda adalah seorang psikolog profesional yang sangat ramah, hangat, dan menyenangkan. Berikan tanggapan yang empatik, suportif, dan sedikit ceria agar suasana tidak suram, namun tetap profesional dan membantu penyelesaian masalah. Gunakan bahasa Indonesia yang santai, bersahabat, dan mudah dipahami.")
    ]
    
# Tampilkan sapaan awal
if len(st.session_state["chat_history"]) == 1:
    with st.chat_message("ai", avatar="✨"):
        st.markdown("Halo kak! 👋 Saya psikolog virtual Anda hari ini. Ada cerita atau unek-unek yang mau dibagikan? Jangan sungkan ya, saya siap mendengarkan dan membantu!")

# 6. Menampilkan Chat History
for chat in st.session_state["chat_history"]:
    if isinstance(chat, HumanMessage):
        with st.chat_message("human", avatar="😊"):
            st.markdown(chat.content)
    elif isinstance(chat, AIMessage):
        with st.chat_message("ai", avatar="✨"):
            st.markdown(chat.content)

# 7. Input Pengguna
user_input = st.chat_input("Ketik pesan Anda di sini...")
if user_input:
    # Tampilkan pesan user
    st.session_state["chat_history"].append(HumanMessage(user_input))
    with st.chat_message("human", avatar="😊"):
        st.markdown(user_input)

    # Tampilkan indikator loading saat AI berpikir
    with st.chat_message("ai", avatar="✨"):
        with st.spinner("Hmm, sebentar ya..."):
            response = client.invoke(st.session_state["chat_history"])
            st.markdown(response.content)
            st.session_state["chat_history"].append(response)