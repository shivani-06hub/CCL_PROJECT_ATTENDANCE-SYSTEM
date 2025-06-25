# CCL_PROJECT_ATTENDANCE-SYSTEM

### Project flow & explaination
- Run the project you have to register your face so that system can identify you, so click on register new student
- Click a small window will pop up in that you have to enter you ID and name and then click on `Take Image` button
- Clicking `Take Image` button A camera window will pop up and it will detect your Face and take upto 50 Images(you can change the number of Image it can take) and stored in the folder named `TrainingImage`. more you give the image to system, the better it will perform while recognising the face.
- Click on `Train Image` button, It will train the model and convert all the Image into numeric format so that computer can understand. we are training the image so that next time when we will show the same face to the computer it will easily identify the face.
- Click on `Automatic Attendance` ,you have to enter the subject name and then it can fill attendace by your face using our trained model.
- Create `.csv` file for every subject you enter and seperate every `.csv` file accoriding the subject
- CVew the attendance after clicking `View Attendance` button. It will show record in tabular format.

