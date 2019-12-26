from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def message_received(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('recvMsg')
def receive_message(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('sendMsg', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(app, debug=True)
