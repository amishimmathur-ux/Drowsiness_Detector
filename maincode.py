#import lib
import cv2
import os
import numpy as np
import pygame
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#file path
train_data_path='Train'
categories =['Active', 'Fatigue']
    
#data labeling and preprocessing
labels=[]
data=[]

print("Data scanning.")  


for category in categories:
    folder_path=os.path.join(train_data_path, category)
    label=categories.index(category)
    print(f"Scanning category: {category}")
    
    
    for img_name in os.listdir(folder_path):
        img_path=os.path.join(folder_path, img_name)
        img=cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img=cv2.resize(img,(128, 128))
            data.append(img.flatten())
            labels.append(label)

print("Data scanning complete.")  


labels= np.array(labels)
data= np.array(data)

#Train test split
X_train, X_test, y_train, y_test= train_test_split(data, labels, test_size=0.2, random_state=42)

#SVM model training
svm_classifier= svm.SVC(kernel ='linear')
svm_classifier.fit(X_train, y_train)


y_pred=svm_classifier.predict(X_test)


accuracy =accuracy_score(y_test, y_pred)
print(f"Model accuracy -> {accuracy * 100:.2f}%")

#Camera feed and real-time prediction
cap=cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    if not ret:
        break

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_resized= cv2.resize(gray, (128, 128))  
    gray_resized =gray_resized.flatten().reshape(1, -1)


    prediction=svm_classifier.predict(gray_resized)
    label='Active' if prediction[0] == 1 else 'Drowsy'  

    
    if label=='Drowsy':
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/amish/OneDrive/Desktop/Projects/Drowsiness detector/soundshelfstudio-ui-alarm-clock-516360.mp3")
        pygame.mixer.music.play()  

   
    cv2.putText(frame, f"Status: {label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Camera Feed', frame)

#to close camera and stop operations
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()