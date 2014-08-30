import json
from flask import Flask, request

app = Flask(__name__)


class APIBase(object):
    routes = {}

    @classmethod
    def register(cls, path):
        def deco(fn):
            cls.routes[path] = fn
            def _(*args, **kwargs):
                return json.dumps(fn(path, *args, **kwargs))
            return _
        return deco

    def dispatch(self, resource):
        if '/' in resource:
            resource, path = resource.split("/", 1)
        else:
            path = "/"
        return json.dumps(self.routes[path](resource))


class Source(APIBase):
    @APIBase.register("/")
    def default(name):
        return {
            "source": "fluxbox",
            "binaries": [],
        }

    @APIBase.register("list")
    def default(name):
        return {
            "source": "fluxbox",
            "suites": {
                "unstable": {
                    "1.3.5-2": [
                        "source",
                        "amd64", "armel", "armhf", "hurd-i386", "i386",
                        "kfreebsd-amd64", "kfreebsd-i386", "mips", "mipsel",
                        "powerpc", "ppc64el", "s390x", "sparc"
                    ]
                },
                "testing": {
                    "1.3.5-2": [
                        "source",
                        "amd64", "armel", "armhf", "hurd-i386", "i386",
                        "kfreebsd-amd64", "kfreebsd-i386", "mips", "mipsel",
                        "powerpc", "ppc64el", "s390x", "sparc"
                    ]
                }
            }
        }


resources = {
    "source": Source()
}


@app.route("/<path:path>/")
def dispatch(path):
    resource, path = path.split("/", 1)
    return resources[resource].dispatch(path)
