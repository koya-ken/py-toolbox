# how to install

```shell
pip install git+https://github.com/koya-ken/py-toolbox.git
```

# examples

## change working directory

```python
from py_toolbox import *

with dir('path_to_working_dir') :
    process on working dir

pushd('path_to_working_dir')
popd()
```

## copy file with progress

```python
from py_toolbox import *
copyfileprogress(fromfile, tofile)
```

## download file with progress

```python
from py_toolbox import *

saveurlcontentprogress(url, '.')
# without progress
# saveurlcontent(url, '.')
```

## excec command for windows

```python
from py_toolbox import *

# like bat script
cmd(command)
```
