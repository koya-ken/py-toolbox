# examples

## change working directory

```python
from py-toolbox import *

with dir('path_to_working_dir') :
    process on working dir
```

## copy file with progress

```python
from py-toolbox import *
copyfileprogress(fromfile, tofile)
```

## download file with progress

```python
from py_toolbox import *

saveurlcontentprogress(url, '.')
# without progress
# saveurlcontent(url, '.')
```
