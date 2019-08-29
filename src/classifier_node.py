#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from detection_msgs.msg import DetectedObjectsWithImage 
from SiameseNet.model import SiameseNet

iteration = 0
model = SiameseNet('SiameseNet/configs/road_signs.yml')
model.load_model('{}best_model_4.h5'.format(model.weights_save_path))
model.load_encodings('{}encodings.pkl'.format(model.encodings_path))

def callback(data):
    global model, iteration
    detected_objects = data.objects
    np_arr = np.fromstring(data.image.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    img_h,img_w,c = image_np.shape
    rospy.loginfo("Frame {}".format(iteration))
    for bbox in detected_objects:
        
        x1 = int(bbox.x1 * img_w)
        y1 = int(bbox.y1 * img_h)
        x2 = int(bbox.x2 * img_w)
        y2 = int(bbox.y2 * img_h)
        sub_image = image_np[y1:y2,x1:x2,:]


        if bbox.class_id == 8 and x2-x1 >0 and y2-y1>0:
            prediction = model.predict(sub_image)
            cv2.putText(image_np,prediction,(x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
            rospy.loginfo("Detected road sign: {}".format(prediction))

        cv2.rectangle(image_np,(x1,y1),(x2,y2),(0,255,0),1)
    rospy.loginfo('\n')
    cv2.imwrite('images/image{}.png'.format(iteration),image_np)
    cv2.waitKey(1)
    iteration+=1
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/detections_source", DetectedObjectsWithImage, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()