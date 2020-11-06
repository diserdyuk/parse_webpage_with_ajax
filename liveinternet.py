import requests
import csv



def get_text(url):    # request on page, get text, not html
    r = requests.get(url)
    return r.text


def write_csv(d):    # write data to csv file
    with open('liveinternet.csv', 'a') as f:
        order = []
        write = csv.DictWriter(f, fieldnames=order)
        write.writerow(d)


def main():
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page=2'
    text_page = get_text(url)    # get text web page 
    text = text_page.strip().split('\n')[1:]    # delite all non use symbols, split string and non use 1st elem.list
    print(text) 



if __name__ == "__main__":
    main()