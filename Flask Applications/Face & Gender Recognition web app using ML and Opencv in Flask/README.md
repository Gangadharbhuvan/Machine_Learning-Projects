# Face and Gender Recognition web app using Machine Learning and OpenCV in Flask
![Face Recognition](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/young-man-face-recognition-biometric-verification-165406876.jpg)
### This is the project created in Flask, the front-end is developed with HTML,CSS,Bootstrap and back-end in entirely in Python, all together running in the Flask WebServer.

<hr> 

## Demo:
![HomePage](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/Home_page.png)

## Pipeline:
![Pipeline](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/model_pipeline.png)

<hr>

![Male](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/male_recognition.png)

<hr>

![Female](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/female_recognition.png)

<hr>

![Group](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/both_gender_recognition.png)


<hr>

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

<hr>

### Download the dataset:
[Download faces data (1GB)](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)

[Download haarcascae classifier (face)](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

<hr>

## Project Overview:
**Objective**: Create a Gender Classification Model and Integrate to Flask App, task is to develop a ML model which should automatically detect faces and classify gender.

**Deliverables**: Developa Flask app and integrate to ML model, User will upload a image and app (RestAPI web server) has to detect the face and identify gender.

<hr>

**High Level Diagram**: 
![Pipeline](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/pipeline.png)

## Machine Model Application Flow: 
Upload Image -> Crop Image(face) -> Data Preprocessing -> Feature Extraction -> ML Model -> Output

<hr>

## Flask:
![Flask](https://github.com/Gangadharbhuvan/Machine_Learning-Projects/blob/master/Flask%20Applications/Face%20%26%20Gender%20Recognition%20web%20app%20using%20ML%20and%20Opencv%20in%20Flask/Face_Recognition-Flask_app/images/Flask-webapp.png)

- Installation - ``` pip install flask ```

**Flask** - Its a lightweight WSGI (Web Server Gateway Interface) web application framework
- Its designed to make quick & easy web app
- Has ability to scale up complex applicationn
- written in Python.

<hr>

## To Run this app in Localhost:
- clone this website
- cd to flask app folder
- run ``` python main.py ```
