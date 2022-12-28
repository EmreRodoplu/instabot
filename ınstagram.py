from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import KB #user information


class Instagram:
    def __init__(self):
        self.link="https://www.instagram.com/"
        self.options = ChromeOptions()
        self.service = Service(executable_path="C:\\Users\\emrer\\Desktop\\chromedriver.exe")
        
        self.browser = webdriver.Chrome(service=self.service,options=self.options)
        
        self.flwrs =[]
        self.flw = []
        self.eski_takipciler = []
        
    
    def goInstagram(self):
        self.browser.get(self.link)
        sleep(2)
        self.browser.maximize_window()
        
    
    def login(self):
        username = self.browser.find_element(By.NAME,"username")
        password = self.browser.find_element(By.NAME,"password")
        
        username.send_keys(KB.username)
        password.send_keys(KB.password)

        btn = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]")
        btn.click()
        sleep(5)      
        self.browser.get(self.link+KB.username)
        sleep(5)
        
    def getfollowers(self):
        takipci_btn = self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        
        
        takipci_btn.click()
        sleep(4)
        
        
        
        Instagram.scrollDown(self)

        takipçiler = self.browser.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")

        for takipçi in takipçiler:
            self.flwrs.append(takipçi.get_attribute("href"))
        
        sleep(2)

            
    def follow(self):
        self.browser.back()        
        sleep(2)
        takip_btn = self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a/div")        
        takip_btn.click()
        sleep(4)
        
        

        Instagram.scrollDown(self)

        takip_edilen = self.browser.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")
        

        for takip in takip_edilen:
            self.flw.append(takip.get_attribute("href"))
        sleep(2)

        self.browser.quit()        
   
   
    def not_follow_me_back(self):
        sayac = 0
        for i in self.flw:
            if i not in self.flwrs:
                sayac += 1
                print(str(sayac)+"-->"+i+" Beni takip etmiyor")
    

    def scrollDown(self):
        jsKomut = """
        sayfa = document.querySelector("._aano");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfasonu = sayfa.scrollHeight;
        return sayfasonu;
        """
        sayfasonu = self.browser.execute_script(jsKomut)
        while True:
            son = sayfasonu
            sleep(1)
            sayfasonu = self.browser.execute_script(jsKomut)
            if son == sayfasonu:
                break
            
    
       
        



app=Instagram()
app.goInstagram()
app.login()
app.getfollowers()
app.follow()
app.not_follow_me_back()






    
