from app.dummy_feature import bp
from flask import render_template
from flask_login import login_required


# Dummy example page
@bp.route('/dummy_page')
@login_required
def dummy_page():
    # Do stuff maybe...

    # Render the page
    return render_template('dummy_feature/dummy_page.html', title='Dummy Title')
