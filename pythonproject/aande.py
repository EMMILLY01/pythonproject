import sys
import spotipy
import spotipy.util as util

from flask import Flask, render_template, request


app = Flask (__name__)

scope = 'user-library-read'


@app.route('/')
def hello():
    
    token = util.prompt_for_user_token(
        'emily.mould@icloud.com',
        scope,
        client_id='547d61dc2645426da6052d29f45c0595',
        client_secret='361e856ab8b2490bb3c22430eddb3eec',
        redirect_uri='http://127.0.0.1:5000/'
    )

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)

app.run(debug=True)