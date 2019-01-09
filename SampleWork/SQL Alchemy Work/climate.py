###################################################################################################
# Step 4 - Climate App
#
#   Now that you have completed your initial analysis, design a Flask api 
#   based on the queries that you have just developed.
#
#      * Use FLASK to create your routes.
#
#   Routes
#
#       * `/api/v1.0/precipitation`
#           * Query for the dates and precipitation observations from the last year.
#           * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
#           * Return the json representation of your dictionary.
#       * `/api/v1.0/stations`
#           * Return a json list of stations from the dataset.
#       * `/api/v1.0/tobs`
#           * Return a json list of Temperature Observations (tobs) for the previous year
#       * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
#           * Return a json list of the minimum temperature, the average temperature, and
#               the max temperature for a given start or start-end range.
#           * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates 
#               greater than and equal to the start date.
#           * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` 
#               for dates between the start and end date inclusive.
###################################################################################################

#Import Dependencies

from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
import pandas as pd
import numpy as np

#Datebase creation

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#Setup Flask

app = Flask(__name__)

#Create flask routes


# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and tobs as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    final_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > last_year).order_by(Measurement.date).all()

    precip_total = []
    for result in precip:
        row = {}
        row["date"] = precip[0]
        row["prcp"] = precip[1]
        precip_total.append(row)

    return jsonify(precip_total)


# /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)

# /api/v1.0/tobs
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > prev_year).order_by(Measurement.date).all()

    tobs_total = []
    for result in tobs:
        row = {}
        row["date"] = tobs[0]
        row["tobs"] = tobs[1]
        tobs_total.append(row)

    return jsonify(tobs_total)

# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>")
def trip_one(start):

    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    year = dt.timedelta(days=365)
    start = start_date-year
    end = dt.date(2017, 8, 23)
    trip_info = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    trip = list(np.ravel(trip_info))
    return jsonify(trip)

@app.route("/api/v1.0/<start>/<end>")
def trip_two(start, end):

    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    year = dt.timedelta(days=365)
    start = start_date-year
    end = end_date-year
    trip_info = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    trip = list(np.ravel(trip_info))
    return jsonify(trip)

if __name__ == "__main__":
    app.run(debug=True)