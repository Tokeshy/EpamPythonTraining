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
## [Iteration 2] Distribution.

# * Utility should be wrapped into distribution package with `setuptools`.
# * This package should export CLI utility named `rss-reader`.


### Task clarification (II)
 
# 1) User should be able to run your application _both_ with and without installation of CLI utility,
# meaning that this should work:

# ```
# > python rss_reader.py ...
# ```

# as well as this:  

# ```
# > rss_reader ...
# ```
# 2) Make sure your second iteration works on a clean machie with python 3.9. (!)
# 3) Keep in mind that installed CLI utility should have the same functionality, so do not forget to update dependencies and packages.

##############################################################################################################
## [Iteration 3] News caching.
# The RSS news should be stored in a local storage while reading. The way and format of this storage you can choose yourself.
# Please describe it in a separate section of README.md or in the documentation.

# New optional argument `--date` must be added to your utility. It should take a date in `%Y%m%d` format.
# For example: `--date 20191020`
# Here date means actual *publishing date* not the date when you fetched the news.

# The cashed news can be read with it. The new from the specified day will be printed out.
# If the news are not found return an error.

# If the `--date` argument is not provided, the utility should work like in the previous iterations.

### Task clarification (III)
# 1) Try to make your application crossplatform, meaning that it should work on both Linux and Windows.
# For example when working with filesystem, try to use `os.path` lib instead of manually concatenating file paths.
# 2) `--date` should **not** require internet connection to fetch news from local cache.
# 3) User should be able to use `--date` without specifying RSS source. For example:
# ```
# > python rss_reader.py --date 20191206
# ......
# ```
# Or for second iteration (when installed using setuptools):
# ```
# > rss_reader --date 20191206
# ......
# ```
# 4) If `--date` specified _together with RSS source_, then app should get news _for this date_ from local cache that _were fetched from specified source_.
# 5) `--date` should work correctly with both `--json`, `--limit`, `--verbose` and their different combinations.

##############################################################################################################

from requests import get  # linking with web
import CustomFuncs  # custom functions container - so creepy place

'''
RSS urls for tests:
   https://news.yahoo.com/rss
   https://www.space.com/feeds/all
   https://www.wired.com/category/science/feed
   https://www.liga.net/tech/technology/rss.xml
   https://news.yandex.ru/society.rss
   https://www.trend.az/rss/trend_all_ru.rss
'''


def RunIt():
   current_version = 'Version 3.0'  # format "X.Y" were X is equal to current task iteration and Y reserved for something else)) - f.e. - commit num
   so_can_i_run = CustomFuncs.CanIRun()  # loading running permissions and initial args
   args = so_can_i_run[3]
   terminate = so_can_i_run[0]

   if not terminate:
      if args.version or args.date:  # cutting logic if it's not needed
         if args.version:
            print(current_version)  # so if we need only look at version just show this info & done
         elif args.date:
            CustomFuncs.VerbosePrint("... '--date' param was selected \nWell let's see what we got in cache")
            if args.source:
               CustomFuncs.LoadFromCache(args.date, args.source, args.json, args.limit)
            else:
               CustomFuncs.LoadFromCache(args.date, 'no_url', args.json, args.limit)


      elif not (args.version and args.date):  # if "version" is not enough keep mooving
         CustomFuncs.VerbosePrint('Loading constants...')
         no_such_resource = 'The resource you trying to connect is not responding or does not exists.'
         CustomFuncs.VerbosePrint('...Done')
         url = args.source  
         CustomFuncs.VerbosePrint(f'Connecting attempt to {url}...')

         if get(url).status_code != 200:
            CustomFuncs.VerbosePrint('...Connection attempt failed')
            print(no_such_resource)
         else:
            CustomFuncs.VerbosePrint('...Connection attempt succeed')
            CustomFuncs.InitialStorage()
            RssPage = get(url).text
            CustomFuncs.VerbosePrint("OK, let's parse it...")

            if not args.limit:
               Output = CustomFuncs.BlockParser(RssPage, args.source)
            else:
               Output = CustomFuncs.BlockParser(RssPage, args.source, args.limit)
            
            CustomFuncs.VerbosePrint('...Done')

         CustomFuncs.VerbosePrint('We start the printer, everything will be fine...')
         CustomFuncs.Printer(Output, args.json)

   elif terminate == True:  # seems like we don't have to do anything else..at this time
      print('Parameters reading failed... \nSee "--help" for input format')

if __name__ == '__main__':
   RunIt()