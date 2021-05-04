from aiohttp import web

async def handler(request):
    if request.body_exists:
        data_b = await request.read()
        data = str(data_b.decode('utf-8'))
        print(data)
    return web.json_response({"ok": 1})

app = web.Application()
app.add_routes([web.view('/', handler)])
web.run_app(app, host='193.162.143.184', port=499)