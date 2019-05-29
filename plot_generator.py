from data_processor import *
from global_variables import *
import matplotlib.pyplot as plt
if not os.path.exists('pics/'):
    os.makedirs('pics/')


# Parameter
city = 'KSAN'
fname = 'pics/{}/highest_temperature/all_plot.jpg'.format(city)
# Code
start_year = 1990
end_year = 2019
yearly_avg_temp_list = []
for year in range(start_year, end_year + 1):
    year_start, year_end = get_yearly_start_end(year=year)
    weather_info = get_info(city, year_start, year_end, info_type='highest temperature', output=False)
    yearly_avg_temp_list.append(weather_info['mean'])
print(yearly_avg_temp_list)

# plot
plt.figure(figsize=(20, 10))
plt.plot(range(start_year, end_year), yearly_avg_temp_list[:-1])
title_str = '{}\'s Yearly Highest Temperature Situation in All years'.format(code_city_refer[city])
plt.xlabel('Year')
plt.ylabel('Fahrenheit')
plt.title(title_str, fontsize='xx-large', fontweight='bold')
plt.grid()
plt.savefig(fname)