
import tornado.web  
import tornado.httpserver  
import tornado.ioloop  
import tornado.options  

from tornado.options import define, options
from app.configs import configs, mysql_configs  
from app.urls import urls 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

define("port", type=int, default=process.env.PORT, help="runing port")


class CustomApplication(tornado.web.Application):
    def __init__(self):
        settings = configs
        handlers = urls
        self.db = self.db_session
        super(CustomApplication, self).__init__(handlers=handlers, **settings)

    @property
    def db_session(self):
        engine = create_engine(
            'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(
                **mysql_configs
            ),
            encoding="utf-8",
            echo=True,
            pool_size=100,
            pool_recycle=10,
            connect_args={"charset": 'utf8'}
        )
        Session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False
        )
        return Session()


def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(
        CustomApplication(),
        xheaders=True
    )
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
