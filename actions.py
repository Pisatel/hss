from selenium import webdriver
import pickle
driver = webdriver.Chrome()
from time import sleep

def open_url(url):
    driver.get(url)
    driver.delete_all_cookies()
    cookie = {'name':'hprchs_vstr_hsh', 'value':'srv59b3114f33f477.62624386'
              }
    driver.add_cookie(cookie)
    # coc = driver.get_cookie('hprchs_vstr_hsh')
    # print coc

def click_button_on_home_promo_by_class(class_name):
    buttons= driver.find_elements_by_xpath('//div[@id="home_promo"]//a[@class="%s"]' %class_name)
    if buttons:
        buttons[0].click()

    else:
        raise ValueError('Buy button not found')


def select_plan(plan_name):
    plans = driver.find_elements_by_xpath('//div[contains(@id, "%s")]' %plan_name)
    if plans:
        plans[0].click()
    else:
        raise ValueError('Plan button not found')
    # try:
    #     plans = driver.find_elements_by_xpath('//div[contains(@id, "%s")]' % plan_name)
    #     if plans:
    #         plans[0].click()
    #     else:
    #         raise ValueError('Plan button not found')


def payment_form():
    form_data = {
        'Card_num':['data_cc_num', '4111111111111111'],
        'Name_on_Card':['data_cardholdername', 'Pupsen Vupsen'],
        'Expiration_Date':['data_cc_expiration', '0220'],
        'CSC_code':['data_cc_cvv', '451'],
        'Email':['data_email','pupsen@vupsen.com'],
        'Zip':['data_holder_zip', '94087']
    }
    for key, value in form_data.items():
        fields = driver.find_elements_by_xpath('//input[@id="%s"]' %value[0])
        if fields:
            fields[0].send_keys(str(value[1]))
        else:
            raise ValueError(key+'field not found')

def click_button_by_id(id_name):
    buttons =driver.find_elements_by_xpath('//button[@id="%s"]' %id_name)
    if buttons:
        buttons[0].click()
    else:
        raise ValueError('Button not found')

def message_check(text_message):
    text = driver.find_elements_by_xpath('//h1[contains(text(), "%s")]' %text_message)
    if text and text[0].is_displayed():
        print 'Payment was Declined'
    else:
        print 'Test feild'

def sleep_sec(sec):
    sleep(sec)




open_url('https://www.hsselite.com/')

click_button_on_home_promo_by_class('btn_buy_elite')
sleep(10)
select_plan('select_btn_for_1866_plan_by_CCVindicia')
payment_form()
click_button_by_id('btn_pay')
message_check('Your Payment was Declined')
