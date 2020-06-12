from app import create_app, make_celery

# Creates the app from its __init__
app = create_app()
app.app_context().push()

celery = make_celery(app)
