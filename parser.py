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
        self.music_dict = {}

    def browser_go(self):
        self.browser.get(self.url)

    def browser_search(self, user_search):

        self.browser_go()

        search_field = self.browser.find_element(By.XPATH, "//input[@type='search']")
        search_field.send_keys(user_search)

        self.browser.find_element(By.XPATH, "//div/button[@type='submit']").click()  # search

        # button
    def page_walking(self):
        self.music_dict = {}

        try:
            pages = self.browser.find_elements(By.XPATH, Selectors.pages)
            pages = [page.get_attribute('href') for page in pages]
            for page in pages:
                self.browser.get(page)
                self.browser_get()

        finally:
            self.browser.quit()

    def browser_get(self):

        authors = self.browser.find_elements(By.XPATH, Selectors.author_name)
        author_names = [author.text for author in authors[:-10]]

        tracks = self.browser.find_elements(By.XPATH, Selectors.track_name)
        track_names = [track.text for track in tracks]

        completed_tracks = list(zip(author_names, track_names))

        completed_tracks = [i[0]+' - '+i[1] for i in completed_tracks]
        completed_tracks = completed_tracks[1::]

        raw_tracks_urls = self.browser.find_elements(By.XPATH, Selectors.track_url_xpath)
        tracks_urls = [track_url.get_dom_attribute(Selectors.track_attribute) for track_url in raw_tracks_urls]

        self.music_dict.update(dict(zip(completed_tracks, tracks_urls)))
