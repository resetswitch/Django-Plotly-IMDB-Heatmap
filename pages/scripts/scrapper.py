import re
import os
import sys
import time
from datetime import datetime
import random

import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

from . import classes as c


def requestContent(URL):
    try:
        request_1 = requests.get(URL)
        request_1.raise_for_status()
    except requests.exceptions.RequestException as e:
        sys.exit("Most Likely you are being Denied for too many Connections at once, please try another TV Show or change to a VPN")
    return request_1.content


def imdbScrapper(IMDB_URL):
    result = c.Data()
    try:
        # In the event of IMDB giving a 400 code when scrapping 'byseasons', we can scrap 'byyear' instead.
        slash_list = []
        title_tt = re.findall('tt\d{7}', IMDB_URL)[0]

        base_URL = "https://www.imdb.com"

        base_content = requestContent(base_URL+"/title/"+title_tt)
        base_soup = BeautifulSoup(base_content, 'html.parser')

        if "TV" and "Series" in base_soup.find('div', class_="subtext").text:
            pass
        else:
            result.error = True
            result.error_message = "IMDB link is not an IMDB TV show"
            return(result)

        soup_isy = base_soup.find("div", class_ = "seasons-and-year-nav")
        isy_urls_ext = [a['href'] for a in soup_isy.find_all('a', href=True) if a.text]

        ini_reqsts = 0
        scrap_type = None
        print("Attempting to Establish a good connection..")
        for isy_url_ext in isy_urls_ext:
            status = requests.get(base_URL+isy_url_ext).status_code
            ini_reqsts+=1
            print("Requests {} of possible {} ; status code {}\nURL {}".format(ini_reqsts, len(isy_urls_ext), status, base_URL+isy_url_ext))
            if status == 200:
                time.sleep(random.randint(8,15))
                if isy_url_ext.find("year") != -1:
                    scrap_type = "year"
                    break
                elif isy_url_ext.find("season") != -1:
                    scrap_type = "season"
                    break
            else:pass

        check_content = requestContent(base_URL+isy_url_ext)
        check_soup = BeautifulSoup(check_content, 'html.parser')

        # All the years or seasons found on IMDB for a certain show
        if scrap_type == "year" :
            years_or_seasons = check_soup.find("select", id = "byYear").text.split()
        elif scrap_type == "season" :
            years_or_seasons = check_soup.find("select", id = "bySeason").text.split()

        scrapping_URL = "https://www.imdb.com/title/{}/episodes?{}=".format(title_tt,scrap_type)#Able to limit to certain seasons if necessary

        # Due to psuedo crawling, this does not find the next URL in the HTML soup, but rather takes advantage of a URL pattern
        #   by appending a number to the end of the URL. In this case, we need to initialize the first URL
        initial_content = requestContent(scrapping_URL+years_or_seasons[0])
        initial_soup = BeautifulSoup(initial_content, 'html.parser')
        show_title = " ".join(initial_soup.find("h3", itemprop="name").text.split())

        # Where all the data will be stored ['SX', 'EX','Episode Title','Rating', 'Votes']
        data = []

        # Gives User a sense of progression
        reqsts = 0

        # episode number overall
        et = 0

        # Runs through each season
        for year_or_season in years_or_seasons: #year_or_season in years_or_seasons
            
            # Passes any season with the literal season number of 'Unknown'
            if year_or_season == 'Unknown':print("Year or Season # is 'Unknown'\nThis season has been skipped");continue
            else:pass
            
            # To prevent blockage of IP Address due to too many reqeusts
            time.sleep(random.randint(1,5))
            eta = ((len(years_or_seasons)-(reqsts+1 ))*((1+5.0)/2))
            
            # Gathering the Soup
            URL  = scrapping_URL+"{}".format(year_or_season)
            page_content = requestContent(URL)
            soup = BeautifulSoup(page_content, 'html.parser')
            
            # Monitor the requests
            reqsts += 1
            print('Request:{} of {} made on {}; est. time remaining: {}s'.format(reqsts, len(years_or_seasons), time.ctime(time.time()), eta))

            # Soup Extractions
            try:
                sx_ex                = [i.text.split() for i in soup.find_all("div", class_ = "image")]                   #finds all seasons and episodes ['S1', 'Ep2']
                for i, elem in enumerate(sx_ex):                #reduces lists that look like this: ['Add', 'Image', 'S2,', 'Ep2'], to this ['S1', 'Ep2']
                    if elem[0].lower() == "Add".lower() and len(elem) == 4:
                        sx_ex[i] = elem[2:]
                title                = [i.text.strip() for i in soup.find_all("a", itemprop = "name")]                    #finds all titles "Pilot"
                rating_and_votes     = [i.text.split() for i in soup.find_all("div", class_ = ["ipl-rating-star small","ipl-rating-star--placeholder"])]
                for i, elem in enumerate(rating_and_votes):
                    if len(elem)   == 2:pass
                    elif len(elem) == 1:
                        elem.append("(1)")
                        rating_and_votes[i]=elem
                    elif len(elem) == 0:
                        rating_and_votes[i]=["N/A","N/A"]
                description          = [i.text.strip() for i in soup.find_all("div", class_ = "item_description")]        #finds all descriptions
                
                air_date             = []
                dates                = [i.text.strip().replace(".","") for i in soup.find_all("div", class_ = "airdate")]
                for date in dates:
                    for dt_format_opt, dt_reformat_to in [["%b %Y","%m/01/%Y"], ["%Y", "01/01/%Y"], ["%d %b %Y","%m/%d/%Y"]]:
                        try:
                            air_date.append(datetime.strptime(date, dt_format_opt).strftime(dt_reformat_to))
                        except:pass                 #finds all air_dates 
            except ValueError:
                print("{} {} (Is In Progress/Has Not Released/Has No Ratings Data Available)\n{} {} has been skipped.".format(scrap_type.capitalize(), year_or_season,scrap_type.capitalize(), year_or_season))
                continue
                
            
            
            
            # Combining Soup Extractions into data
            if len(sx_ex) != len(rating_and_votes):
                print("{} {} (Is In Progress/Has Not Released/Has No Ratings Data Available)\n{} {} has been skipped.".format(scrap_type.capitalize(), year_or_season,scrap_type.capitalize(), year_or_season))
            else:
                for i in range(0, len(sx_ex)):
                    et+=1
                    data.append([
                                et,
                                re.sub('\D', '', sx_ex[i][0]), 
                                re.sub('\D', '', sx_ex[i][1]), 
                                title[i], 
                                rating_and_votes[i][0], 
                                rating_and_votes[i][1].replace("(","").replace(")",""),
                                air_date[i],
                                description[i]
                                ])
        # If data is emtpy
        if not data:
            result.error = True
            result.error_message = "{} does not have full season ratings".format(show_title)
            return result

        # Creating and saving Dataframe 
        df = pd.DataFrame(data,columns=['ET','SX', 'EX','Episode Title','Rating', 'Votes', 'Air Date','Description'])
        result.DataFrame_title = show_title.replace('–','-') + " - IMDB"
        result.DataFrame = df
        return result
    except:
        result.error = True
        result.error_message = "An error occurred when trying to connect to IMDB"
        return result

