import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func, desc
from matplotlib.ticker import NullFormatter
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import seaborn as sns
from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)



@app.route("/api/v1.0/precipitation")
def precipitation():
    '''Return list of dates and temps'''
    # Query results
    prcp_date_list = list(session.query(Measurement.date).all())[:365]

    prcp_list = list(session.query(Measurement.prcp).all())[:365]

    # Create a dictionary
    all_prcps = {"date" : prcp_date_list, "prcp" : prcp_list}
  
    return jsonify(all_prcps)



@app.route("/api/v1.0/stations")
def stations():
    '''Returns  list of stations'''
    # Query results
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():
    """Returns list of Temperature Observations (tobs) for the previous year."""
    # Query results
    results = session.query(Measurement.date, Measurement.tobs).\
           filter(Measurement.date >= '2016-01-01').
           filter(Measurement.date <= '2017-01-01').all()

    # Create a dictionary
    tobs_date_list = []
    tobs_list = []
    
    for tob in range(len(results)):
        (tobs_date, tobs) = results[tob]
        tobs_date_list.append(tobs_date)
        tobs_list.append(tobs)

    tobs_dict = {"date" : tobs_date_list, "tobs" : tobs_list}

    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>")
def start_date(start):
    """Returns a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    # Query results
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    calc_temps = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
           filter(Measurement.date >= start).\
           group_by(Measurement.date).order_by(Measurement.date.desc()).all()

    I = range(len(calc_temps))
    dates = [calc_temps[i][0] for i in I]
    minimum = [calc_temps[i][1] for i in I]
    average = [calc_temps[i][2] for i in I]
    maximum = [calc_temps[i][3] for i in I]

    df_calc_temps = pd.DataFrame({'date':dates,
                                  'min':minimum,
                                  'ave':average,
                                  'max':maximum})

    dictionary = {
    "date" : dates,
    "min_temp" : minimum,
    "avg_temp" : average,
    "max_temp" : maximum
    }

    return jsonify(dictionary)

@app.route("/api/v1.0/<start>/<end>")
def dates(start, end):
    """Returns a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    # Query results
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
           filter(Measurement.date >= start).\
           filter(Measurement.date <= end).\
           group_by(Measurement.date).order_by(Measurement.date.desc()).all()

    I = range(len(calc_temps))
    dates = [calc_temps[i][0] for i in I]
    minimum = [calc_temps[i][1] for i in I]
    average = [calc_temps[i][2] for i in I]
    maximum = [calc_temps[i][3] for i in I]

    df_calc_temps = pd.DataFrame({'date':dates,
                                  'min':minimum,
                                  'ave':average,
                                  'max':maximum})

    dictionary = {
    "date" : dates,
    "min_temp" : minimum,
    "avg_temp" : average,
    "max_temp" : maximum
    }

    return jsonify(dictionary

if __name__ == "__main__":
    app.run(debug=True)
