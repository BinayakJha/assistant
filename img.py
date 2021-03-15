import requests
from bs4 import BeautifulSoup

URL = "https://classroom.google.com/u/0/c/MTc1NjQyNTExNjg3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
job_elems = soup.find_elements_by_class_name("hrUpcomingAssignmentGroup").get_text()
print(job_elems)
