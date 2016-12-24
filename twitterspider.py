import requests
import json
import urllib
import re
from bs4 import BeautifulSoup
from config import USERNAME, PASSWORD

def twitter_login(user, pw, user_agent):
    """Start a requests session and login to Twitter with credentials.
    Returned object is logged-in session."""
    
    tw_url = "https://twitter.com/"
    session = requests.session()
    first_req = session.get(tw_url)

    auth_token_str = re.search(r'<input type="hidden" value="([a-zA-Z0-9]*)" name="authenticity_token"\>',
          first_req.text)
    authenticity_token = auth_token_str.group(1)

    login_url = 'https://twitter.com/sessions'
    
    payload = {
        'session[username_or_email]' : user,
        'session[password]' : pw,
        'remember_me' : '1',
        'return_to_ssl' : 'true',
        'scribe_log' : None,
        'redirect_after_login':'/',
        'authenticity_token': authenticity_token
    }

    login_req = session.post(login_url, data=payload, headers=user_agent)
    print("twitter登录状态: ", login_req.status_code)

    return session

user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    
session = twitter_login(USERNAME, PASSWORD, user_agent)

def spider(twitter_name, limit=99):
    dic={}
    link='https://twitter.com/' + twitter_name
    response=session.get(link)
    html=response.text
    soup=BeautifulSoup(html, "html.parser")

    avatarimage=soup.select('.ProfileAvatar-image')[0].get('src')
    tags=soup.select('li')

    
    for tag in tags:
        message=''
        pics=[avatarimage]
              
        if len(tag.select('.TweetTextSize '))>0:
            if tag.select('p')[0].text!=tag.select('.TweetTextSize ')[0].text:
                message=tag.select('p')[0].text+tag.select('.TweetTextSize ')[0].text
            else:
                message=tag.select('p')[0].text
            if len(tag.select('.QuoteTweet-text'))>0:
                message=message+tag.select('.QuoteTweet-text')[0].text
                for each in tag.select('.QuoteMedia-photoContainer'):
                    pics.append(each.get('data-image-url'))
            if len(tag.select('.AdaptiveMedia-photoContainer'))>0:
                for each in tag.select('.AdaptiveMedia-photoContainer'):
                    pics.append(each.get('data-image-url'))
            if re.search(r'[\u3041-\u30F6\u4E00-\u9FA0]',message)!=None:
                dic[message]=pics
        if len(dic)+1>limit:
            return dic            


