import os
from urllib import request
from tqdm import tqdm


def saveurlcontent(url, savepath, callback=None, overwrite=False, buffersize=8192, useragent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"):
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


def saveurlcontentprogress(url, savepath, overwrite=False, buffersize=8192, useragent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"):
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
