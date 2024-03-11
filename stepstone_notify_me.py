from plyer import notification  # Import the notification module from plyer

import schedule
def notifyme():
    notification.notify(
        title="New Job Posting",
        message="A new job posting is available!",
        app_icon=None,
        timeout=10
    )






import time
def get_previous_state():
    try:
        with open("webpage_state.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def save_state(state):
    with open("webpage_state.txt", "w") as file:
        file.write(state)
def program():
  def webscraping():
      import bs4
      import requests
      response = requests.get(url="https://www.stepstone.de/jobs/praktikum-informatik?rsearch=1")
      from bs4 import BeautifulSoup
      soup = BeautifulSoup(response.text, 'html.parser')
      body_element = soup.body
      first_article = soup.find('article')
      global stats
      stats = first_article.get('class')
      return stats
  save_state(webscraping())
  def checkingforupdates():
      if webscraping()!= get_previous_state():
          notifyme()
          save_state(webscraping())

schedule.every(30).minutes.do(program)



    
    



  
  

    





# Find the body element and print its text content
   

   
   
   
   








  
  
     




