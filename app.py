from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    username = request.form['username']
    twitter_url = f'https://twitter.com/{username}'

    # Send a GET request to the Twitter page
    response = requests.get(twitter_url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Perform scraping and extract the required information
    # Replace the following code with your scraping logic
    tweet_ids = [tweet['data-tweet-id'] for tweet in soup.select('div[data-tweet-id]')]
    tweet_urls = [tweet['data-permalink-path'] for tweet in soup.select('div[data-permalink-path]')]
    tweet_texts = [tweet.text for tweet in soup.select('div.tweet-text')]
    # ... extract other information ...
    # css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0
    # css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0

    # Generate the HTML to display the scraped data
    result_html = "<h2>Scraped Data for User: " + username + "</h2>"
    result_html += "<h3>Tweet IDs:</h3>"
    result_html += "<ul>"
    for tweet_id in tweet_ids:
        result_html += "<li>" + tweet_id + "</li>"
    result_html += "</ul>"
    # ... generate HTML for other information ...

    return result_html

if __name__ == '__main__':
    debug=True
    app.run()
