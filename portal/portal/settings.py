# -*- coding: utf-8 -*-

# Scrapy settings for portal project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'portal'

SPIDER_MODULES = ['portal.spiders']
NEWSPIDER_MODULE = 'portal.spiders'


PROXIES = [
  "218.60.8.99:3129",
  "212.64.51.13:8888",
  "112.247.181.208:8060",
  "118.26.170.209:8080",
  "125.62.27.53:3128",
  "183.146.213.198:80",
  "117.127.16.207:8080",
  "123.161.23.50:9797",
  "120.234.63.196:3128",
  "119.28.203.242:8000",
  "171.80.112.60:9999",
  "60.235.28.165:8088",
  "47.52.231.140:8080",
  "125.46.0.62:53281",
  "175.18.152.45:8080",
  "175.18.52.11:8080",
  "221.2.174.3:8060",
  "14.20.235.230:9797",
  "82.114.241.138:8080",
  "61.135.155.82:443",
  "111.59.90.238:80",
  "122.137.177.232:8080",
  "27.191.234.69:9999",
  "122.141.74.186:8080",
  "39.137.69.6:8080",
  "117.191.11.108:80",
  "144.255.48.144:9999",
  "211.101.154.105:43598",
  "175.18.18.88:8080",
  "119.48.180.254:9999",
  "60.5.254.169:8081",
  "121.69.46.177:9000",
  "122.136.212.132:53281",
  "101.231.234.38:8080",
  "218.108.175.15:80",
  "61.128.208.94:3128",
  "180.107.179.44:8118",
  "27.46.21.179:8888",
  "202.162.34.115:53281",
  "119.23.238.202:3128",
  "58.249.55.222:9797",
  "58.247.127.145:53281"
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'portal (+http://www.yourdomain.com)'
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'portal.middlewares.PortalSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'portal.middlewares.PortalDownloaderMiddleware': 543,
   'portal.middlewares.RandomUserAgent': 543,
   'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware': None
   # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'portal.pipelines.PortalPipeline': 300,
   'portal.pipelines.ElasticsearchPipeline': 298
}


import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'portal'))

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
