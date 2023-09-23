
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
        