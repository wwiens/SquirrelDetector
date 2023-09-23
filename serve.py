
#******************************************************************
#*  Squirrel Detector
#*  Warren Wiens
#*  wwiens@gmail.com
#*  Last updated: 2023-09-23
#*  License: MIT License (see LICENSE.TXT)
#******************************************************************

from flask import Flask, jsonify, request
from flask import render_template
import json
import numbers
import os
import datetime


#* Load the COCO JSON file
#******************************************************************
if os.path.exists('coco.json'):
    with open("coco.json", "r") as f:
        coco_data = json.load(f)


#* Extract the header info and list of images and annotations
#******************************************************************
info = coco_data["info"]
licenses = coco_data["licenses"]
categories = coco_data["categories"]
images = coco_data["images"]
annotations = coco_data["annotations"]


#* Create a list with the annotation IDs
#******************************************************************
imagelist = []
for annotation in annotations:
    imagelist.append(annotation["id"])


#= Function to save updated annotation information to the JSON file
#==================================================================
def updateJSON():
    if os.path.exists('coco.json'):
        with open('coco.json', 'r+') as f:
            payload = {
                "info": info,
                "licenses": licenses,
                "categories": categories,
                "images": images,
                "annotations": annotations
            }
            f.seek(0)
            f.truncate()
            json.dump(payload, f)


#= Function to get the annotation image information based on the ID
#==================================================================
def getImage(id):

    # Check to see if ID is in the list
    if id <= len(imagelist)-1:
        imageid = imagelist[id]
    else:
        return False
    
    #? Find the annotation based on the ID we received
    annotation = annotation_search(imageid, annotations)
    
    #? Find the image based on the image_id in the annotation
    image = image_search(annotation["image_id"], images)
    
    #? Return a JSON object with the annotation and image information
    return {
            '[id': annotation["id"], 
            'image': image["file_name"], 
            'bbox': annotation["bbox"], 
            'lastupdated': annotation["last_update"], 
            'imagenumber': id,            
            'imagecount': len(imagelist)
            }


#= Function to search for an annotation based on the ID
#==================================================================
def annotation_search(id, annotations):
    for annotation in annotations:
        if annotation['id'] == id:
            return annotation


#= Function to search for an image based on the ID
#==================================================================
def image_search(id, images):
    for image in images:
        if image['id'] == id:
            return image


#* Creates a Flask application
#******************************************************************
app = Flask(__name__)

#* Home page
#******************************************************************
@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html')

#* Collect images page
#******************************************************************
@app.route("/collect.html")
def collect():
    return render_template('collect.html')

#* Annotate images page
#******************************************************************
@app.route("/annotate.html")
def annotate():
    return render_template('annotate.html')

#* Train model page
#******************************************************************
@app.route("/train.html")
def train():
    return render_template('train.html')

#* Help page
#******************************************************************
@app.route("/help.html")
def help():
    return render_template('help.html')


#= REST API that will return the information about an image
#==================================================================
@app.route("/getimage")
def getimageinfo():
    #? Get current image information from the web request
    if 'id' in request.args:
        id = int(request.args.get('id')) - 1
        print(id)
    else:
        id = 0

    #? Get image and annotation information to send to the client
    jsonimage = getImage(id)
    if jsonimage == False:
        return {
            'imagenumber': 0,            
            'imagecount': 0
        }
    else:
        return jsonify(jsonimage)


#= Web service that initializes the annotation process
#==================================================================
@app.route("/annotateinit")
def annotateinit():
    numberImages = len(imagelist)
    numberAnnotationsLeft = 0
    numberManualAnnotations = 0
    numberAutoAnnotations = 0
    for obj in annotations:
        if obj["update_method"] == "auto":
            numberAutoAnnotations += 1
        elif obj["update_method"] == "manual":
            numberManualAnnotations += 1
        else:
            numberAnnotationsLeft += 1

    numberAnnotations = numberManualAnnotations + numberAutoAnnotations
    return jsonify({'numberImages': numberImages, 'numberAnnotations': numberAnnotations, 'numberAnnotationsLeft': numberAnnotationsLeft, 'numberManualAnnotations': numberManualAnnotations, 'numberAutoAnnotations': numberAutoAnnotations})


#= Web service that saves annotation changes
#==================================================================
@app.route("/annotation")
def annotation():
    #? Get current image information from the web request
    if 'id' in request.args:
        id = int(request.args.get('id')) - 1
    else:
        return("Invalid ID")

    #? Get the annotation information from the web request
    if 'width' in request.args:
        width = int(request.args.get('width'))
    else:
        width = 0

    if 'height' in request.args:
        height = int(request.args.get('height'))
    else:
        height = 0

    if 'left' in request.args:
        left = int(request.args.get('left'))
    else:
        left = 0

    if 'top' in request.args:
        top = int(request.args.get('top'))
    else:
        top = 0                

    annotations[id]['bbox'] = [left, top, width, height]
    annotations[id]['last_update'] = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    annotations[id]['update_method'] = "manual"
    annotations[id]['area'] = int(width * height)

    updateJSON()
    return("Annotation saved")


#= Start up the application
#==================================================================
if __name__ == "__main__":
    app.run(debug=True)