from aiohttp import web
import json
import check_port

async def handler(request):
    if request.body_exists:
        data_b = await request.read()
        data = json.loads(str(data_b.decode('utf-8')))
        ip = data['ip']
        port = data['port']
        internal_port = check_port.create_new_rule(ip,port)
        return web.json_response({"internal_port": internal_port})

app = web.Application()
app.add_routes([web.view('/', handler)])
web.run_app(app, host='185.252.144.176', port=499)