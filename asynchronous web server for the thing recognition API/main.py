from aiohttp import web

from recg import *
from handlers import *

app = web.Application()
app.add_routes(routes)
web.run_app(app)