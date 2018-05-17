# Emotion-based-music-player
Emotion recognition using facial expression based music player


STEPS TO EXECUTE THIS PROGRAM:

* First create a folder and download the 'EMP.py', 'update_module' and 'haarcascade_frontalface_default' files in the same folder.
* To execute this program for the first time we should create .xml file by following the below steps.
* Open terminal (command prompt) from the same folder. (Shift+right click -> Open command window here)
* To successfully execute this program we need dataset, so to creat the dataset, we should give our own facial expression for Angry,      Happy, Sad, Nuetral and Surprise. to do that we should run below command in the command window.
   EMP.py --update
* By running above command the computer asks you to follow the orders and give expression to aquire your own dataset and it creates the .xml file.
* Once it collected the images and updating the model is done.
* Now you can find the folder with the name of "dataset" and it has subfolders of all the emotions and your images.
* Now you are ready to execute the EMP.py file.

Tip:
* Don't forget to add the songs in the same folder.
* The more number of peoples images, more the accuracy.
