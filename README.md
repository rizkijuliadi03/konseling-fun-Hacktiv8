# Konseling Fun Chatbot 🛋️✨

Proyek ini adalah implementasi Chatbot berbasis LLM menggunakan **LangChain**, **Groq** (model LLaMA), dan **Streamlit** untuk UI-nya. Repositori ini berisi tiga tahapan perkembangan aplikasi chatbot, dari yang paling dasar (CLI) hingga menjadi aplikasi web dengan antarmuka yang menarik dan interaktif.

## Struktur File 📁

Repositori ini memiliki tiga file utama (`app1.py`, `app2.py`, `app3.py`) yang menunjukkan evolusi pembuatan chatbot:

### 1. `app1.py` - Chatbot Berbasis Terminal (CLI)
File ini adalah bentuk paling sederhana dari chatbot. 
- **Antarmuka**: Command Line Interface (CLI) / Terminal.
- **Cara Kerja**: Meminta API Key menggunakan modul `getpass` agar input tidak terlihat di layar. Obrolan dilakukan melalui perulangan `while True` di mana pengguna mengetikkan prompt, dan AI membalas langsung di terminal.
- **Konteks AI**: Secara default, AI diinstruksikan menjadi seorang komedian (`SystemMessage("You are a comedian")`).

### 2. `app2.py` - Dasar UI Chatbot (Streamlit)
File ini adalah langkah awal mengintegrasikan chatbot ke dalam aplikasi web menggunakan Streamlit.
- **Antarmuka**: Web User Interface (Streamlit).
- **Cara Kerja**: Menggunakan `st.session_state` untuk menyimpan API Key dan riwayat obrolan (chat history). Ini adalah bentuk *skeleton* (kerangka) UI chatbot di mana input API Key dan tampilan *bubble* obrolan (pesan user dan AI) mulai dibuat.

### 3. `app3.py` - Aplikasi Final: Konseling Fun Chatbot ✨
Ini adalah aplikasi web chatbot yang sudah selesai dan dipoles secara visual.
- **Tema**: Psikolog virtual yang ramah, asyik, dan suportif ("Konseling Fun").
- **Fitur Utama**:
  - **Tampilan Premium**: Menggunakan tema *Light Mode* pastel yang hangat (disesuaikan di `.streamlit/config.toml`) dan CSS kustom untuk menghilangkan elemen bawaan Streamlit.
  - **Manajemen API Key yang Aman**: API Key dimasukkan melalui *Sidebar* atau bisa dibaca dari file `.env`.
  - **Avatar & Animasi**: Menggunakan emoji avatar kustom (😊 untuk *user* dan ✨ untuk AI) serta dilengkapi dengan spinner animasi (*"Hmm, sebentar ya..."*) saat AI sedang merangkai jawaban.
  - **Pengelolaan Sesi Obrolan**: Tersedia tombol untuk mereset riwayat obrolan di bagian *Sidebar*.

---

## Cara Menjalankan Aplikasi 🚀

### Persyaratan
Pastikan Anda telah menginstal semua pustaka Python yang dibutuhkan. Anda membutuhkan API Key dari Groq atau Google Gemini.
```bash
pip install streamlit langchain-core langchain-google-genai langchain-groq python-dotenv
```

### Menjalankan `app1.py` (Versi Terminal)
```bash
python app1.py
```

### Menjalankan `app3.py` (Versi Web Final)
Buka terminal Anda dan jalankan perintah berikut:
```bash
streamlit run app3.py
```
*(Atau Anda bisa menggunakan `python -m streamlit run app3.py`)*

## Konfigurasi Tema 🎨
Tampilan ceria pada `app3.py` didukung oleh file konfigurasi `.streamlit/config.toml` yang menimpa pengaturan bawaan menjadi tema terang dengan aksen warna pink dan pastel, menyesuaikan dengan nuansa konseling yang hangat dan menenangkan.
