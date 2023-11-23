import requests
from bs4 import BeautifulSoup

def get_jobs(location, title, page=1):
    loc = location.replace(' ', '+')
    page_num = (page - 1) * 10
    base_url = f"https://www.indeed.com/jobs?q={title}&l&={loc}start="
    url = f"{base_url}{page_num}"
    page = requests.get(url)
    print(url)
    print(page.status_code)
    return page

def prese_info(soup):
    results = soup.find(id="resultsCol")
    if results:
        jobs = results.find_all('div', class_="jobsearch-SerpJobCard")
        job_list = []
        ID = 0
        for job in jobs:
            base_url = 'https://www.indeed.com'
            title = job.find('h2').find('a')['title']
            link = base_url + job.find('h2').find('a')['href']
            location = job.find(class_='location').text
            ID += 1
            job_list.append({
                'ID': ID,
                'title': title,
                'location': location,
                'link': link,
            })
        return job_list
    else:
        print("Aucun résultat trouvé.")
        return []

if __name__ == "__main__":
    page = get_jobs("New York", "python", 2)
    soup = BeautifulSoup(page.content, features="lxml")
    results = prese_info(soup)
    print(results)

