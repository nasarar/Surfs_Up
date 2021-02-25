#importing dependencies
import datetime as dt
import numpy as np
import pandas as pd

#importing SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import Flash dependecies
from flask import Flask, jsonify

#allows access to SQLite Database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflects the databases into our classes
Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#creates a session link to the database
session = Session(engine)


#### SETUP FLASK ###
app = Flask(__name__)

#creates a base route
@app.route("/")

def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        '''
    )


#creates a precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    #dictionary is created to return a key-value pair for precipitation
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


#creates a stations route
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    
    #unravel results in one dimensional array then convert into a list
    stations = list(np.ravel(results))
    return jsonify(stations = stations) #stations = stations to format the list into JSON


#creates the monthly temperature route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    
    return jsonify(results = results)


#creates statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #IF NO END DATE GIVEN THEN THIS IF STATEMENT RUNS
    if not end:
        #asterisk means there's multiple results to the query
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)


    #this query gets the statistics data
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
