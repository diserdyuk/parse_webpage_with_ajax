import requests
import csv



def get_text(url):    # request on page, get text, not html
    r = requests.get(url)
    return r.text


def write_csv(d):    # write data to csv file
    with open('liveinternet.csv', 'a') as f:
        write = csv.writer(f)
        pass



def main():
    pass



if __name__ == "__main__":
    main()