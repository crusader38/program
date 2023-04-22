import streamlit as st
def variant3():
    name=st.text_input("Введите имя пассажира")
    with open("data.csv") as file:
        for line in file.readlines()[1:]:
            lst = line.rstrip().split(",")
            if lst[1] == "1" and str(lst[3]+' '+lst[4])[1:-1].startswith(name): st.success(lst[2]+', '+lst[3]+' '+lst[4]+', '+lst[6])
