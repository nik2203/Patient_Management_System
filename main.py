import urllib, tkinter, time, random

def take_url(n,urllist):
    for i in range(n):
        x=input('Enter the YouTube URL\n')
        if (verify_url(x)):
            urllist.append(x)
            print('URL successfully added to the list')
        else:
            print('The URL',x,'is an invalid URL and was not added')
    return x

def verify_url(url):
    if url.startswith('https://www.youtube.com/'):
        return True
    else:
        return False

'''
def del_url()

def load_url()

def categ()

def pick_categ()
'''

def rand_url(fh):
    urls=fh.readlines()
    for i in urls:
        i=i.strip('\n')
    alarm_tune=random.choice(urls)