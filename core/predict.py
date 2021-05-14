import cv2

def predict(dataset, model, ext):
    global img_y
    x = dataset[0].replace('\\', '/')
    file_name = dataset[1]
    print('x:',x)
    print('file:',file_name)
    x = cv2.imread(x)
    print('读取成功',type(x))
    img_y, image_info, pred_boxes = model.detect(x)
    # print("img_y:",img_y)
    # static\ct
    cv2.imwrite('static\draw\{}.{}'.format(file_name, ext), img_y)
    return image_info, pred_boxes