import requests
import csv



def get_text(url):    # request on page, get text, not html
    r = requests.get(url)
    return r.text


def write_csv(d):    # write data to csv file
    with open('liveinternet.csv', 'a') as f:
        order = ['name', 'url', 'descrip', 'view', 'percent']
        write = csv.DictWriter(f, fieldnames=order)
        write.writerow(d)


def main():

    for i in range(0, 100):
        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
        text_page = get_text(url)    # get text web page 
        text = text_page.strip().split('\n')[1:]    # delite all non use symbols, split string and non use 1st elem.list

        for eachstr in text:
            column = eachstr.strip().split('\t')    # decision str '\t' on elements 
            name = column[0]
            url = column[1]
            descrip = column[2]
            view = column[3]
            percent = column[4]

            data = {'name': name,    # pack in dictionary
                    'url': url,
                    'descrip': descrip,
                    'view': view,
                    'percent': percent}

            write_csv(data)    # dictionary write to csv



if __name__ == "__main__":
    main()