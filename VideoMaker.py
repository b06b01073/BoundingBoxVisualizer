import cv2
import os
from collections import defaultdict
import numpy as np
from tqdm import tqdm


class VideoMaker:
    def __init__(self):
        self.palette = Palette()

    def find_camera(self, file_name):
        return file_name.split('_')[0]
    

    def build_camerawise_data(self, image_dir, label_dir):

        image_list = os.listdir(image_dir)
        image_dict = defaultdict(list)
        for image in image_list:
            camera = self.find_camera(image)
            image_dict[camera].append(os.path.join(image_dir, image))

        for value in image_dict.values():
            value.sort()


        label_list = os.listdir(label_dir)
        label_dict = defaultdict(list)
        for label in label_list:
            camera = self.find_camera(label)
            label_dict[camera].append(os.path.join(label_dir, label))
        
        for value in label_dict.values():
            value.sort()

        return image_dict, label_dict


    def make(self, image_dir, label_dir, save_path):
        image_dict, label_dict = self.build_camerawise_data(image_dir, label_dir)
        self.make_video(image_dict, label_dict, save_path)
        
        

    def make_video(self, image_dict, label_dict, save_dir):
        camera_set = image_dict.keys()
        
        for camera in tqdm(camera_set, dynamic_ncols=True, desc='processing camera'):
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
            out = cv2.VideoWriter(os.path.join(save_dir, f'camera_{camera}.mp4'), fourcc, 2, (1280, 720))

            for label, image in zip(label_dict[camera], image_dict[camera]):
                image = cv2.imread(image)

                height, width, _ = image.shape
                bounding_boxes = self.get_bounding_boxes(label)

                for box in bounding_boxes:
                    x1, y1, x2, y2 = self.cv2_bbox_adaptor(height, width, box)



                    color = self.palette.get_color(box[4])
                    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2) # add bounding box


                    cv2.putText(image, text=str(box[4]), org=(x1, y1 - 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=color, thickness=3) # add id text

                text = f'Camera {camera}'

                # Define the font and scale
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1

                # Get the size of the text
                text_size = cv2.getTextSize(text, font, font_scale, thickness=1)[0]

                # Calculate the position of the text
                text_x = image.shape[1] - text_size[0] - 10  # 10 pixels padding from the right edge
                text_y = image.shape[0] - 120  # 10 pixels padding from the bottom edge
                cv2.putText(image, text, (text_x, text_y), font, font_scale, (255, 255, 255), thickness=3)
                out.write(image)


            out.release()



    def cv2_bbox_adaptor(self, height, width, box):
        center_x = width * box[0]
        adjusted_width = width * box[2] / 2

        center_y = height * box[1]
        adjusted_height = height * box[3] / 2

        return int(center_x - adjusted_width), int(center_y - adjusted_height), int(center_x + adjusted_width), int(center_y + adjusted_height)


    def get_bounding_boxes(self, label):
        with open(label) as f:
            def process_raw_box(box):
                box = box[1:]
                box[0] = float(box[0]) # center_x
                box[1] = float(box[1]) # center_y
                box[2] = float(box[2]) # width
                box[3] = float(box[3]) # height
                box[4] = int(box[4]) # track_ID

                return box


            return [process_raw_box(line.rstrip().split(' ')) for line in f.readlines()]


class Palette:
    def __init__(self):     
        self.colors = {}

    def get_color(self, id):
        if not id in self.colors:
            color = list(np.random.choice(range(256), size=3))
            color = (int(color[0]), int(color[1]), int(color[2]))

            self.colors[id] = color

        return self.colors[id]
        
