def variant2():
    st.header('Посчитаем долю выживших среди пассажиров выбранного пола:')
    with open("data.csv") as file:
        male = 0
        female = 0
        survived_male = 0
        survived_female = 0
        for line in file.readlines()[1:]:
            lst = line.rstrip().split(",")
            if lst[5] == "male":
                male += 1
            else:
                female += 1
            if lst[1] == "1":
                if lst[5] == "male":
                    survived_male += 1
                else:
                    survived_female += 1
    x = round(survived_female / female, 2)
    y = round(survived_male / male, 2)
    choise = st.radio('Выберите пол пассажира', ['муж', 'жен'])
    if choise == 'муж':
        st.success(f'Доля выживших среди мужчин: {y}')
    else:
        st.warning(f'Доля выживших среди женщин: {x}')
