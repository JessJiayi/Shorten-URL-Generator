import uuid
from wtforms import Form  
from wtforms.fields import StringField  
from wtforms.validators import DataRequired, URL  
from app.views.views_common import CommonHandler
from werkzeug.datastructures import MultiDict
from app.models.models import ShortUrl


class ShortUrlForm(Form):
    url = StringField(
        "link",
        validators=[
            DataRequired(u"please enter link"),
            URL(message="invalid link")
        ]
    )


class IndexHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="Shorten URL Generator"
        )
        self.render("index.html", data=data)

    def post(self, *args, **kwargs):
        res = dict(code=0)
        form = ShortUrlForm(MultiDict(self.params))
        if form.validate():
            try:
                res["code"] = 1
                short_url_by_url = self.session.query(ShortUrl).filter_by(
                    url=form.data["url"]
                ).first()
                if not short_url_by_url:
                    uuid_data = uuid.uuid4().hex
                    shorturl = ShortUrl(
                        url=form.data["url"],
                        code=self.get_hash_key(form.data["url"])[0],
                        uuid=uuid_data,
                        createdAt=self.dt,
                        updatedAt=self.dt
                    )
                    self.session.add(shorturl)
                else:
                    uuid_data = short_url_by_url.uuid
                res["uuid"] = uuid_data
            except Exception as e:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)
