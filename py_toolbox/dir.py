import os


class dir(object):
    def __init__(self, path):
        """create change working dir object

        Arguments:
            path {string} -- relative or full path
        """
        self.__prev_path = os.getcwd()
        mkdir(path)
        os.chdir(path)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.__prev_path)
        return False


def mkdir(path):
    """mkdir all subdirectory

    Arguments:
        path {string} -- relative or full path
    """
    if not os.path.exists(path):
        os.makedirs(path)
