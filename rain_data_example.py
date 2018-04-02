import datetime
import operator
import matplotlib.pyplot as plt

class RainData:
    def __init__(self, filename):
        self.text_list = self.load(filename)
        self.data = self.load_dictionary(self.text_list)

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()

    def load_dictionary(self, text_list):
        remove_useless = []
        for i in text_list:
            if i.find('-', 11) > -1:
                continue
            remove_useless.append(i)
        return {datetime.datetime.strptime(i.split()[0], '%d-%b-%Y'): list(map(lambda x: int(x), i.split()[1:])) for i in remove_useless}

    def most_rain_day(self):
        most = []
        for date, values in self.data.items():
            most.append((date, sum(values)))
        return max(most, key=operator.itemgetter(1))

    def most_rain_year(self, full=False):
        most = {}
        for date, values in self.data.items():
            if date.year in most:
                most[date.year] += sum(values)
            else:
                most[date.year] = sum(values)
        if not full:
            return max(most.items(), key=operator.itemgetter(1))
        else:
            return most

    def create_graph(self, x_label, y_label):
        plt.plot([str(x[0]) for x in self.data.items()], [x[1] for x in self.data.items()])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.gca().invert_xaxis()
        plt.show()

rain1 = RainData('hayden_island.rain.txt')
rain1.create_graph('year', 'inch')
