import asyncio
import time

from song import Song
from my_selectors import Selectors
from playwright.async_api import async_playwright, Playwright


class MusicParser:
    @classmethod
    async def init_browser(cls,playwright : Playwright, user_search : str ):
        #cls.playwright = playwright
        cls.user_search = user_search
        cls.url = 'https://muzofond.fm/'
        cls.browser = await playwright.firefox.launch(headless=True)
        cls.page = await cls.browser.new_page()
        cls.music_list = []
        await cls.browser_search()


    @classmethod
    async def browser_search(cls):
        #cls.music_list = []
        await cls.page.goto(cls.url)
        # finding search field and put what we want to find
        await cls.page.locator( Selectors.search_field).fill(cls.user_search)

        # click search button
        await cls.page.locator(Selectors.search_field_button).click()

        await cls.page_walking()
    @classmethod
    async def page_walking(cls):
        #the function just gets all frames by finding its links and go there to get tacks on the frames
        pages =  cls.page.locator( Selectors.pages)
        links = await cls.page.locator( Selectors.pages).count()
        links = [await pages.nth(i).get_attribute("href") for i in range(links)]


        for page in links:
            await cls.page.goto(page)
            await cls.get_tracks()


    @classmethod
    async def get_tracks(cls):

        authors = await cls.page.locator(Selectors.author_name).all_inner_texts()
        track_names = await cls.page.locator(Selectors.track_name).all_inner_texts()

        #await cls.page.wait_for_selector(Selectors.track_url_xpath)

        raw_tracks_urls = cls.page.locator(Selectors.track_url_xpath)


        links = await  cls.page.locator(Selectors.track_url_xpath).count()


        links = [await raw_tracks_urls.nth(i).get_attribute("data-url") for i in range(links)]


        completed_tracks = list(zip(authors[1:-10], track_names[1::],links))

        completed_tracks = [Song(*i) for i in completed_tracks]


        cls.music_list.extend(completed_tracks)

'''async def main():
    async with async_playwright() as playwright:
        await MusicParser.init_browser(playwright, 'wildways')

    print(MusicParser.music_list)
asyncio.run(main())'''