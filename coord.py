def convert_coco_to_yolo(coco_coords, image_width, image_height):
    # CoCo coordinates [xmin, ymin, width, height]
    xmin, ymin, width, height = coco_coords
    
    # Calculate center coordinates 
    center_x = (xmin + width/2) / image_width
    center_y = (ymin + height/2) / image_height
    
    # Calculate relative width and height
    relative_width = width / image_width
    relative_height = height / image_height
    
    # YoLo coordinates [center_x, center_y, relative_width, relative_height]
    yolo_coords = [center_x, center_y, relative_width, relative_height]
   
    return yolo_coords


width = 640
height = 360

bbox = [447, 124, 177, 190]

print(convert_coco_to_yolo(bbox, width, height))