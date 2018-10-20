from flask import Flask, g
from database import get_db

app = Flask(__name__)


@app.route('/member', methods=['GET'])
def get_members():
    return 'This returns all the members.'


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    return 'The returns one member by ID.'


@app.route('/member', methods=['POST'])
def add_member():
    return 'This adds a new member.'


@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return 'This updates a member by ID.'


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'This removes a member ID.'


if __name__ == '__main__':
    app.run(debug=True)
