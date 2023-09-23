# -----------------------------------------------------------------
# Squirrel Detector Machine Learning Project
# Warren Wiens
# wwiens@gmail.com
# warren@semanticorchestration.com
# 
# SEE LICENSE.TXT FILE FOR LICENSE INFORMATION
# 
# Comment color coding using Better Comments:
# = Functions or sections
# ! Todo items
# ------------------------------------------------------------------

import json
import annotate

# Load the COCO JSON file
with open("coco.json", "r") as f:
    coco_data = json.load(f)

# Extract the list of images and annotations
images = coco_data["images"]
annotations = coco_data["annotations"]

# Create a list with the annotation IDs
imagelist = []
for annotation in annotations:
    imagelist.append(annotation["id"])



#= Function to get the annotation image information based on the ID
#==================================================================
def getImage(id):

    # Check to see if ID is in the list
    if id <= len(imagelist)-1:
        imageid = imagelist[id]
    else:
        return False
    
    # Find the annotation based on the ID we received
    annotation = annotate.annotation_search(imageid, annotations)
    
    # Find the image based on the image_id in the annotation
    image = annotate.image_search(annotation["image_id"], images)
    
    # Return a JSON object with the annotation and image information
    return {
            '[id': annotation["id"], 
            'image': image["file_name"], 
            'bbox': annotation["bbox"], 
            'last_update': annotation["last_update"], 
            'imagenumber': id,            
            'imagecount': len(imagelist)
            }

# =========== MAIN PROGRAM ===========


# The request ID will get back the numbered item from imagelist
requestid = 2


jsonimage = getImage(requestid)
print(jsonimage)
