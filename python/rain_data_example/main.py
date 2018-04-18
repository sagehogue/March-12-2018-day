import datetime
from operator import itemgetter
import matplotlib.pyplot as plt


class RainData:
    def __init__(self, file_path):
        self.name = 'None'
        self.data = self.load_data(file_path)

    def load_data(self, file_path):
        data = {}
        with open(file_path, 'r', encoding='utf-8')as f:
            lines = f.readlines()
        start = None
        self.name = lines[0]
        for i in enumerate(lines):
            if i[1][0] == '-':
                start = i[0] + 1
                break
        for line in lines[start:]:
            tmp = line.split()
            if tmp[2] == '-':
                continue
            data.update({datetime.datetime.strptime(tmp[0], '%d-%b-%Y'): (tmp[1], tmp[2:])})
        return data

    def find_average(self):
        total = 0
        for k, v in self.data.items():
            total += int(v[0])
        print(total / len(self.data))

    def find_most_rain(self):
        best_day = None
        best_number = 0
        for k, v in self.data.items():
            if int(v[0]) > best_number:
                best_number = int(v[0])
                best_day = k
        print(best_day, self.data[best_day])
        # maxdate = max(self.data, key=lambda key: int(self.data[key][0]))
        # print(maxdate, self.data[maxdate])

    def find_unique_years(self):
        lst = []
        for i in self.data:
            lst.append(i.year)
        return set(lst)

    def find_average_for_year(self, year):
        year = int(year)
        total = 0
        number = 0
        for k, v in self.data.items():
            if k.year == year:
                total += int(v[0])
                number += 1
        return total / number

    def find_highest_yearly_average(self):
        averages = []
        for i in self.find_unique_years():
            averages.append((i, self.find_average_for_year(i)))
        for i in averages:
            print(i)
        return max(averages, key=itemgetter(1))

    def yearly_rain_chart(self):
        x_coord = [str(y) for y in self.find_unique_years()]
        y_coord = [self.find_average_for_year(av) for av in x_coord]
        print(y_coord)
        print(x_coord)
        plt.plot(x_coord, y_coord)
        plt.xlabel('Years')
        plt.ylabel('Averages')
        # plt.gca().invert_xaxis()
        plt.show()


if __name__ == '__main__':
    hayden = RainData('hayden_island.rain')
    swan = RainData('swan_island_pump.rain')
    print(hayden.name)
    hayden.find_most_rain()
    print(swan.name)
    # for k, v in hayden.data.items():
    #     if len(v) == 24:
    #         print(k, v[1][23])
    #     else:
    #         print(k, v[1][len(v)-1])
    # hayden.find_average()

    swan.find_most_rain()
    # hayden.find_unique_years()
    # print(hayden.find_highest_yearly_average())
    # hayden.yearly_rain_chart()
    # swan.yearly_rain_chart()
    #
