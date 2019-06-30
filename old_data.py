from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# link = 'http://suninjuly.github.io/find_xpath_form'
# link = "http://suninjuly.github.io/find_link_text"
# browser = webdriver.Chrome()
# browser.get(link)

# link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
# link.click()

# input1 = browser.find_element_by_tag_name('input')
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_name('last_name')
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_class_name('city')
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id('country')
# input4.send_keys("Russia")
# button = browser.find_element_by_xpath("//button[text()='Отправить']")
# button.click()

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/huge_form.html")
# elements = browser.find_elements_by_tag_name('input')
# for element in elements:
#     element.send_keys("Мой ответ")
#
# button = browser.find_element_by_css_selector("button.btn")
# button.click()



# links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
#
#
# for link in links:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
#     input1.send_keys("some_name")
#
#     input2 = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
#     input2.send_keys("some_second_name")
#
#     input3 = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
#     input3.send_keys("some_mail")
#
#     input4 = browser.find_element_by_xpath("//input[@placeholder='Введите телефон:']")
#     input4.send_keys("some_phone")
#
#     input5 = browser.find_element_by_xpath("//input[@placeholder='Введите адрес:']")
#     input5.send_keys("some_address")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
#     browser.close()


# link = "http://suninjuly.github.io/math.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id('input_value')
# x = x_element.text
# y = calc(x)
#
# answer = browser.find_element_by_id('answer')
# answer.send_keys(y)
#
# checkbod = browser.find_element_by_id('robotCheckbox')
# checkbod.click()
#
# radio = browser.find_element_by_id('robotsRule')
# radio.click()
#
# button = browser.find_element_by_css_selector("button.btn")
# button.click()


# link = "http://suninjuly.github.io/get_attribute.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# gold = browser.find_element_by_id('treasure')
# valuex = gold.get_attribute('valuex')
# y = calc(valuex)
#
# answer = browser.find_element_by_id('answer')
# answer.send_keys(y)
#
# checkbod = browser.find_element_by_id('robotCheckbox')
# checkbod.click()
#
# radio = browser.find_element_by_id('robotsRule')
# radio.click()
#
# button = browser.find_element_by_css_selector("button.btn")
# button.click()



# link = "http://suninjuly.github.io/selects1.html"
# browser = webdriver.Chrome()
# browser.get(link)


# browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("option:nth-child(46)").click()
# browser.find_element_by_css_selector("[value='19']").click()

# num1 = browser.find_element_by_id('num1').text
# num2 = browser.find_element_by_id('num2').text
#
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value(str(int(num1) + int(num2)))
#
# button = browser.find_element_by_css_selector("button.btn").click()

#
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")

# browser = webdriver.Chrome()
# link = "https://suninjuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()
# assert True


# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id('input_value').text
#
# answer = browser.find_element_by_id('answer')
# answer.send_keys(calc(x_element))
#
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#
# radio = browser.find_element_by_id('robotsRule')
# radio.click()
#
# checkbod = browser.find_element_by_id('robotCheckbox')
# checkbod.click()
#
#
# button.click()


# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/alert_accept.html"
# browser.get(link)
#
#
# button = browser.find_element_by_tag_name("button")
# button.click()
#
# alert = browser.switch_to.alert
# alert.accept()
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id('input_value').text
#
# answer = browser.find_element_by_id('answer')
# answer.send_keys(calc(x_element))
# button = browser.find_element_by_tag_name("button").click()

#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/redirect_accept.html"
# browser.get(link)
#
#
# button = browser.find_element_by_tag_name("button")
# button.click()
#
# browser.switch_to.window(browser.window_handles[1])
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id('input_value').text
#
# answer = browser.find_element_by_id('answer')
# answer.send_keys(calc(x_element))
# button = browser.find_element_by_tag_name("button").click()


#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element_by_id("check")
# button.click()
# message = browser.find_element_by_id("check_message")
#
# assert "успешно" in message.text


# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("check")
# button.click()
# message = browser.find_element_by_id("check_message")
#
# assert "успешно" in message.text


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
button = browser.find_element_by_id("book")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_id('input_value').text

answer = browser.find_element_by_id('answer')
answer.send_keys(calc(x_element))
button = browser.find_element_by_id("solve").click()
