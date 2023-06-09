from app import create_app
from app.server.events import socketio
import sys

if __name__ == '__main__':
    app = create_app()
    if len(sys.argv) > 2:
        if sys.argv[1] == '--expose' or sys.argv[1] == '-E':
            socketio.run(app, debug=True, host='0.0.0.0', port=8080)
    else:
        socketio.run(app, debug=True, host='127.0.0.1', port=8080)