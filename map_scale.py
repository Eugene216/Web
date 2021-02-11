def scale(toponym):
    coordinates = toponym['boundedBy']['Envelope']
    delta_x = float(coordinates['lowerCorner'].split()[0]) - float(coordinates['upperCorner'].split()[0])
    delta_y = float(coordinates['lowerCorner'].split()[1]) - float(coordinates['upperCorner'].split()[1])
    return delta_x, delta_y
