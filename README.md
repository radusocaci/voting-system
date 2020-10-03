# Voting System featuring Face Recognition

Online voting application developed in a team setup, at university. Using the application, a user can create an account and vote in one of the available elections. The elections are created and populated by admins using a special admin view.

Being a voting application we made it as secure as possible. In order to be able to vote you need to be logged in, verify your email and provide all required data (the data is checked for validity) such as CNP (Romania's Social Security Number), name, profile picture, etc. Moreover, when pressing the "vote now" button the system will take a photo using the webcam and check that the face matches the one provided in the profile picture. In case no profile picture is present or the user does not have a webcam, the vote is discarded.

The application uses an MVP (Model View Presenter) architecture implemented using Django + Python. The front-end was developed using basic HTML, CSS (Bootstrap 4) and JS. All the information is saved in MongoDB (which we ran in a separate docker container). 
