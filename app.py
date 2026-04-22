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
from math import sqrt

st.set_page_config(layout="wide")

def reset_callback():
    st.session_state.total = 0
    st.session_state.kartu1 = None
    st.session_state.kartu2 = None
    st.session_state.kartu3 = None
    st.session_state.kartu4 = None
    st.session_state.kartu5 = None


#biggest = int(input("Bilangan bulat positif terbesar yang diinginkan: "))
##biggest = st.slider( "Bilangan bulat positif terbesar yang diinginkan:", 31, 100, 31)
biggest = 31
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

kolom = int(sqrt(max_members))

def print_numbers(data):
    baris = '## `'
    kol = 1
    printed = len(data)
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
    if printed>0:
        baris = baris + "`"
    return baris

##pprint(cards)

petunjuk, tab1, tab2, tab3, tab4, tab5,hasil = st.tabs(
    ['Petunjuk', 'Kartu 1', 'Kartu 2', 'Kartu 3',
     'Kartu 4', 'Kartu 5', 'Hasil']
)

with petunjuk:
    st.header("Petunjuk Permainan")
    st.write('''
Pikirkan sebuah bilangan bulat antara 1 hingga 31. Cek apakah bilangan yang anda pikirkan muncul di Kartu 1, Kartu 2, dan seterusnya hingga Kartu 5.'''
            )
    st.session_state.total = 0

with tab1:
    st.header("Kartu 1")
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
    st.header("Kartu 2")
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
    st.header("Kartu 3")
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
    st.header("Kartu 4")
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
    st.header("Kartu 5")
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

with hasil:
    st.header("Hasil")
    with st.expander("Angka yang kamu pikirkan adalah", expanded=False):
        st.write(f"## `{st.session_state.total}`")
    st.button("Ulangi dari awal", on_click=reset_callback)

