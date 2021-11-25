
# Selenium-Scrapping-Amazon

Scrapping Amazon Products along with their data using Python script through Selenium Automation. The script scrapes 10 products' data from one specific Category.



## Run Locally

Clone the project

```bash
  git clone https://github.com/varkha-yadav-7/Selenium-Scrapping-Amazon.git
```

Install Python 3.x and Chrome Webdriver for your version of chrome through the following link : 

https://sites.google.com/chromium.org/driver/downloads?authuser=0


Open terminal and enter the repository.

```bash
  cd Selenium-Scrapping-Amazon
```

Open selen.py file and set your path to chrome web driver file in line 4.


Run the script

```bash
  python3 selen.py
```




## Appendix

You can change the number of products you want to scrape upto 50 per category from line number 18 by changing the break value of loop in if statement. You can get items from different categories by changing the main link on line number 5. Given below is the main link for different categories for your convinience. You can open the category you want to use and change the link in line 5 accordingly.

https://www.amazon.in/gp/new-releases/apparel/ref=zg_bsnr_unv_%22a%22_1_11400137031_2

