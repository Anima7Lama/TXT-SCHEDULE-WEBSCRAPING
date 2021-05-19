from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#from django.views.generic.base import View
#from .models import ScrapedData

# Create your views here.
url = 'https://ibighit.com/txt/eng/schedule/?year=2021&month=2&day=1'

page = requests.get(url)
#print out the HTML content of the page using the content property
htmlContent = page.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

schedules = soup.find_all('li', class_ = "valign broadcast")
#print(schedules)
#    
def home(request):
    # global Schedule
    Schedule = {}
    test_dates = []
    timetable = []
    activities = []

    for schedule in schedules:
        date = schedule.find_parent('div').get('id')
        test_dates.append(date)
        times = schedule.find_all('div', class_ = "time")
        for time in times:
            Time = time.get_text()
            timetable.append(Time)
        contents = schedule.find_all('div', class_ = "contents-inner")
        for activity in contents:
            Activity = activity.get_text()
            activities.append(Activity)

    # filtering out none elements from the list
    text_dates = list(filter(None, test_dates)) 
    filtered_dates = []
    for i in text_dates:
        dates = i.strip('schedule') #clear out the schedule to store the date only
        date = dates[:4] + '-' + dates[4:6]+ '-' + dates[-2:] #insert hash for the datetime format
        filtered_dates.append(date)

    """print(Dates)
    print(timetable)
    print(activities)"""
    days = []
    for i in filtered_dates:
        day = pd.Timestamp(i)
        days.append(day.day_name())

    Schedule = {
        'Dates' : filtered_dates,
        'Days' : days,
        'Time' : timetable,
        'Tasks' : activities
    }
    print(Schedule)
    #print(schedule)
    return render(request, 'index.html', Schedule)

def post(request):
    pass

    