# Tianchi-Dataset-Download

A python script for downloading training datasets of "Global AI Challenge on Meteorology" in Tianchi.

### Usage:
1. Login to the website of Tianchi: https://account.aliyun.com/login/login.htm
2. Get your cookie with the development tool of your browser.
3. Edit Download.py, and paste your cookie to line 11:
```
u'cookie': u'PASTE YOUR COOKIE HERE'
```
4. Save the changes, and run the script in terminal:
```
nohup python -u Download.py >download.log 2>&1 &
```
