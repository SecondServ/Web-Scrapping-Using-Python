from selenium import webdriver
import time

# Set browser to be Chrome
driver = webdriver.Chrome()
# Access targeted url
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
# Wait 3 second for browser to open the page
time.sleep(3)
# Locate the place for inputing username
user = driver.find_element_by_id('user_login')
# Input username
user.send_keys('xxxxx@gmail.com')
# Locate the place for inputing password
pas = driver.find_element_by_id('user_pass')
# Input username
pas.send_keys('xxxxxxxx')
# Loacte 'submit' button 
sub = driver.find_element_by_id('wp-submit')
# Click 'submit' button
sub.click()
# Wait 2 second for browser to jump
time.sleep(2)
# Locate the link I want to click
article = driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
# Click
article.click()
# Locate the place for inputing comment
comment = driver.find_element_by_name('comment')
# Input comment
comment.send_keys('selenium比cookie好用得多啊！')
# Locate and click 'submit' button
post = driver.find_element_by_id('submit')
post.click()
