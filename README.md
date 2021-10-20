# sds - Scrap Download Split
Extracts latest #videos from given YouTube channel link, then downloads and splits them into parts.

# Notes:
* Runs using commandline and takes 3 arguments: channel link, number of videos and duration of each part.

it should look like this for example:

    python main.py https://www.youtube.com/c/mkbhd 3 120

* By default it uses Microsoft Edge but an optional argument can be added `firefox` or `edge`.
To add other browsers you need to download its driver and create an instance of that browser
with the path of the driver that you downloaded in **getUrls.py**.
```python
driver = webdriver.Chrome('./chromedriver')
```

# Known Issues:
* Only supports downloading .mp4 video format.
* Can't handle titles that include  wildcard characters.
* Download speeds can be slow sometimes.
