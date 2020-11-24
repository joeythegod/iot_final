from flask import Flask, render_template
from flask import jsonify
from flask import request
# from flask_pymongo import PyMongo
import json
import os
from detect_mask_image import mask_image

app= Flask(__name__)
app.config['UPLOAD_FOLDER'] = "images"

# app.config['MONGO_DBNAME']= 'coordinates'
# app.config['MONGO_URI']= 'mongodb://localhost:27017/coordinates'
# mongo= PyMongo(app)

# @app.route('/post', methods=['POST'])
# def add_coordinate():   
    # data = None
    # label= None
    # coordinate= mongo.db.coordinates

    # data= request.json["data"]
    # label= request.json["label"]
    # print(label) 
    
    # coordinate.insert({'data': data, 'label': label})
    # new_coordinate=coordinate.find_one({'data': data} and {'label':label})
    # output = {'data': new_coordinate['data'], 'label':new_coordinate['label']}                 
    # return jsonify({'result':output})


# @app.route('/get', methods=['GET'])
# def get_coordinate():
    # coordinate= mongo.db.coordinates
    # output= []
    # for c in coordinate.find():
        # output.append({'data': c['data'], 'label': c['label']})
    # return jsonify({'result' : output})

@app.route('/post', methods=['POST'])
def infer():
    file = request.files["image"]
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)
    results = mask_image(save_path)
    return jsonify({'results':results})

if __name__== '__main__':
    # coordinate= mongo.db.coordinates
    # coordinate.delete_many({})
    app.run(debug=True, host="0.0.0.0", port= 80)




