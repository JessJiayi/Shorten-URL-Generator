
import datetime
import hashlib
import tornado.web


class CommonHandler(tornado.web.RequestHandler):
    @property
    def site_url(self):
        return "http://127.0.0.1:8000/"


    @property
    def dt(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def d(self, day=0):
        return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime("%Y-%m-%d")


    @property
    def session(self):
        return self.application.db

    @property
    def params(self):
        data = self.request.arguments
        data = {
            v[0]: list(
                map(
                    lambda val: str(val, encoding="utf-8"),
                    v[1]
                )
            )
            for v in data.items()
        }
        return data

    def get_md5(self, long_url):
        s = long_url.encode("utf-8")
        md5 = hashlib.md5()
        md5.update(s)
        return md5.hexdigest()

    def get_hash_key(self, long_url):
        code_map = []  # 0~9a~zA~Z
        for v in range(0, 10):
            code_map.append(str(v))
        for v in range(97, 123):
            code_map.append(chr(v))
        for v in range(65, 91):
            code_map.append(chr(v))
        code_map = tuple(code_map)
        md5 = self.get_md5(long_url)
        su = []
        for i in range(0, 4):
            n = int(md5[i * 8:(i + 1) * 8], 16)
            v = []
            e = 0
            for j in range(0, 5):
                x = 0x0000003D & n
                e |= ((0x00000002 & n) >> 1) << j
                v.insert(0, code_map[x])
                n = n >> 6
            e |= n << 5
            v.insert(0, code_map[e & 0x0000003D])
            su.append(''.join(v))
        return su

