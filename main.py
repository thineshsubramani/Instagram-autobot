from selenium import webdriver
from time import sleep

class Instabot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username1 = username
        self.driver.get("https://instagram.com")
        sleep(2)
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        password = self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        btn = self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def get_unfollower(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username1)).click()
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        sleep(2)
        last_ht, ht = 0,1
        while last_ht !=ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name != '']
        print(names)

    def get_followers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username1)).click()
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        sleep(2)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                   arguments[0].scrollTo(0, arguments[0].scrollHeight);
                   return arguments[0].scrollHeight;
                   """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name != '']
        print(names)
        count =0
        for nam in names:
            count +=1
        print(count)

my_bot = Instabot("thineshsubramani","theri5085")
my_bot.get_followers()