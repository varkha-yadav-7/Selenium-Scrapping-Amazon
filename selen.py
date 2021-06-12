from selenium import webdriver
import time

driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.amazon.in/gp/new-releases/apparel/1968120031?ref_=Oct_s9_apbd_onr_hd_bw_b29C1vT_S&pf_rd_r=5BJNNT8P6QND2AQ8GWHP&pf_rd_p=8fc488c0-2d67-5093-afbc-cff5a926f4af&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1968120031")

k=driver.find_element_by_id("zg-center-div")
l=k.find_element_by_tag_name("ol")
t=l.find_elements_by_tag_name('li')
links=[]
for i in t:
	n=i.find_element_by_tag_name('a')
	link=n.get_attribute("href")
	links.append(link)

for i in links:
	Product={}
	if(links.index(i)==5):
		break;
	driver.get(i)
	a=driver.find_element_by_id("main-image-container")
	b=a.find_element_by_class_name("imgTagWrapper")
	img=b.find_element_by_tag_name('img')
	image=img.get_attribute('src')
	name=driver.find_element_by_id('productTitle').text
	desc=''
	price=''
	try:
		price=driver.find_element_by_id('priceblock_ourprice').text
		desc=driver.find_element_by_id('productDescription').text
	except:
		price=1000
	features=[]
	c=driver.find_element_by_id('feature-bullets')
	for j in c.find_elements_by_tag_name('li'):
		features.append(j.text)	
	Product['Name']=name
	Product['Description']=desc
	Product['Price']=price
	Product['img']=image
	Product['features']=features
	print(Product)
	print('\n\n')
driver.quit()


'''driver=webdriver.Chrome("/usr/local/bin/chromedriver 2")
driver.get('https://www.amazon.in/gp/new-releases/apparel/1968076031/ref=zg_bsnr_nav_%22a%22_2_1968024031')

k=driver.find_element_by_id("zg-center-div")
l=k.find_element_by_tag_name("ol")
t=l.find_elements_by_tag_name('li')
links=[]
for i in t:
	n=i.find_element_by_tag_name('a')
	link=n.get_attribute("href")
        links.append(link)
for i in links:
        if(links.index(i)==10):
            break
        driver.get(i)
        a=driver.find_element_by_id("main-image-container")
        b=a.find_element_by_class_name("imgTagWrapper")
        img=b.find_element_by_tag_name('img')
        image=img.get_attribute('src')
        name=driver.find_element_by_id('productTitle').text
        desc=''
        price=''
        try:
            price=driver.find_element_by_id('priceblock_ourprice').text
            desc=driver.find_element_by_id('productDescription').text
        except:
            price=1000
        features=[]
        c=driver.find_element_by_id('feature-bullets')
        for j in c.find_elements_by_tag_name('li'):
            features.append(j.text)	
        cat=Category.objects.get(name='Jeans')
        p=Product(name=name,description=desc,price=price,imgsrc=image,features=features,category=cat)
        p.save()
    driver.quit()'''
