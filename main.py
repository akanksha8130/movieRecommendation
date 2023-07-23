from flask import Flask,jsonify
import csv 
from demographic import output
import pandas as pd
from contentbased import get_recommendations

all_movies=[]
liked_movies=[]
did_not_liked_movies=[]
did_not_watch_movies=[]

with open('final.csv',encoding='utf8') as f:
    a=csv.reader(f)

    data=list(a)
    all_movies=data[1:]

app=Flask(__name__)

@app.route('/getmovie')
def getmovie():
    return jsonify({
        'data':all_movies[0],
        'status':'success'
    })

@app.route('/likemovie',methods=['POST'])
def likemovie():
    movies=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.apend(movies)
    return jsonify({
        'status':'success'
    })



@app.route('/unlikemovie',methods=['POST'])
def unlikemovie():
    movies=all_movies[0]
    all_movies=all_movies[1:]
    did_not_liked_movies.apend(movies)
    return jsonify({
        'status':'success'
    })

@app.route('/notwatchmovie',methods=['POST'])
def not_watch_movie():
    movies=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watch_movies.apend(movies)
    return jsonify({
        'status':'success'
    })




if __name__=="__main__":
    app.run()