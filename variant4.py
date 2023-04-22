import streamlit as st
import csv
def variant4():
  ch = st.radio("Поиск пассажиров с билетом нулевой стоимости:", ["спасенные","погибшие"])
  with open('data.csv') as file:
      file_reader = csv.reader(file, delimiter=",")
      for line in file_reader:
          if ch == "спасенные":
              if line[9] == '0' and line[1] == '1':
                  st.success("Имя: "+line[3]+", пол: "+line[4]+", возраст: "+line[5])
          else:
              if line[9] == '0' and line[1] == '0':
                  st.error("Имя: "+line[3]+", пол: "+line[4]+", возраст: "+line[5])
