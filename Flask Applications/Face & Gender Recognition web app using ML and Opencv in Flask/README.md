# Face and Gender Recognition web app using Machine Learning and OpenCV in FLask
![Face Recognition](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/young-man-face-recognition-biometric-verification-165406876.jpg)
### This is the project created in Flask, the front-end is developed with HTML,CSS,Bootstrap and back-end in entirely in Python, all together running in the Flask WebServer.

## Here, created the image processing application is Face Recognition. The task here is to detect the face along with the gender(Male/Female).

# Working:
Upload Image -> Process image in Flask app with ML Model -> Detect the Face & Gender.
Using this as a base, anyone can build more advanced app for Face Emotion detection and other so on.

### Installation:
- Install Python
- Anaconda Promt
- Create Virtual Environment
  - Windows -> To install -> ``` pip install --user virtualenv ``` then to create a new virtual Env -> ``` python -m venv FaceAI ``` (replace FaceAI with your own virtual Env name)
  - Linus -> ``` Python3 -m pip install -user virtualenv ``` then to create a new virtual Env -> ``` python3 -m venv FaceAI ```
  - Now a folder has been created in the name of virtual Env (FaceAI in this code), Go to the folder then, To activate that Virtual Environment
    - Windows -> ``` .\FaceAI\Scripts\activate ```
    - Linux -> ``` source FaceAI/bin/activate ```
- Requirements -> ``` pip install -r requirements.txt ```
- OpenCV - ``` pip install opencv-python ```

![OpenCV Python](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/opencv-python.png)

### Download the dataset:
[Download faces data (1GB)](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)

[Download haarcascae classifier (face)](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)



