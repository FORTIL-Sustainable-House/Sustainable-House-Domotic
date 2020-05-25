from flask import render_template
from flask_login import login_required

from app.management import bp

# Main page.
@bp.route('/dashboard')
@login_required
def dashboard():
    # Render the page
    return render_template(
        'management/dashboard.html', 
        title='Dashboard',
    )