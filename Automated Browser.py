from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
user = driver.find_element_by_id('user_login')
time.sleep(3)
user.send_keys('agreezhao@gmail.com')
pas = driver.find_element_by_id('user_pass')
pas.send_keys('zzh960607')
sub = driver.find_element_by_id('wp-submit')
sub.click()
time.sleep(2)
article = driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
article.click()
comment = driver.find_element_by_name('comment')
comment.send_keys('selenium比cookie好用得多啊！')
post = driver.find_element_by_id('submit')
post.click()