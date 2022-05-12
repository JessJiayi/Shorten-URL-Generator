
from app.views.views_index import IndexHandler as index
from app.views.views_result import ResultHandler as result
from app.views.views_shorturl import ShortUrlHandler as shorturl
from app.views.views_pageview import PageViewHandler as pageview
from app.views.views_error import ErrorHandler as error


urls = [
    (r"/", index),
    (r"/result", result),
    (r"/pageview", pageview),
    (r"/([a-zA-Z0-9]{6})", shorturl),
    (r"/.*", error)
]
