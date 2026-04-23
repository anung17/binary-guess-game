#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-04-22 09:47
# Distributed under terms of the MIT license.

"""
Streamlit version of binary guess number game.
"""

import streamlit as st
from math import sqrt, ceil

st.set_page_config(layout="wide")

st.logo('images/trisula.png', size='large')

st.header("Dukun Digital Tebak Angka")
st.markdown('''
Aplikasi ini meminta kamu untuk memilih sebuah angka bilangan bulat,
dan berusaha untuk menebak angka yang kamu pikirkan.
''')

#biggest = int(input("Bilangan bulat positif terbesar yang diinginkan: "))
##biggest = st.slider( "Bilangan bulat positif terbesar yang diinginkan:", 31, 100, 31)
biggest = 63
len_bin = len(bin(biggest))-2
##print(f"Number of cards needed: {len_bin}.")

cards = {}
max_members = 0

for card in range(1, len_bin+1):
    ## print(f"{card=}")
    members = []
    for num in range(1, biggest+1):
        card_index = -card
        ## print(f"{bin(num)=}")
        pads = len_bin - len(bin(num)) + 2
        ## print(f"{pads=}")
        if pads>0:
            bin_rep = '0'*pads+bin(num)[2:]
        else:
            bin_rep = bin(num)[2:]
        ## print(f"{bin(num)=} {pads=} {num=} {bin_rep=}")
        if bin_rep[card_index] == '1':
            members.append(num)
    ##print(f"Card number {card} contains {len(members)} numbers:\n{members}.")
    cards[card] = members
    if len(members) > max_members:
        max_members = len(members)

kolom = int(ceil(sqrt(max_members)))

def reset_callback():
    st.session_state.total = 0
    st.session_state.kartu1 = None
    st.session_state.kartu2 = None
    st.session_state.kartu3 = None
    st.session_state.kartu4 = None
    st.session_state.kartu5 = None
    st.session_state.kartu6 = None


def print_numbers(data):
    baris = '## `'
    kol = 1
    printed = len(data)
    ##print(data)
    for d in data:
        baris = baris + f"{d:02d} "
        printed -= 1
        kol += 1
        if kol > kolom:
            kol = 1
            if printed>0:
                baris = baris + '`\n## `'
            else:
                baris = baris + '`\n'
    if printed>=0:
        baris = baris + "`"
    ##print(f"{printed:02d} {baris}")
    return baris


##pprint(cards)

petunjuk, about_us = st.tabs(
    [':green[Petunjuk]', ':green[Tentang Kami]']
)

with petunjuk:
    st.header("Petunjuk Permainan")
    st.write('''
- Pikirkan sebuah bilangan bulat antara 1 hingga 63.
- Periksa apakah bilangan yang kamu pikirkan muncul di `Kartu 1`, `Kartu 2`, dan seterusnya hingga `Kartu 6` di bawah ini.
- Pada setiap tab Kartu, kamu harus menjawab apakah bilangan yang kamu pikirkan "**Ada**" atau "**Tidak ada**".
- _Dukun Digital_ akan menebak angka yang kamu pikirkan di tab `Hasil`.
             '''
            )
    st.session_state.total = 0

with about_us:
    st.write("Dibuat oleh:")
    st.write("Laboratorium Pemrograman")
    st.write("Jurusan Teknik Informatika")
    st.write("Fakultas Teknologi Industri")
    st.write("Universitas Trisakti")

tab1, tab2, tab3, tab4, tab5, tab6, hasil = st.tabs(
    [
     '`Kartu 1`', '`Kartu 2`', '`Kartu 3`',
     '`Kartu 4`', '`Kartu 5`', '`Kartu 6`',
        '`Hasil`'
    ]
)

with tab1:
    st.write(print_numbers(cards[1]))
    kartu1 = st.radio(
        "Apakah bilangan yang kamu pikirkan muncul di sini?",
        ['Ada', 'Tidak ada'],
        horizontal=True,
        index=None,
        key='kartu1'
    )
    if kartu1 == 'Ada':
        st.session_state.total += 1
    else:
        st.session_state.total += 0


with tab2:
    st.write(print_numbers(cards[2]))
    kartu2 = st.radio(
        "Apakah bilangan yang kamu pikirkan muncul di sini?",
        ['Ada', 'Tidak ada'],
        horizontal=True,
        index=None,
        key='kartu2'
    )
    if kartu2 == 'Ada':
        st.session_state.total += 2
    else:
        st.session_state.total += 0

with tab3:
    st.write(print_numbers(cards[3]))
    kartu3 = st.radio(
        "Apakah bilangan yang kamu pikirkan muncul di sini?",
        ['Ada', 'Tidak ada'],
        horizontal=True,
        index=None,
        key='kartu3'
    )
    if kartu3 == 'Ada':
        st.session_state.total += 4
    else:
        st.session_state.total += 0

with tab4:
    st.write(print_numbers(cards[4]))
    kartu4 = st.radio(
        "Apakah bilangan yang kamu pikirkan muncul di sini?",
        ['Ada', 'Tidak ada'],
        horizontal=True,
        index=None,
        key='kartu4'
    )
    if kartu4 == 'Ada':
        st.session_state.total += 8
    else:
        st.session_state.total += 0

with tab5:
    st.write(print_numbers(cards[5]))
    kartu5 = st.radio(
        "Apakah bilangan yang kamu pikirkan muncul di sini?",
        ['Ada', 'Tidak ada'],
        horizontal=True,
        index=None,
        key='kartu5'
    )
    if kartu5 == 'Ada':
        st.session_state.total += 16
    else:
        st.session_state.total += 0

with tab6:
    st.write(print_numbers(cards[6]))
    kartu6 = st.radio(
        "Apakah bilangan yang kamu pikirkan muncul di sini?",
        ['Ada', 'Tidak ada'],
        horizontal=True,
        index=None,
        key='kartu6'
    )
    if kartu6 == 'Ada':
        st.session_state.total += 32
    else:
        st.session_state.total += 0

with hasil:
    st.header("Hasil")
    if kartu1 is None:
        st.write("Kamu belum menentukan jawaban untuk `Kartu 1`.")
    elif kartu2 is None:
        st.write("Kamu belum menentukan jawaban untuk `Kartu 2`.")
    elif kartu3 is None:
        st.write("Kamu belum menentukan jawaban untuk `Kartu 3`.")
    elif kartu4 is None:
        st.write("Kamu belum menentukan jawaban untuk `Kartu 4`.")
    elif kartu5 is None:
        st.write("Kamu belum menentukan jawaban untuk `Kartu 5`.")
    elif kartu6 is None:
        st.write("Kamu belum menentukan jawaban untuk `Kartu 6`.")
    else:
        st.write("Terima kasih sudah menentukan jawaban untuk semua kartu...")

        with st.expander("..dan angka yang kamu pikirkan adalah", expanded=False):
            st.write(f"## `{st.session_state.total}`")
            st.write("Bagaimana, apakah tebakan _Dukun Digital_ benar?")
        st.button("Ulangi dari awal", on_click=reset_callback)

