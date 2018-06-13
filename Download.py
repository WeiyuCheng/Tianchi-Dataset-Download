# -*- coding: utf-8 -*-
import requests

def main():
    for i in range(60):
        try:
            url = 'https://tianchi.aliyun.com/datalab/download.do?filePath=file/opensearch/documents/110/SRAD2018_TRAIN_%03d.zip&id=110' % (i+1)
            Headers = {u'accept': u' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       u'accept-encoding': u' gzip, deflate, br',
                       u'accept-language': u' zh-CN,zh;q=0.9,en;q=0.8',
                       u'cookie': u" ",
                       u'referer': u'https://tianchi.aliyun.com/datalab/dataSet.html?spm=5176.11409106.555.12.747a1e8bU64VIe&dataId=110',
                       u'upgrade-insecure-requests': u' 1',
                       u'user-agent': u' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'}
            html = requests.get(url=url, headers=Headers, allow_redirects=False)
            print html.status_code
            r = requests.get(url=html.headers['Location'], headers=html.headers, stream=True)
            f = open("train_file_%03d.zip"%(i+1), "wb")
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
        except:
            continue


if __name__ == '__main__':
    main()