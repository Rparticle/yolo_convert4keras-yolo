import sys

if len(sys.argv) != 4:
    print('Prease write like this:\nconv.py [annotation_file_path(without\'/\')] [image_width] [image_height]\n')
    sys.exit()

path = sys.argv[1]
image_width = int(sys.argv[2])
image_height = int(sys.argv[3])

newFile = open('train.txt', mode='w')
for i in range(1070):
    name = path + '/{:04}.txt'.format(i)
    try:
        f = open(name, mode='r')
    except:
        continue
    
    fileLine = 'img/'+'{:04}'.format(i)+'.jpg'
    lines = f.readlines()
    for line in lines:
        points = line.split()
        print(points)
        class_num = points[0]
        center_x = float(points[1])
        center_y = float(points[2])
        obj_w = float(points[3])
        obj_h = float(points[4])

        x_min = int((center_x-(obj_w/2))*image_width)
        y_min = int((center_y-(obj_h/2))*image_height)
        x_max = int((center_x+(obj_w/2))*image_width)
        y_max = int((center_y+(obj_h/2))*image_height)
        fileLine += ' {},{},{},{},{}'.format(x_min, y_min, x_max, y_max, class_num)
    fileLine += '\n'
    newFile.write(fileLine)