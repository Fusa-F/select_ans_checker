from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time, sys

# private setting file
try:
    from local_settings import *
except:
    print('Import Error')
    sys.exit()

driver = webdriver.Chrome(driver_path)

# login-page
driver.get(url)

# ! private !
u = username
p = password

# login
username = driver.find_element_by_name('j_username')
username.send_keys(u)
password = driver.find_element_by_name('j_password')
password.send_keys(p)
btn = driver.find_element_by_class_name('btn-primary')
btn.click()

# choose course
course = driver.find_element_by_id("gncourse")
course.click()
courselist = driver.find_element_by_xpath('//*[@id="gncoursemenu"]/ul/li[1]/a')
courselist.click()

class_name = driver.find_element_by_id(class_name_id)
class_name.click()
class_num = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(class_num_id))
class_num.click()
exercise = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(exercise_id))
exercise.click()
test = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(test_path))
test.click()

# answer check
question_num = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector(
    '#exerciseOrderList > tbody > tr > td:nth-child(' + str(question_num) + ') > .symbolLabel > a'
))
question_num.click()

select = []
for i in range(select_num):
    select.append(Select(WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(select_id[i]))))

submit = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('answerSubmitButton'))

# check loop (N=4)
flg = False
for i in range(value_num):
    select[0].select_by_index(i)
    for j in range(value_num):
        select[1].select_by_index(j)
        for k in range(value_num):
            select[2].select_by_index(k)
            for l in range(value_num):
                select[3].select_by_index(l)
                time.sleep(1) # delay
                try :
                    submit.click()
                except StaleElementReferenceException:
                    flg = True
                    print(i)
                    print(j)
                    print(k)
                    print(l-1)
                    break
            if flg:
                break
        if flg:
            break
    if flg:
        break

driver.quit()