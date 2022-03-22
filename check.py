def check(root,x,y):
    for child in root.children:
        bbox = child.bbox
        if x >= bbox[0] and x <= bbox[1] and y >= bbox[2] and y <= bbox[3]:
            return child
