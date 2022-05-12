
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
    db_host="ec2-54-172-175-251.compute-1.amazonaws.com",
    db_name="d8nt0t0evtddcp",
    db_port=5432,
    db_user="ocklswkhlicvau",
    db_pwd="0ef0864eb874ca4af692ff36d91ed54c5ca6bf25f7d5e10f84e3cda62b59a3c8"
)
