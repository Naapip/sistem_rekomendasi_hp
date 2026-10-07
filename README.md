# RekomenHP

Prototipe sistem rekomendasi smartphone berbasis Aspect-Based Sentiment Analysis (IndoBERT)
pada komentar YouTube berbahasa Indonesia.

## Isi folder
| File | Fungsi |
|---|---|
| `app.py` | Aplikasi Streamlit |
| `templates/index.html` | Tampilan antarmuka (HTML/CSS/JavaScript) |
| `data/data_ui.json` | Skor sentimen per merek/model, keluaran notebook bagian 10d |
| `requirements.txt` | Pustaka yang dibutuhkan |
| `.streamlit/config.toml` | Pengaturan tema |

## Menjalankan di komputer sendiri
```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Community Cloud
1. Buat repository baru di GitHub (misalnya `rekomenhp`) dan unggah seluruh isi folder ini,
   termasuk folder `templates`, `data`, dan `.streamlit`.
2. Buka https://share.streamlit.io, masuk dengan akun GitHub, pilih **Create app**.
3. Pilih repository, branch `main`, dan *main file path* `app.py`, lalu **Deploy**.
4. Setelah selesai, salin URL aplikasi (misalnya `https://rekomenhp.streamlit.app`).

## Memperbarui data
Jalankan ulang notebook sampai bagian 10d, ambil `data_ui.json` dari folder `hasil/`,
ganti file `data/data_ui.json` di repository, lalu commit. Aplikasi otomatis memuat data baru.
