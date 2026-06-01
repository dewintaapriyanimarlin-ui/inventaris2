import streamlit as st
import pandas as pd

# Data Inventaris (Dummy Awal)

if "data_barang" not in st.session_state:
    st.session_state.data_barang = [
        {"ID": "BRG01", "Nama": "Laptop", "Stok": 10, "Harga": 7000000},
        {"ID": "BRG02", "Nama": "Mouse", "Stok": 25, "Harga": 150000},
    ]

# Fungsi untuk menampilkan data sebagai DataFrame
def tampilkan_data():
    df = pd.DataFrame(st.session_state.data_barang)
    st.dataframe(df)


# Tampilan Menu
st.title("📦 Aplikasi Inventaris Barang")

menu = st.sidebar.radio("Menu", ["Tambah Barang", "Tampilkan Data", "Edit Barang", "Hapus Barang", "Cari Barang"])


# Tambah Barang
if menu == "Tambah Barang":
    st.subheader("➕ Tambah Barang")
    id_barang = st.text_input("ID Barang")
    nama_barang = st.text_input("Nama Barang")
    stok = st.number_input("Stok", min_value=0)
    harga = st.number_input("Harga", min_value=0)

    if st.button("Simpan"):
        st.session_state.data_barang.append(
            {"ID": id_barang, "Nama": nama_barang, "Stok": stok, "Harga": harga}
        )
        st.success(f"Barang {nama_barang} berhasil ditambahkan!")


# Tampilkan Data
elif menu == "Tampilkan Data":
    st.subheader("📋 Data Barang")
    tampilkan_data()


# Edit Barang
elif menu == "Edit Barang":
    st.subheader("✏️ Edit Barang")
    tampilkan_data()
    id_edit = st.text_input("Masukkan ID Barang yang ingin diedit")

    barang = next((b for b in st.session_state.data_barang if b["ID"] == id_edit), None)
    if barang:
        nama_baru = st.text_input("Nama Barang", barang["Nama"])
        stok_baru = st.number_input("Stok", min_value=0, value=barang["Stok"])
        harga_baru = st.number_input("Harga", min_value=0, value=barang["Harga"])

        if st.button("Update"):
            barang["Nama"] = nama_baru
            barang["Stok"] = stok_baru
            barang["Harga"] = harga_baru
            st.success("Data barang berhasil diperbarui!")
    else:
        if id_edit:
            st.warning("ID Barang tidak ditemukan.")


# Hapus Barang
elif menu == "Hapus Barang":
    st.subheader("🗑️ Hapus Barang")
    tampilkan_data()
    id_hapus = st.text_input("Masukkan ID Barang yang ingin dihapus")

    if st.button("Hapus"):
        st.session_state.data_barang = [b for b in st.session_state.data_barang if b["ID"] != id_hapus]
        st.success(f"Barang dengan ID {id_hapus} berhasil dihapus!")


# Cari Barang
elif menu == "Cari Barang":
    st.subheader("🔍 Cari Barang")
    keyword = st.text_input("Masukkan ID atau Nama Barang")

    if keyword:
        hasil = [b for b in st.session_state.data_barang if keyword.lower() in b["ID"].lower() or keyword.lower() in b["Nama"].lower()]
        if hasil:
            st.write("Hasil pencarian:")
            st.dataframe(pd.DataFrame(hasil))
        else:
            st.warning("Barang tidak ditemukan.")
