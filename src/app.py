from flask import Flask
from routes.tasks_routes import task_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(task_bp)

    return app

app = create_app()

if (__name__ == "__main__"):
    try:
        app.run(debug=True, port=3333)
    except Exception as e:
        print(e)