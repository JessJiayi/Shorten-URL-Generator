
import os  


root = os.path.dirname(__file__)



configs = dict(
    static_path=os.path.join(root, "static"),
    template_path=os.path.join(root, "templates"),
    debug=True,
    xsrf_cookies=True,
    cookie_secret='03df65effda044bca54b8b59b5d2d03e'
)


mysql_configs = dict(
    db_host="127.0.0.1",
    db_name="short_url",
    db_port=3306,
    db_user="root",
    db_pwd="root"
)
