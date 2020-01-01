import os
from tqdm import tqdm


def copyfileobj(fromfile, tofile, callback, length=16*1024, overwrite=False):
    copied = 0

    if os.path.isdir(tofile):
        tofile = os.path.join(tofile, os.path.basename(fromfile))
    size = os.path.getsize(fromfile)
    tosize = os.path.getsize(tofile) if os.path.exists(tofile) else 0

    if os.path.exists(tofile) and not overwrite:
        return

    if not overwrite and size == tosize:
        return

    with open(fromfile, 'rb') as fsrc, open(tofile, 'wb') as fdst:
        while True:
            buf = fsrc.read(length)
            if not buf:
                break
            fdst.write(buf)
            copied = len(buf)
            callback(copied)


def copyfileprogress(fromfile, tofile, length=16*1024, overwrite=False, showmessage=True):
    if os.path.isdir(tofile):
        tofile = os.path.join(tofile, os.path.basename(fromfile))
    size = os.path.getsize(fromfile)
    tosize = os.path.getsize(tofile) if os.path.exists(tofile) else 0

    if os.path.exists(tofile) and not overwrite:
        return

    if not overwrite and size == tosize:
        return

    if showmessage:
        fromname = os.path.basename(fromfile)
        toname = os.path.basename(tofile)
        print(fromname, '=>', toname)

    progress = tqdm(total=size)
    copyfileobj(fromfile, tofile, lambda x: progress.update(x), length)
