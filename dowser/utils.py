import cherrypy
from dowser import Root


def launch_memory_usage_server(port=8080, show_trace=False):
    config = {
        'server.socket_host': '0.0.0.0',
        'environment': 'embedded',
        'server.socket_port': port,
    }
    if show_trace:
        config.update({
            'global': {
                'request.show_tracebacks': True
            }}
        )
    cherrypy.tree.mount(Root())
    cherrypy.config.update(config)
    cherrypy.engine.start()
