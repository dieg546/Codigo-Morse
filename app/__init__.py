from flask import Flask 

def create_app():

    app=Flask(__name__)

    from . import task

    app.register_blueprint(task.Blue)

    @app.route('/task')
    def init():
        return 'You can.'

    return app