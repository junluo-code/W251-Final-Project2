from flask import Flask, render_template, jsonify
from cassandra.cluster import Cluster
#from flask_cassandra import CassandraCluster


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/explorer')
def explorer():
    return render_template("explorer.html")

@app.route('/flot')
def flot():
    return render_template("flot-charts.html")


@app.route('/rsvp')
def rsvp():
    return app.send_static_file("rsvps.json")

@app.route('/top10topics')
def top10topics():
    return app.send_static_file("top10topics.json")


@app.route('/api/venue',  methods=['GET'])
def get_venues():
    cluster = Cluster("dse-01.meetlytix.com")
    session = cluster.connect("meetlytix")
    venues = session.execute('SELECT * from ankit_v2')
    results = []
    for venue in venues:
        #result = '{' + '"venue_id":' + venue.venue_id + ', "lat":' + venue.lat  + ', "lon":' + venue.lon + ', "venue_name": "' + venue.venue_name + '"}'
        result = '{' + '"venue_name":' + venue.venue_name + '"}'

        results.append(result)
        #print venue.venue_id, venue.lat, venue.lon, venue.venue_name
    return jsonify({'results':results})
    #return jsonify({'results':venues})


if __name__ == '__main__':
    app.run()
    #app.run(host='198.11.195.219', port=80)
