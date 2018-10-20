from flask import Flask, g, request, jsonify
from database import get_db

app = Flask(__name__)


@app.route('/member', methods=['GET'])
def get_members():
    db = get_db()
    member_cur = db.execute('''
                SELECT
                    id, name, email, level 
                FROM
                    members
    ''')
    members = member_cur.fetchall()

    return_values = []

    for member in members:
        member_dict = {}
        member_dict['id'] = member['id']
        member_dict['name'] = member['name']
        member_dict['email'] = member['email']
        member_dict['level'] = member['level']
        return_values.append(member_dict)

    return jsonify({'members': return_values})


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    return 'The returns one member by ID.'


@app.route('/member', methods=['POST'])
def add_member():
    new_member_data = request.get_json()

    db = get_db()
    db.execute('INSERT INTO members (name, email, level) VALUES (?,?,?)',\
               [new_member_data['name'], new_member_data['email'], new_member_data['level']])
    db.commit()

    member_cur = db.execute('''
                SELECT
                    id, name, email, level
                FROM
                    members
                WHERE
                    name = ?
    ''', [new_member_data['name']])
    new_member = member_cur.fetchone()

    return jsonify({'id': new_member['id'],
                    'name': new_member['name'],
                    'email': new_member['email'],
                    'level': new_member['level']
                    })


@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return 'This updates a member by ID.'


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'This removes a member ID.'


if __name__ == '__main__':
    app.run(debug=True)
