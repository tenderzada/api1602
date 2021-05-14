from core import process, predict


def c_main(path, model, ext):
    image_data = process.pre_process(path)
    image_info, pred_boxes = predict.predict(image_data, model, ext)

    return image_data[1] + '.' + ext, image_info, pred_boxes


if __name__ == '__main__':
    pass
