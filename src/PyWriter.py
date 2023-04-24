from selenium import webdriver 
import time 
from selenium.webdriver import ActionChains
from pynput.keyboard import  Controller
from os import environ, system, name
from colorama import *
from sub import main
from json import dump, load, dump
import pwinput
from selenium.webdriver.common.by import By



def clear():
    clearer = "clear"
    if name == "cmd" or "dos":
        clearer = "cls"
    else:
        pass
    system(clearer)
clear()
main.helloscreen()





FILE = open("src/data/logindata.json")
FILE_ = load(FILE)

while True:
    print(Fore.YELLOW + "Do you want to use log-in data from last session? " + Style.RESET_ALL)
    answer = input("(yes/no): ")
    if answer == "yes":
        username = FILE_["username"]
        password = FILE_["password"]
        break
    
    if answer == "Yes":
        username = FILE_["username"]
        password = FILE_["password"]
        break

    if answer == "no":
        username = input('Enter your username: ')         ### Log-in Data
        password = str(pwinput.pwinput(prompt='Enter your password: ', mask="*"))
        json_temp = {
        "username":str(username),
        "password":str(password)
        }
        with open("src/data/logindata.json", "w+", encoding="utf8") as f:
            dump(json_temp, f, indent=2)
        f.close()
        break

    elif answer == "No":
        username = input('Enter your username: ')        ### Log-in Data
        password = pwinput.pwinput(prompt='Enter your password: ', mask="*")
        json_temp = {
        "username":str(username),
        "password":str(password)
        }
        with open("src/data/logindata.json", "w+", encoding="utf8") as f:
            dump(json_temp, f, indent=2)
        f.close()
        break

    if answer.isnumeric == True:
        print(Fore.RED + "Please use a valid answer! " + Style.RESET_ALL)
        time.sleep(1.5)

    if answer.isalnum == True:
        print(Fore.RED + "Please use a valid answer! " + Style.RESET_ALL)
        time.sleep(1.5)


clear()


while True:
    clear()
    main.helloscreen()
    zeit = input(Fore.LIGHTGREEN_EX +"Time in Seconds for 1 Word: " + Style.RESET_ALL)     ### Speed of Typing.
    
    if zeit.isalpha() == True:
        print(Fore.RED + "Please type in a number!" + Style.RESET_ALL)
        time.sleep(2)
        clear()
        main.helloscreen()
        
    else:
        zeit1= zeit.replace(',','.')
        print(zeit1)
        break



environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

### Define Chrome-driver.
driver = webdriver.Chrome("src\chromedriver.exe")
keyboard = Controller()



driver.get('https://at4.typewriter.at/index.php?r=typewriter/runLevel')         ### Starting driver(chrome) and logging in.
driver.maximize_window()

time.sleep(3)

userlog = driver.find_element(By.ID, "LoginForm_username")
passwordlog = driver.find_element(By.ID, "LoginForm_pw")



userlog.send_keys(username)             ### Initialising User log-in.
passwordlog.send_keys(password)

log_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/form/div[3]/input")
log_button.click()
time.sleep(5)
runlevelB = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/a/div[2]/b")
runlevelB.click()
time.sleep(2)


def main():
    while True:
        keyboard.press('a')
        keyboard.release('a')
       
        time.sleep(1)
        ###schreibt
        text1c = driver.find_element(By.ID, "text_todo")
        text1= text1c.text
        text1l = list(text1)
        print(text1l[0])
        
        time.sleep(0)

        keyboard.press(text1l[0])
        keyboard.release(text1l[0])

        long = driver.find_element(By.ID, "amountRemaining")
        longt =long.text
        print (longt)
        
        for x in range(int(longt)):
            text1c = driver.find_element(By.ID, "text_todo")
            text1= text1c.text
            text1l = list(text1)
            keyboard.press(text1l[0])
            keyboard.release(text1l[0])
            time.sleep(float(zeit1))
            

                    
            

        time.sleep(2)
        print("Level complete")
        driver.back() 
        
        
        clear()

if __name__ == "__main__":
    main()
