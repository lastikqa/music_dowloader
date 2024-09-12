import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from my_selectors import Selectors


class MusicParser:
    def __init__(self):
        self.url = 'https://muzofond.fm/'
        self.options_firefox = webdriver.FirefoxOptions()
        self.options_firefox.add_argument('--headless')
        self.options_firefox.add_argument("--disable-automation")
        self.browser = webdriver.Firefox(options=self.options_firefox)

    def browser_go(self):
        self.browser.get(self.url)
        
    def browser_search(self, user_search):
        self.browser_go()

        search_field = self.browser.find_element(By.XPATH, "//input[@type='search']")
        search_field.send_keys(user_search)

        search_button = self.browser.find_element(By.XPATH, "//div/button[@type='submit']").click()

    def browser_get(self):
        try:
            authors = self.browser.find_elements(By.XPATH, Selectors.author_name)
            author_names = [author.text for author in authors]

            tracks = self.browser.find_elements(By.XPATH, Selectors.track_name)
            track_names = [track.text for track in tracks]

            completed_tracks = list(zip(author_names,track_names))
            completed_tracks = [i[0]+' - '+i[1] for i in completed_tracks]

            raw_tracks_urls = self.browser.find_elements(By.XPATH, Selectors.track_url_xpath)
            tracks_urls = [track_url.get_dom_attribute(Selectors.track_attribute) for track_url in raw_tracks_urls]

            music_dict = dict(zip(completed_tracks,tracks_urls))
        finally:
            self.browser.quit()
        return music_dict



