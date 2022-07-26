# Blackboard Scraper
Script for locally downloading all files from your personal Blackboard page

## Requirements
- Python 3.9 or up
- Beautiful Soup 4
```
pip install beautifulsoup4
```

## Steps
1. Login to Blackboard
2. On the home page (where the course list is) right click anywhere on the screen and click "inspect" to open the developer tools
3. Look for the "Network" tab and open it
4. Refresh the page
5. You'll see a lot of requests appear. Find the first one and right click on it. 
6. Click copy then copy as cURL

<img width="524" alt="Screenshot 2022-07-26 at 20 33 22" src="https://user-images.githubusercontent.com/38282695/181096404-7a750c25-b67b-421a-a873-2ee65b77d2c9.png">

7. Go to https://curlconverter.com/ and paste the cURL request into it to get the request headers and cookies in Python
8. Copy the `headers` and `cookies` variables and paste them into `headers.py`
9. Go back to the Blackboard homepage and open the Console tab in the developer tools
10. Copy the contents of `getCourseLinks.js` and paste it into the console and press Enter.
11. Right click on the output and click "Copy Object"
12. Paste the object in place of `#PASTE HERE` in `course_links.py`
13. Save changes 
14. Run `python3 scrape.py` to start downloading
