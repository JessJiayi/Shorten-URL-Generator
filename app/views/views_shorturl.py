# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.models.models import ShortUrl, PageView
from app.tools.ip2Addr import ip2addr


class ShortUrlHandler(CommonHandler):
    def get(self, code):
        try:
            su = self.session.query(ShortUrl).filter_by(code=code).first()
            self.save_pv(su.id)
        except Exception as e:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
        self.redirect(su.url)

    def save_pv(self, shorturl_id):
        try:
            pv = PageView(
                ip=self.request.remote_ip,
                url=self.request.uri,
                shorturl_id=shorturl_id,
                method=self.request.method,
                address=ip2addr(self.request.remote_ip)["region"],
                createdAt=self.dt,
                updatedAt=self.dt
            )
            self.session.add(pv)
        except Exception as e:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
