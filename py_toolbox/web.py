import os
from urllib import request
from tqdm import tqdm

CHROME_USERAGENT = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

def gethtml(url,useragent=CHROME_USERAGENT,encoding="utf-8"):
    headers = {"User-Agent": useragent }
    req = request.Request(url, None, headers)
    data = request.urlopen(req)
    return data.read().decode(encoding)

def saveurlcontent(url, savepath, callback=None, overwrite=False, buffersize=8192, useragent=CHROME_USERAGENT):
    if os.path.isdir(savepath):
        savepath = os.path.join(savepath, os.path.basename(url))

    if not overwrite and os.path.exists(savepath):
        return

    headers = {"User-Agent":  useragent}
    req = request.Request(url, None, headers)
    return savereqcontent(req, savepath, callback, overwrite, buffersize)


def savereqcontent(req, savepath, callback=None, overwrite=False, buffersize=8192):
    if not overwrite and os.path.exists(savepath):
        return

    conetnt = request.urlopen(req)
    with open(savepath, mode="wb") as fdst:
        while True:
            buf = conetnt.read(buffersize)
            if not buf:
                break
            fdst.write(buf)
            copied = len(buf)
            if callback is not None:
                callback(copied)


def saveurlcontentprogress(url, savepath, overwrite=False, buffersize=8192, useragent=CHROME_USERAGENT):
    if os.path.isdir(savepath):
        savepath = os.path.join(savepath, os.path.basename(url))

    if not overwrite and os.path.exists(savepath):
        return

    headers = {"User-Agent":  useragent}
    req = request.Request(url, None, headers)
    conetnt = request.urlopen(req)
    size = int(conetnt.getheader('Content-Length'))
    progress = tqdm(total=size)
    return savereqcontent(req, savepath, lambda x: progress.update(x), overwrite, buffersize)
