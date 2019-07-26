class URL(object):
    def __init__(self, url, resource, name=None):
        self.url = url
        self.resource = resource
        self.name = name


def add_prefix(url_obj, prefix):
    url_obj.url = prefix + url_obj.url
    return url_obj


URL_LIST_V1 = (
    URL('/', 'resources.home.Home', name='home_page'),
    URL('/login', 'resources.login.Login', name='login_page'),
    URL('/login/callback', 'resources.callback.LoginCallback', name='login_callback_page')
)

URL_LIST = [add_prefix(url_obj, 'api/v1') for url_obj in URL_LIST_V1]