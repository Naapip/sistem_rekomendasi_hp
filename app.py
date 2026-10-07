"""
RekomenHP - Sistem Rekomendasi Smartphone berbasis ABSA (IndoBERT)
Aplikasi Streamlit yang menyajikan prototipe antarmuka rekomendasi.

Struktur:
  app.py                 -> aplikasi Streamlit (file ini)
  templates/index.html   -> tampilan antarmuka (HTML/CSS/JavaScript)
  data/data_ui.json      -> skor sentimen per merek/model, keluaran notebook bagian 10d

Jalankan lokal : streamlit run app.py
"""
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent
FILE_DATA = BASE / "data" / "data_ui.json"
FILE_TEMPLATE = BASE / "templates" / "index.html"
ASPEK = ["Baterai", "Kamera", "Performa", "Harga"]

st.set_page_config(page_title="RekomenHP", page_icon="📱", layout="wide",
                   initial_sidebar_state="collapsed")

# Sembunyikan elemen bawaan Streamlit agar tampilan sama dengan prototipe,
# dan buat area aplikasi memenuhi tinggi layar.
st.markdown("""
<style>
  header[data-testid="stHeader"], footer, #MainMenu, [data-testid="stToolbar"],
  [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }
  .stApp { background: #f3f4f1; }
  .block-container, [data-testid="stMainBlockContainer"] {
      padding: 0 !important; max-width: 100% !important; }
  [data-testid="stVerticalBlock"] { gap: 0 !important; }
  iframe { display: block; width: 100% !important; height: 100vh !important; border: 0; }
  @media (prefers-color-scheme: dark) { .stApp { background: #111614; } }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def muat_data(path: str) -> dict:
    """Baca data_ui.json dan periksa strukturnya."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for kunci in ["aspek", "jumlah_komentar", "evaluasi", "produk"]:
        if kunci not in data:
            raise ValueError(f"data_ui.json tidak memuat kolom '{kunci}'")
    for p in data["produk"]:
        for a in ASPEK:
            s = p["aspek"][a]
            # skor dihitung ulang dari jumlah opini agar konsisten dengan rumus penelitian
            s["skor"] = round((s["pos"] - s["neg"]) / (s["n"] + data.get("k_smooth", 5)), 3)
    return data


@st.cache_data
def bangun_halaman(path_template: str, path_data: str) -> str:
    data = muat_data(path_data)
    teks_data = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = Path(path_template).read_text(encoding="utf-8")
    return html.replace("__DATA__", teks_data)


try:
    halaman = bangun_halaman(str(FILE_TEMPLATE), str(FILE_DATA))
except (FileNotFoundError, ValueError, KeyError) as e:
    st.error(f"Data aplikasi tidak dapat dimuat: {e}. Pastikan folder data/ berisi data_ui.json "
             "hasil notebook bagian 10d, dan folder templates/ berisi index.html.")
    st.stop()

components.html(halaman, height=900, scrolling=True)
