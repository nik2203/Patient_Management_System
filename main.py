import urllib, tkinter, time, random, csv

def take_url(n,urllist):
    for i in range(n):
        x=input('Enter the YouTube URL\n')
        if (verify_url(x)):
            urllist.append(x)
            print('URL successfully added to the list')
        else:
            print('The URL',x,'is an invalid URL and was not added')
    return

def verify_url(url):
    if url.startswith('https://www.youtube.com/') or url.startswith('http://youtu.be/'):
        return True
    else:
        return False

'''
def del_url(url):
'''

def load_url(*args):
    for i in args:
        if i.startswith('https://www.youtube.com/') or i.startswith('http://youtu.be/'):
            url=i
            return url
        elif i in title_list:
            title=i
            return title
        else:
            print('Invalid input')
            return

def pick_categ(categ):
    with open(categ,'r') as categ_file:
        lurl=csv.reader(categ_file)


def rand_url(fh):
    urls=fh.readlines()
    for i in urls:
        i=i.strip('\n')
    alarm_tune=random.choice(urls)

