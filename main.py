import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

#st.set_page_config() adalah sebuah metode yang digunakan untuk mengubah sebuah parameter dari aplikasi page kita
st.set_page_config(
    page_title='Exploratory Data Analysis App',
    layout='wide'
)

#persiapkan parameter konfigurasi
path_dataset = st.secrets.path_configuration.path_dataset
file_name='Jumlah PNS Jabar.csv'


#baca data
df=pd.read_csv(f'{path_dataset}{file_name}')
df=df.drop(['kode_provinsi','nama_provinsi','satuan'],axis=1)

#container title
with st.container():
    st.title('Jumlah PNS Jawa Barat Tahun 2015 - 2023')
    st.text('oleh : Dwi Nur Cahyani')

#menampilkan data
st.dataframe(df,
             use_container_width=True)
#mengecek data unik
#for column in df.columns:
#    st.text(df[column].unique())

#container 1
_=df.groupby(['tahun','jenis_kelamin'],as_index=False)['jumlah_pns'].sum()
table = pd.pivot_table(_, values='jumlah_pns', index=['tahun'],
                       columns=['jenis_kelamin'], aggfunc="sum")


#untuk cek dibikin dataframe
#st.dataframe(table,
#             use_container_width=True)


st.divider()

#container 2
with st.container():
    coln2_col1,con2_col2=st.columns([2,1])
    with coln2_col1:
        st.bar_chart(table)
    with con2_col2:
        st.markdown('''
            <p class 'analisis_1'> Kesimpulan : </p>''',
            unsafe_allow_html=True
            )
        st.markdown('''
            <p> 1. Terjadi ketimpangan jumlah pegawai laki - laki dan perempuan antara tahun 2015 - 2017 <p\n>''',
            unsafe_allow_html=True
            )
        st.markdown('''
            <p> 2. Lonjakan penerimaan pegawai hampir 3x lipat antara tahun 2017 - 2018 <p\n>''',
            unsafe_allow_html=True)
        st.markdown('''
            <p> 3. Terjadi penurunan yang konsisten pada tahun 2018 - 2023 <p\n>''',
            unsafe_allow_html=True)

st.divider()

#data contain
idx=df.groupby(['tahun'])['jumlah_pns'].transform(max)== df['jumlah_pns']
idx_max=(df[idx])
st.dataframe(idx_max)

#container2
with st.container():
    con3_col1,con3_col2,con3_col3,con3_col4=st.columns(4)
    with con3_col1:
        temp= idx_max[idx_max.tahun == 2017]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]}-{temp["tahun"].values[0]}',value=temp["jumlah_pns"].values[0])
    with con3_col2:
        temp= idx_max[idx_max.tahun == 2019]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]}-{temp["tahun"].values[0]}',value=temp["jumlah_pns"].values[0])
    with con3_col3:
        temp= idx_max[idx_max.tahun == 2021]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]}-{temp["tahun"].values[0]}',value=temp["jumlah_pns"].values[0])
    with con3_col4:
        temp= idx_max[idx_max.tahun == 2023]
        st.metric(label=f'{temp["perangkat_daerah"].values[0]}-{temp["tahun"].values[0]}',value=temp["jumlah_pns"].values[0])
    st.markdown('''
            <p> Kesimpulan : </p>''',
            unsafe_allow_html=True
            )
    st.markdown('''
            <p> Dalam beberapa tahun Dinas Pendidikan masih menempati posisi teratas </p>''',
            unsafe_allow_html=True
            )

st.divider()

with st.container():
    con4_col1,con4_col2=st.columns([1,10])

    tahun = con4_col1.text_input('Tahun', max_chars=4)
    temp = df[df['tahun']==int(tahun)]
    st.dataframe(temp,use_container_width=True)



#examplecheckbox
    for item in df['jenis_kelamin'].unique():
        a=st.checkbox(item)

    print(item)

