from data_processor import *
from global_variables import *
import matplotlib.pyplot as plt
if not os.path.exists('pics/'):
    os.makedirs('pics/')


def monthly_plot():
    '''
    Drag the monthly plot code to run a loop
    :return:
    '''
    for month in range(1,13):
        '''Chage Code Start'''
        # Parameter
        city = 'KSAN'
        #month = 11
        fname = 'pics/{}/precipitation/m{}_plot.jpg'.format(city, month)

        # Code
        if not os.path.exists('pics/{}/precipitation/'.format(city)):
            os.makedirs('pics/{}/precipitation/'.format(city))
        start_year = 1994
        end_year = 2018
        monthly_avg_precip_list = []
        yearly_avg_precip_list = []
        for year in range(start_year, end_year + 1):
            month_start, month_end = get_monthly_start_end(year=year, month=month)
            weather_info = get_info(city, month_start, month_end, info_type='precipitation', output=False)
            monthly_avg_precip_list.append(weather_info['mean'])
            year_start, year_end = get_yearly_start_end(year=year)
            weather_info = get_info(city, year_start, year_end, info_type='precipitation', output=False)
            yearly_avg_precip_list.append(weather_info['mean'])
        print(monthly_avg_precip_list)

        # plot
        plt.figure(figsize=(20, 10))
        plt.plot(range(start_year, end_year), monthly_avg_precip_list[:-1])
        plt.plot(range(start_year, end_year), yearly_avg_precip_list[:-1], '--')
        title_str = '{}'.format(get_month_str(month))
        plt.xlabel('Year', {'size': 25})
        plt.ylabel('Precipitation(mm)', {'size': 25})
        plt.ylim([-0.15, 0.75])
        plt.tick_params(labelsize=23)
        plt.title(title_str, fontsize=28, fontweight='bold')
        plt.legend(['Monthly Average Precipitation', 'Yearly Average Precipitation'],
                   prop={'weight': 'normal', 'size': 20}, loc=1)
        plt.grid()
        plt.savefig(fname)

        #plt.show()
        '''Chage Code end'''
    pass


def yearly_plot():
    '''
    Drag the yearly plot code to run a loop
    :return:
    '''
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
        kv_map = dict([(list(weather_color_refer.keys())[i], 0) for i in range(len(weather_color_refer.keys()))])
        for i in range(len(keys)):
            kv_map[keys[i]] = values[i]
        new_map = {'sunny': kv_map['mostlysunny'] + kv_map['partlysunny'],
                   'clear': kv_map['clear'],
                   'cloudy': kv_map['cloudy'] + kv_map['mostlycloudy'] + kv_map['partlycloudy'],
                   'rain': kv_map['rain'],
                   'disaster': kv_map['hazy'] + kv_map['tstorms']}

        print(new_map)
        keys = list(new_map.keys())
        values = list(new_map.values())

        # Plot
        plt.figure(figsize=(20, 20))
        color_list = list(new_weather_color_refer[k] for k in keys)
        patches, label_text, percent_text = plt.pie(values,
                                                    # explode= tuple([0.02]*len(keys)),
                                                    labels=keys,
                                                    colors=color_list,
                                                    autopct='%3.2f%%',  # digits
                                                    shadow=False,  # No Shadow
                                                    startangle=90,  # reverse start angle
                                                    pctdistance=0.6)  # 数值距圆心半径倍数距离
        plt.axis('equal')
        # plt.legend(loc='lower left',fontsize='25')
        for t in label_text:
            t.set_size(0)
        for t in percent_text:
            t.set_size(35)
        title_str = '{}'.format(year)
        plt.title(title_str, fontsize=70, fontweight='bold')
        plt.savefig(fname)
        '''Chage Code end'''
    pass

if __name__=='__main__':
    monthly_plot()
    #yearly_plot()

    pass