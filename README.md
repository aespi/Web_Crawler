# Web_Crawler
A web crawler in python 3 using scrapy to extract the text of all &lt;P> tags from any website and its subpages.

To use this web Crawler. You need to install python 3 in your pc 
now install scrapy with following command in cmd: pip install Scrapy for installation guide please visit: https://doc.scrapy.org/en/latest/intro/install.html 
after that download the folder of Paragraph_Extracter. 
In CMD: navigate to the Dirctory of Paragraph_Extacter. 
after that type in this command to run the crawler: 
scrapy crawl paragraphs -a url="<url_of_the_site_you_want_to_crawl" 
the output will be stored in the same directory in json format

URL must start from http://..... and must not include 'www'




^^^You can change the Seperator for Paragraphs in Json File from /Paragraph_extracter/spiders/paragraphs.py file and change the sep variable to any Seperator you want.^^^
