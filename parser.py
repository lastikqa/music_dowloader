import asyncio
from song import Song
from my_selectors import Selectors
from playwright.async_api import async_playwright, Playwright


class MusicParser:
    @classmethod
    async def init_browser(cls,playwright : Playwright, user_search):
        cls.url = 'https://muzofond.fm/'
        cls.browser = await playwright.chromium.launch()
        cls.page = await cls.browser.new_page()
        cls.user_search = user_search
        cls.music_list = []
        await cls.browser_search()


    @classmethod
    async def browser_search(cls):
        cls.music_list = []
        await cls.page.goto(cls.url)
        # finding search field and put what we wanna find
        await cls.page.locator( "//input[@type='search']").fill(cls.user_search)

        # click search button
        await cls.page.locator("//div/button[@type='submit']").click()
        await cls.page_walking()
    @classmethod
    async def page_walking(cls):
        #the function just gets all frames by finding links and go there to get tacks on the frames
        try:
            pages =  cls.page.locator( Selectors.pages)
            links = await cls.page.locator( Selectors.pages).count()
            links = [await pages.nth(i).get_attribute("href") for i in range(links)]

            for page in links:
                await cls.page.goto(page)
                await cls.get_tracks()

        finally:
            pass
    @classmethod
    async def get_tracks(cls):

        authors = await cls.page.locator(Selectors.author_name).all_inner_texts()
        track_names = await cls.page.locator(Selectors.track_name).all_inner_texts()

        completed_tracks = list(zip(authors[:-10], track_names))

        completed_tracks = completed_tracks[1::]

        raw_tracks_urls = cls.page.locator(Selectors.track_url_xpath)

        links = await  cls.page.locator(Selectors.track_url_xpath).count()

        links = [await raw_tracks_urls.nth(i).get_attribute("data-url") for i in range(links)]

        completed_tracks = list(zip(completed_tracks, links))
        completed_tracks =  [Song(*i) for i in completed_tracks ]

        cls.music_list.extend(completed_tracks)

async def main():
    async with async_playwright() as playwright:
        await MusicParser.init_browser(playwright, 'skillet')

asyncio.run(main())