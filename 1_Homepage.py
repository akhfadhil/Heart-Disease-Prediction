import streamlit as st

st.set_page_config(
    page_title = "Heart Disease Prediction",
    page_icon="🧊",
    layout = "wide"
)

i, ii, iii = st.columns([1,2,1])
with ii:
    st.markdown("<h1 style='text-align: center; color: white;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    st.image('heart.jpg', caption='Healthy heart', width=700)

with st.container(border=True):
    st.markdown(
        """
        \nMenurut Kementerian Kesehatan (Kemenkes), penyakit jantung menjadi penyebab kematian terbanyak di Indonesia. Tidak hanya di Indonesia, kedua penyakit kardiovaskular tersebut 
        juga menjadi perhatian dunia. Sebagian besar negara di dunia mengalokasikan sebagian besar anggarannya untuk memastikan warganya sehat. Namun, negara-negara masih belum mampu 
        memenuhi permintaan layanan medis yang ideal bagi warganya karena kurangnya keahlian medis di berbagai rumah sakit. 
        \nSistem diagnosis medis telah banyak diterapkan untuk mendiagnosis gejala penyakit seperti kanker dan diabetes. Namun, alat dan metode analisis 
        tidak cukup untuk mengidentifikasi hubungan tersembunyi dalam gejala penyakit jantung. Akibatnya, rasio penderita penyakit ini meningkat pesat hingga 
        12 juta kematian setiap tahun. Saling ketergantungan yang kompleks pada berbagai gejala penyakit ini menunjukkan sulitnya 
        mendiagnosis penyakit jantung pada tahap awal. Dokter tidak memiliki cukup waktu untuk menangani setiap kasus dan mengalami kesulitan dalam mengikuti perkembangan 
        aplikasi terbaru. Banyak metode alternatif telah disarankan untuk diagnosis medis di bidang kesehatan. Namun, mengevaluasi fungsionalitas sistem diagnosis penyakit jantung
        masih merupakan tantangan. 
        \nSalah satu metode yang dapat digunakan yaitu machine learning. Dengan menggunakan sistem dan alat yang dirancang untuk mengurutkan dan mengkategorikan data, algoritma 
        machine learning dapat menemukan pola dalam kumpulan data yang memungkinkan para profesional di bidang medis mengidentifikasi penyakit jantung dan melakukan pencegahan.
        Data yang digunakan pada sistem ini berasal dari repositori machine learning Universitas California Irvine. Algoritma machine learning yang digunakan pada sistem ini yaitu 
        Logistic Regression yang memiliki akurasi sebesar 90%. 
        """)