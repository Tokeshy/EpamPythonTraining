## [Iteration 1] One-shot command-line RSS reader.
# RSS reader should be a command-line utility which receives [RSS](wikipedia.org/wiki/RSS) URL and prints results in human-readable format.

# You are free to choose format of the news console output. The textbox below provides an example of how it can be implemented:

# ```shell
# $ rss_reader.py "https://news.yahoo.com/rss/" --limit 1

# Feed: Yahoo News - Latest News & Headlines

# Title: Nestor heads into Georgia after tornados damage Florida
# Date: Sun, 20 Oct 2019 04:21:44 +0300
# Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

# [image 2: Nestor heads into Georgia after tornados damage Florida][2]Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
# homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
# off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
# march across a swath of the U.S. Southeast.

# Links:
# [1]: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html (link)
# [2]: http://l2.yimg.com/uu/api/res/1.2/Liyq2kH4HqlYHaS5BmZWpw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/ap.org/5ecc06358726cabef94585f99050f4f0 (image)

# ```
# Utility should provide the following interface:
# ```shell
# usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
#                      source

# Pure Python command-line RSS reader.

# positional arguments:
#   source         RSS URL

# optional arguments:
#   -h, --help     show this help message and exit
#   --version      Print version info
#   --json         Print result as JSON in stdout
#   --verbose      Outputs verbose status messages
#   --limit LIMIT  Limit news topics if this parameter provided
# ```

# In case of using `--json` argument your utility should convert the news into [JSON](https://en.wikipedia.org/wiki/JSON) format.
# You should come up with the JSON structure on you own and describe it in the README.md file for your repository or in a separate documentation file.


# With the argument `--verbose` your program should print all logs in stdout.

### Task clarification (I)

# 1) If `--version` option is specified app should _just print its version_ and stop.
# 2) User should be able to use `--version` option without specifying RSS URL. For example:
# ```
# > python rss_reader.py --version
# "Version 1.4"
# ```
# 3) The version is supposed to change with every iteration.
# 4) If `--limit` is not specified, then user should get _all_ available feed.
# 5) If `--limit` is larger than feed size then user should get _all_ available news.
# 6) `--verbose` should print logs _in the process_ of application running, _not after everything is done_.
# 7) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout_.
# 8) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout in JSON format_.
# 9) It is preferrable to have different custom exceptions for different situations(If needed).
# 10) The `--limit` argument should also affect JSON generation.

##############################################################################################################

from argparse import ArgumentParser  # console params
from requests import get  # linking

'''
RSS urls for tests & other:
   https://news.yahoo.com/rss/
   https://www.space.com/feeds/all
   https://www.wired.com/category/science/feed
   https://www.liga.net/tech/technology/rss.xml
   https://news.yandex.ru/society.rss
   https://www.trend.az/rss/trend_all_ru.rss

   https://www.digital-science.com/feed/ !!!!!

'''

## константы
CurrVer = 'Version 1.0'
NoSuchResource = 'The resource you trying to connect is not responding or does not exists'


def LineCleaner(line :str, PropertyID :int):
   '''
   clearing parameters depending on the type

   description for Dict id params

   general id:
   1 - RSS page feed
   2 - RSS page link
   3 - RSS page description (optional)
   4 - RSS language (optional)
   5 - RSS logo image link (optional)

   news id:
   11 - title of the news
   12 - link of the news
   13 - publication date of the news
   14 - source url, used if news page locate on remote (not RSS) server - optional parameter 
   15 - news category - opttional parameter
   16 - description  - opttional parameter of news category
   17 - media:content - opt (+- = image) # link 2 image
   '''

   PropDict = {1 : '<title>', 2 : '<link>', 3 : '<description>', 4: '<language>', 5 : '<url>',
               11 : '<title>', 12 : '<link>', 13 : '<pubDate>', 14 : '<source', 15 : '<category>',
               16 : '<description>',}
   NoSuchInfo = 'information not presented by this portal'
   
   if PropertyID != 17:
      try:
         value = line[(line.index(PropDict[PropertyID]) + len(PropDict[PropertyID])) : (line.index(PropDict[PropertyID].replace('<', '</')))]
         if len(value) <= 1:
            value = NoSuchInfo
      except:
         value = NoSuchInfo
      finally:
         return value
   else:
      pass # обработка картинок
    

def BlockParser(Page:str, limit:int = -1):
   '''
   receiving the page as str and news limit as int, after which we form the heading part and the news list
   '''
   DividedPage = Page.split('<item>')
   if limit == -1:
      limit = Page.count('<item>') 
   
   NewsStorage = {}
   NewsStorage['RSSFeed'] = 'Feed: ' + LineCleaner(DividedPage[0], 1).replace('&amp; ', '& ')
   NewsStorage['RssLink'] = 'RSS news portal link: ' + LineCleaner(DividedPage[0], 2)
   NewsStorage['RssDescription'] = 'RSS portal self description: ' + LineCleaner(DividedPage[0], 3)
   NewsStorage['RssLang'] = 'RSS current language: ' + LineCleaner(DividedPage[0], 4)
   NewsStorage['RssLogoUrl'] = 'RSS logo picture: ' + LineCleaner(DividedPage[0], 5)   

   for id in range(1, limit+1):
      NewsStorage['title_' + str(id)] = LineCleaner(DividedPage[id], 11)
      NewsStorage['link_' + str(id)] = LineCleaner(DividedPage[id], 12)
      NewsStorage['pubDate_' + str(id)] = LineCleaner(DividedPage[id], 13)
      NewsStorage['source_' + str(id)] = LineCleaner(DividedPage[id], 14)
      NewsStorage['category_' + str(id)] =LineCleaner(DividedPage[id], 15)
      NewsStorage['description_' + str(id)] =LineCleaner (DividedPage[id], 16)
      NewsStorage['media_' + str(id)] = LineCleaner(DividedPage[id], 17)
   
   return NewsStorage


inp_loader = ArgumentParser(description='Pure Python command-line RSS reader.')
inp_loader.add_argument('source', nargs='?', type = str, help = 'RSS URL')
inp_loader.add_argument('--version', action="store_true", help = 'Print version info')
inp_loader.add_argument('--json', action="store_true", help = 'Print result as JSON in stdout')
inp_loader.add_argument('--verbose', action="store_true", help = 'Outputs verbose status messages')
#inp_loader.add_argument('-lim', '--limit', action="store_true", help = 'Limit news topics if this parameter provided')
inp_loader.add_argument('--limit', nargs='?', type = int, help = 'Limit news topics if this parameter provided')
args = inp_loader.parse_args()


if args.version:
    print(CurrVer)
else:
    arguments = inp_loader.parse_args()
    url = arguments.source
    try:
        if get(url).status_code != 200:
            print(NoSuchResource)
        else:
            RssPage = get(url).text
            Output = BlockParser(RssPage, arguments.limit)  
    except:
        pass
        #print(NoSuchResource)

  

