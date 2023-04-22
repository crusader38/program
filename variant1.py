def variant1():
    st.header("Посчитать долю пассажиров Титаника, указав: вести поиск среди спасенных или погибших, искать в возрастных группах до 30 лет или старше 60 лет")
    with open("data.csv") as file:
        file_reader = csv.reader(file, delimiter=",")
        surv30 = 0
        surv60 = 0
        unsurv30 = 0
        unsurv60 = 0
        count = 0
        for line in file_reader:
            count += 1
            if line[5] != '':
                if line[1] == '1':
                    if float(line[5]) < 30:
                        surv30 += 1
                    if float(line[5]) > 60:
                        surv60 += 1
                elif line[1] == '0':
                    if float(line[5]) < 30:
                        unsurv30 += 1
                    if float(line[5]) > 60:
                        unsurv60 += 1
    ch1 = st.radio("Поиск пассажиров среди:", ["спасенных", "погибших"])
    ch2 = st.radio("Поиск в возрастной группе:", ["до 30 лет", "старше 60 лет"])
    if ch1 == 'спасенных':
        if ch2 == 'до 30 лет':
            st.success("Доля спасенных пассажиров в возрастной группе до 30 лет: "+str(round(surv30/count*100))+"%")
        else:
            st.success("Доля спасенных пассажиров в возрастной группе старше 60 лет: "+str(round(surv60/count*100))+"%")
    else:
        if ch2 == 'до 30 лет':
            st.error("Доля погибших в возрастной группе до 30 лет: "+str(round(unsurv30/count*100))+"%")
        else:
            st.error("Доля погибших пассажиров в возрастной группе старше 60 лет: "+str(round(unsurv60/count*100))+"%")
