from flask import render_template, redirect, url_for, session
from flask_wtf import Form
from wtforms.fields import SubmitField, StringField
from testdb import Flask, db, app, Users

class usersubmit(Form):
    username = StringField('What is your name?')
    firstname = StringField('What is your  first name?')
    firstname = StringField('What is your  last name?')
    submit = SubmitField('Submit')


@app.route('/')
def index():
    session['known'] = False
    return render_template('index.html')

'''
@app.route('/users', methods=['GET'])
def users():
    form = usersubmit()
    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()
        if user is None:
            user = Users(name=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('learn.html',
        form=form, name=session.get('name'),
        known=session.get('known', False))
'''

if __name__ == '__main__':
   # app.run(debug=True)
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)

