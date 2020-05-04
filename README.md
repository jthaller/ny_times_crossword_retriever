
*Edit*: Project postponed indefinitely. Something must be wrong with my selenium installation.
``` 
driver.get(website_url)
```
seems to work fine. Yet calling:
```
print(driver.current_url)
```
does nothing. I suspect a new installation of selenium and chrome would be necessary to get things working. It's not important enough for me to install a new browser, just for this, so I am postponing this project.

# ny_times_crossword_retriever
Download and print the Times' daily crossword with a single click.

## Dependencies
Selenium must be installed as a driver for your browser:
* [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
