from flask import Flask, session, request, redirect, url_for
from flask import render_template

app = Flask(__name__)

# Encrypt the session cookie with a secret key
# This is a simple key for demonstration purposes
app.secret_key = b'sAlty _Key_ for saLtY c00k!es'


# This endpoint should be called by the Rocketchat app when clicking Join
# It will have the jwt token in the query string
@app.route('/start/<tenant>/<meeting_id>', methods=['GET'])
def start_meeting(tenant, meeting_id):
    # we store the tenant, meeting_id and jwt in the session
    session['tenant'] = tenant
    session['meeting_id'] = meeting_id
    session['jwt'] = request.args.get('jwt')
    # and we redirect to the meeting page
    return redirect(url_for('meet', meeting_id=session['meeting_id']))


@app.route('/meet/<meeting_id>')
def meet(meeting_id):
    # here we render a Jitsi Meet iframe with the meeting_id and jwt token
    return render_template('meeting.html',
                           meeting_id=meeting_id,
                           jwt=session['jwt'],
                           tenant=session['tenant']
                           )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
