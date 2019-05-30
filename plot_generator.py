from data_processor import *
from global_variables import *
import matplotlib.pyplot as plt
if not os.path.exists('pics/'):
    os.makedirs('pics/')


def monthly_plot():
    for month in range(1,13):
        '''Chage Code Start'''

        # Parameter
        city = 'KSAN'
        #month = 3
        fname = 'pics/{}/temperature/m{}_plot.jpg'.format(city, month)

        # Code
        if not os.path.exists('pics/{}/temperature/'.format(city)):
            os.makedirs('pics/{}/temperature/'.format(city))
        start_year = 1990
        end_year = 2019
        if month > 4:
            end_year = 2018
        monthly_avg_temp_list = []
        yearly_avg_temp_list = []
        for year in range(start_year, end_year + 1):
            month_start, month_end = get_monthly_start_end(year=year, month=month)
            weather_info = get_info(city, month_start, month_end, info_type='temperature', output=False)
            monthly_avg_temp_list.append(weather_info['mean'])
            year_start, year_end = get_yearly_start_end(year=year)
            weather_info = get_info(city, year_start, year_end, info_type='temperature', output=False)
            yearly_avg_temp_list.append(weather_info['mean'])
        print(monthly_avg_temp_list)

        # plot
        plt.figure(figsize=(20, 10))
        plt.plot(range(start_year, end_year), monthly_avg_temp_list[:-1])
        plt.plot(range(start_year, end_year), yearly_avg_temp_list[:-1], '--')
        title_str = '{}\'s Average Temperature Situation of {} in All Years'.format(get_month_str(month),
                                                                                    code_city_refer[city])
        plt.xlabel('Year')
        plt.ylim([1990, 2019])
        plt.ylabel('Fahrenheit')
        plt.ylim([55, 80])
        plt.title(title_str, fontsize='xx-large', fontweight='bold')
        plt.legend(['Monthly average temperature', 'Yearly average temperature'])
        plt.grid()
        plt.savefig(fname)
        # plt.show()

        '''Chage Code end'''
    pass


def yearly_plot():
    for year in range(1990, 2019):
        '''Chage Code Start'''

        # Parameter
        city = 'KSAN'
        #year = 2018
        fname = 'pics/{}/weather/y{}_pie.jpg'.format(city, year)

        # Code
        if not os.path.exists('pics/{}/weather/'.format(city)):
            os.makedirs('pics/{}/weather/'.format(city))
        year_start, year_end = get_yearly_start_end(year=year)
        weather_info = get_info(city, year_start, year_end, info_type='weather')
        keys = weather_info.index.tolist()
        values = weather_info.days.tolist()

        # Plot
        plt.figure(figsize=(20, 23))
        color_list = list(weather_color_refer[k] for k in keys)
        patches, label_text, percent_text = plt.pie(values,
                                                    explode=tuple([0.02] * len(keys)),
                                                    labels=keys,
                                                    colors=color_list,
                                                    autopct='%3.2f%%',  # digits
                                                    shadow=False,  # No Shadow
                                                    startangle=90,  # reverse start angle
                                                    pctdistance=0.6)  # 数值距圆心半径倍数距离
        plt.axis('equal')
        plt.legend(loc='lower left', fontsize='x-large')
        for t in label_text:
            t.set_size(20)
        for t in percent_text:
            t.set_size(20)
        title_str = '{}\'s Weather Situation in Year {}'.format(code_city_refer[city], year)
        plt.title(title_str, fontsize='xx-large', fontweight='bold')
        plt.savefig(fname)

        '''Chage Code end'''
    pass

if __name__=='__main__':
    #monthly_plot()
    #yearly_plot()
    pass