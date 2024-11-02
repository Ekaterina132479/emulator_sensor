import random      #библиотека для генерации случайных значений
import datetime    #библиотека для работы с датой и временем
import time        #библиотека для задержки времени

#функция sensor_emulator принимает на вход название метрики, 
#диапазон значений для генерации и единицу измерения
def sensor_emulator(metric_name, metric_range, metric_unit):
    #время начала работы эмулятора
    start_time = datetime.datetime.now()     
    #время окончания работы эмулятора
    end_time = start_time + datetime.timedelta(minutes=2)    

    #открытие файла для записи данных определённой метрики
    with open(f"{metric_name}_data.txt", "w", encoding="UTF-8") as file:
        #цикл выполняется, пока текущее время меньше времени окончания 
        while datetime.datetime.now() < end_time:
            #создание пустого списка
            sensor_values = []
            #генерация 60-ти случайных значений и их запись в список
            for _ in range(60):
                value = random.uniform(metric_range[0], metric_range[1])
                sensor_values.append(value)
                time.sleep(1)

            #вычисление среднего значения метрики за 1 минуту
            avg_value = sum(sensor_values) / 60
            #время окончания работы эмулятора
            current_time = datetime.datetime.now()
            #запись в файл времени окончания работы эмулятора, имени метрики, значения и единицы измерения
            file.write(f"{current_time}, {metric_name}, {avg_value:.2f} {metric_unit}\n")
            
    print(f" sensor '{metric_name}' done")

    #пример работы эмулятора
sensor_emulator("temperature", (-20, 40), "°C")
sensor_emulator("humidity", (0, 100), "%")
sensor_emulator("air_quality", (0, 500), "ppm")