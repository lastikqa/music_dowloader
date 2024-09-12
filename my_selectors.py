
class Selectors:
    """if artists in current url use the selectors"""
    author_name = "//h3/span[@class='artist']"
    track_name = "//h3/span[@class='track']"
    track_url_xpath = "//div[@class='actions']/ul/li[@class='play']"
    track_attribute = 'data-url'

