from aiohttp import web
import os
from handlers import *

import templates  as temp

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text=temp.MainPage, content_type='text/html')

@routes.get('/SendFile')
async def HandlerPhoto(request):

    IsJson = await request.rel_url.query['IsJson']

    reader = await request.multipart()

    field = await reader.next()
    assert field.name == 'name'
    name = await field.read(decode=True)

    field = await reader.next()
    assert field.name == 'mp3'
    filename = field.filename
    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    with open(os.path.join(os.getcwd(), "/photo", filename), 'wb') as f:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)

    
    a = await detect_objects(os.path.join(os.getcwd(), "/photo", filename)

    if IsJson:
        return web.json_response([a[0]])

    else:
        return web.Response(text=temp.ResponseHTML(a), content_type='text/html')


