# # import tkinter as tk
# # from tkinter import filedialog
# # import time
# # def takeScreenshot():
# #     im1 = pyautogui.screenshot()
# #     im2 = filedialog.asksaveasfilename(defaultextension='.png')
# #     im1.save(im2)
# # a = input("Take screen shot=")
# # if a=='y':
# #   time.sleep(5)
# #   takeScreenshot()
# # import pyautogui
# # pyautogui.displayMousePosition()
# import webbrowser
# import time
import pyautogui
from pyautogui import hotkey ,typewrite ,click,prompt,password
# from selenium import webdriver
# import time

# driver = webdriver.Chrome()  
# driver.maximize_window()  
# driver.get("https://www.instagram.com/")  
# driver.find_element_by_name("username").send_keys("jha36binayak@gmail.com")
# driver.find_element_by_name("password").send_keys("livenews123")
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)    
# # a=prompt(text="enter username",title="username")
# # b=password(text='enter password', title='password(will not be saved)', default='', mask='*')
# # email = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# # email.send_keys(a)
# # passw = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
# # passw.send_keys(b)
# # submit = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
# # submit.click()
from selenium import webdriver  
import time  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
a=prompt(text="enter the username",title="Username")
b=password(text="enter the password",title="Password(safe)",mask="*")
driver = webdriver.Chrome(executable_path=r'C:\Users\Laptop-16\Desktop\python\chromedriver')
driver.get('https://instagram.com/')

#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()
#navigate to the url  
#identify the Google search text box and enter the value  
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(a)  
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(b)    
#click on the Google search button  
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)  
time.sleep(3)  
#close the browser  
# driver.close()  
print("sample test case successfully completed")  
