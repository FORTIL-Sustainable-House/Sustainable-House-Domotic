from app import create_app

# Creates the app from its __init__
app = create_app()
app.app_context().push()
