from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://internshala.com/internships/data%20science-internship"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div', class_="internship_meta")

url2 = "https://internshala.com/internships/data%20science-internship/page-2"
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content,'html.parser')
lists2 = soup2.find_all('div', class_="internship_meta")

url3 = "https://internshala.com/internships/data%20science-internship/page-3"
page3 = requests.get(url3)
soup3 = BeautifulSoup(page3.content,'html.parser')
lists3 = soup3.find_all('div', class_="internship_meta")



with open('DataScience_internships.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header=['Field','Company','Location','Duration','Stipend','Apply_by']
    thewriter.writerow(header)
    for list in lists:
        Field = list.find('a', class_="view_detail_button").text
        Company = list.find('a', class_="link_display_like_text view_detail_button").text.replace('\n','').strip()
        Location = list.find('a', class_="location_link view_detail_button").text
        Duration = list.find('div', class_="item_body").find_next('div').text.replace('\n','').replace('Duration','').strip()
        Stipend = list.find('span', class_ ="stipend").text
        Apply_by = list.find('div', class_="item_body").find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').text
        info1 = [Field,Company,Location,Duration,Stipend,Apply_by]
        thewriter.writerow(info1)

    
    for list in lists2:
        Field = list.find('a', class_="view_detail_button").text
        Company = list.find('a', class_="link_display_like_text view_detail_button").text.replace('\n','').strip()
        Location = list.find('a', class_="location_link view_detail_button").text
        Duration = list.find('div', class_="item_body").find_next('div').text.replace('\n','').replace('Duration','').strip()
        Stipend = list.find('span', class_ ="stipend").text
        Apply_by = list.find('div', class_="item_body").find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').text
        info2 = [Field,Company,Location,Duration,Stipend,Apply_by]
        thewriter.writerow(info2)
    
    for list in lists3:
        Field = list.find('a', class_="view_detail_button").text
        Company = list.find('a', class_="link_display_like_text view_detail_button").text.replace('\n','').strip()
        Location = list.find('a', class_="location_link view_detail_button").text
        Duration = list.find('div', class_="item_body").find_next('div').text.replace('\n','').replace('Duration','').strip()
        Stipend = list.find('span', class_ ="stipend").text
        Apply_by = list.find('div', class_="item_body").find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').find_next('div').text
        info3 = [Field,Company,Location,Duration,Stipend,Apply_by]
        thewriter.writerow(info3)
   
