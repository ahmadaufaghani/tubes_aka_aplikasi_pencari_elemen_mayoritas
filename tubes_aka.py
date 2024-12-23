import streamlit as st
import algoritma_mayoritas as am
from datetime import datetime
import sys 

sys.setrecursionlimit(10000000)

st.header("Aplikasi Pencarian Elemen Mayoritas")
st.text("Cara kerja dari aplikasi ini yaitu mencari elemen mayoritas berdasarkan jumlah kemunculan yang lebih dari n/2.")

elemen = st.form("form_voting_moore")
angka = elemen.text_area("Silahkan masukkan angka yang akan dicari elemen mayoritasnya : ")
submit = elemen.form_submit_button("Proses")


findIteratif = am.findModeLoop(angka.split(','), len(angka.split(',')))

findRecursive = am.findModeRecursive(angka.split(','), len(angka.split(',')))

if submit :
    st.write("**Iteratif**")
    startIterative = datetime.now()
    st.write("Hasil :",int(findIteratif))
    endIterative = datetime.now()
    st.write("Waktu Eksekusi : ", (endIterative - startIterative).total_seconds(), "detik")
    st.write("**Rekursif**")
    startRecursive = datetime.now()
    st.write("Hasil :",int(findRecursive))
    endRecursive = datetime.now()
    st.write("Waktu Eksekusi : ", (endRecursive - startRecursive).total_seconds(), "detik")