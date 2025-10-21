import streamlit as st
import csv

csv_file = 'data.csv'

fieldnames = ('PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked')

def calculate_relatives(row):
  return (int(row['SibSp']) + int(row['Parch']))

def calculate_average(list: list):
   if not list:
      return 0
   return round(sum(list) / len(list), 2)

def get_average_relatives_from_file(file: str):
  survived_passengers, dead_passengers = [], []

  try:
    with open(file, 'r', encoding='utf-8') as file:
      reader = csv.DictReader(file, fieldnames=fieldnames)
      next(reader)
      for row in reader:
        if int(row['Survived']) == 1:
          survived_passengers.append(calculate_relatives(row))
        else:
          dead_passengers.append(calculate_relatives(row))

      return survived_passengers, dead_passengers
  except FileNotFoundError:
     return [], []

survived, dead = get_average_relatives_from_file(csv_file)

st.image("titanic-image.jpg")
st.title("Данные пассажиров Титаника")
st.write("Для просмотра данных только по выжившим или погибшим, выберите соответсвующий пункт из списка:")

selected = st.selectbox(
    "Значение поля Survived:",
    ("Выжившие", "Погибшие")
)

if selected == "Выжившие":
    st.write(f"Среднее количество родственников у выживших пассажиров: {calculate_average(survived)}")
else:
    st.write(f"Среднее количество родственников у погибших пассажиров: {calculate_average(dead)}")