from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.dummy_feature import bp
from app.dummy_feature.forms import RoomForm
from app.dummy_feature.models import Room

# Main page.
@bp.route('/dummy_page')
@login_required
def dummy_page():
    # Retrieve rooms.
    rooms = Room.query.all()

    # Render the page
    return render_template(
        'dummy_feature/dummy_page.html', 
        title='Dummy Title', 
        rooms=rooms
    )  

# Method to add a room.
@bp.route('/room/add', methods=['GET', 'POST'])
@login_required
def add_room():
    # If user is not authenticated, redirect to login page.
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    form = RoomForm()

    # If form is correctly filled, add in database.
    # Redirect to main page.
    if form.validate_on_submit():
        room = Room(
            name=form.name.data, 
            area=form.area.data
        )
        db.session.add(room)
        db.session.commit()
        flash('Congratulations, you added a new room!')
        return redirect(url_for('dummy_feature.dummy_page'))

    # Redirect to form to add room.
    return render_template('dummy_feature/add_room.html', title='Add room', form=form)
