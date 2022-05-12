# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.models import ShortUrl


class ResultHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="Generate Results"
        )
        uuid_data = self.get_argument("uuid", None)
        if uuid_data:
            try:
                su = self.session.query(ShortUrl).filter_by(uuid=uuid_data).first()
                data["su"] = su
            except Exception as e:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
            self.render("result.html", data=data)
