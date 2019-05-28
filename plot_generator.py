from data_processor import *
from global_variables import *
import matplotlib.pyplot as plt
if not os.path.exists('pics/'):
    os.makedirs('pics/')

for year in range(1990, 2019):
    # Parameter
    city = 'KSAN'
    #year = 2018
    fname = 'pics/{}/precipitation/y{}_plot.jpg'.format(city, year)
    if not os.path.exists('pics/{}/precipitation/'.format(city)):
        os.makedirs('pics/{}/precipitation/'.format(city))
    # Code
    monthly_avg_precip_list = []
    for month in range(1, 13):
        month_start, month_end = get_monthly_start_end(year=year, month=month)
        weather_info = get_info(city, month_start, month_end, info_type='precipitation', output=False)
        monthly_avg_precip_list.append(weather_info['mean'])
    print(monthly_avg_precip_list)
    year_start, year_end = get_yearly_start_end(year=year)
    weather_info = get_info(city, year_start, year_end, info_type='precipitation', output=False)
    yearly_avg_precip_list = list([weather_info['mean'] for i in range(12)])
    print(yearly_avg_precip_list)

    # Plot
    plt.figure(figsize=(20, 10))
    plt.plot(range(12), monthly_avg_precip_list)
    plt.plot(range(12), yearly_avg_precip_list, '--')
    title_str = '{}\'s Monthly Precipitation Situation in Year {}'.format(code_city_refer[city], year)
    plt.xlabel('Month')
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.ylabel('Precipitation (mm)')
    plt.title(title_str, fontsize='xx-large', fontweight='bold')
    plt.legend(['Monthly Average Precipitation', 'Yearly Average Precipitation'])
    plt.grid()
    plt.savefig(fname)
    #plt.show()