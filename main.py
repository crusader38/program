import streamlit as st
import csv
import variant1
import variant2.ru
import variant3.ru
import variant4

def user_name(par):
    if par == "var1":
        return "Вариант 1, выполнил Горелкин А.В., доля спасенных/погибших пассажиров по возрастным группам"
    elif par == "var2":
        return "Вариант 2, выполнила Гочияева Л."
    elif par == "var3":
        return "Вариант 3, выполнила Исмагилова Э."
    elif par == "var4":
        return "Вариант 4, выполнил Бутов С.А., данные спасенных/погибших пассажиров с билетами нулевой стоимости"

st.title("Команда №4, практическая работа 10")
var = st.selectbox(
    label = "Выбери вариант:",
    options = ["var1","var2","var3","var4"],
    format_func = user_name
)
st.text(user_name(var))
if var == "var1":
    variant1.variant1()
elif var == "var2":
    pass
    variant2.variant2()
elif var == "var3":
    pass
    variant3.variant3()
elif var == "var4":
    variant4.variant4()
