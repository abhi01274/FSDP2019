

from selenium import webdriver
import matplotlib.pyplot as plt
lnk = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(lnk)

A=[]
D=[]


for x in range(1,7):
    value= browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(x)+']/td[5]').text.strip()
    state= browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(x)+']/td[2]/a').text.strip()
    A.append(value)
    D.append(state)



colors= ['gold','green','lightcoral','lightskyblue']
explode= (0.2,0,0,0,0,0)
plt.pie(A,explode=explode,labels=D, colors=colors,autopct='%2.2f%%',shadow=True)