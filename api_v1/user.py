from flask import jsonify
from flask import request
from models import Fcuser, db
from .import api


@api.route('/users', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        if not (userid and username and password and re_password):
            return jsonify({'error' : 'No arguments'}), 400

        if password != re_password:
            return jsonify({'error' : 'Wrong password'}), 400
        
        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password

        db.session.add(fcuser)
        db.session.commit()

        return jsonify(), 201

    users = Fcuser.query.all()

    return jsonify([user.serialize for user in users])