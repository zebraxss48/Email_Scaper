# # Hacking Tool in python 

import requests
from bs4 import BeautifulSoup
import requests.exceptions
import urllib.parse
from collections import deque
import re


user_url = str(input("[+]Enter your target URL TO Scan: "))
urls = deque([user_url])  # All url will go into deques for checking

scrapped_url = set()  # All url will store in scrapped_url
email = set()  # All email wil go in email varibale

count = 0
try:
    while len(urls):
        count += 1
        if count == 100:  # count will stop will It will Reach 100
            break
        url = urls.popleft()   # scapped url from left side 
        scrapped_url.add(url)

        parts = urllib.parse.urlsplit(url)  # Just spliting the url
        base_url = "{0.scheme}://{0.netloc}".format(parts)   # This is a base location of a domain 

        path = url[:url.rfind("/")+1] if "/" in parts.path else url
        print('[%d] proccessing... %s' % (count, url))

        try:
            response = requests.get(url)

            new_emails = set(re.findall(r'[a-z0-9\. \-+_]+@[a-z0-9\. \-+]+\.[a-z]+', response.text, re.I))
            email.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scrapped_url:
                    urls.append(link)

        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # Handle the exception or perform any necessary actions
            continue


        # soup = BeautifulSoup(response.text, features="lxml")

#             for anchor in soup.find_all("a"):
#                 link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
#                 if link.startswith('/'):
#                     link = base_url + link
#                 elif not link.startswith('http'):
#                     link = path + link
#                 if not link in urls and not link in scrapped_url:
#                     urls.append(link)
        
except KeyboardInterrupt:
    print('[-] Closing...')
    for mail in email:
        print(mail) 


# ... (your imports)

# user_url = str(input("[+] Enter your target URL TO Scan: "))
# urls = deque([user_url])  # All URLs will go into deques for checking
# scrapped_url = set()  # All URLs will be stored in scrapped_url
# email = set()  # All emails will go in the email variable

# count = 0
# try:
#     while len(urls):
#         count += 1
#         if count == 100:  # count will stop will It will Reach 100
#             break
#         url = urls.popleft()  # scrapped URL from the left side
#         scrapped_url.add(url)

#         parts = urllib.parse.urlsplit(url)  # Just splitting the URL
#         base_url = "{0.scheme}://{0.netloc}".format(parts)  # This is the base location of a domain

#         path = url[:url.rfind("/") + 1] if "/" in parts.path else url
#         print('[%d] processing... %s' % (count, url))

#         try:
#             response = requests.get(url)

#             new_emails = set(re.findall(r'[a-z0-9\. \-+_]+@[a-z0-9\. \-+]+\.[a-z]+', response.text, re.I))
#             email.update(new_emails)

#             soup = BeautifulSoup(response.text, features="lxml")

#             for anchor in soup.find_all("a"):
#                 link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
#                 if link.startswith('/'):
#                     link = base_url + link
#                 elif not link.startswith('http'):
#                     link = path + link
#                 if not link in urls and not link in scrapped_url:
#                     urls.append(link)

#         except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
#             # Handle the exception or perform any necessary actions
#             continue

# except KeyboardInterrupt:
#     print('[-] Closing...')
#     for mail in email:
#         print(mail)
