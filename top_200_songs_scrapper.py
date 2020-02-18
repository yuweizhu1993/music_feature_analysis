# scrapping top 200 daily songs using fycharts
from fycharts.SpotifyCharts import SpotifyCharts

region_list = ['ca', 'dk', 'gr', 'is', 'mx', 'ph', 'sv',
               'ar', 'ch', 'do', 'gt', 'it', 'my', 'pl', 'th',
               'at', 'cl', 'ec', 'hk', 'jp', 'ni', 'pt', 'tr',
               'au', 'co', 'ee', 'hn', 'lt', 'nl', 'py', 'tw',
               'be', 'cr', 'es', 'hu', 'lu', 'no', 'ro', 'us',
               'by', 'cy', 'fi', 'id', 'lv', 'nz', 'se', 'uy',
               'bo', 'cz', 'fr', 'ie', 'mc', 'pa', 'sg', 'vn',
               'br', 'de', 'gb', 'il', 'mt', 'pe', 'sk', 'global']

week_list = []
with open('week_list.txt', 'r') as fin:
    for line in fin:
        week_list.append(line.strip())

def main():
    for region in region_list:
        for i in range(len(week_list)):
            api = SpotifyCharts()
            file_name ='./data/' + region +'.csv'
            api.top200Daily(output_file = file_name, region = [region],
                            start = week_list[i], end = week_list[i])

if __name__ == "__main__":
    main()