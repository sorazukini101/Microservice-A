1) How to request data from Microservice A:

The following screenshot shows a terminal for the Microservice A in (MicroserviceA.py) and a terminal for the tester in (Microservice_tester.py).
Make sure that you cd (change directory) into the correct folder where the two files, MicroserviceA.py and Microservice_tester.py are located.
First, run Microservice A (MicroserviceA.py) in the first terminal by typing the command "python MicroserviceA.py", secondly, run the tester
(Microservice_tester.py) in a seperate terminal by typing the command "python Microservice_tester.py". Then you will be prompted in the terminal
where Microservice_tester.py is running, "Enter music format (vinyl, cd, cassette):  ", which you will enter either "vinyl", "cd", or "cassette".

MicroserviceA.py terminal:
![image](https://github.com/user-attachments/assets/24a6cf56-6b44-4727-a849-07638ca43ce0)

Microservice_tester.py:
![image](https://github.com/user-attachments/assets/7a867e2b-eeab-4674-80be-eac533984626)

Example code:
![image](https://github.com/user-attachments/assets/07a45e35-caac-4027-b1b6-d46bff45806f)
![image](https://github.com/user-attachments/assets/e857ad60-f1f8-4451-8b02-e5a75e1c4a94)

Example code description:
This code shows the HTTP request library being imported, where we then prompt the user for user input (vinyl, cd or cassette), then sends
the response request to MicroserviceA.py using GET.


2) How to receive data from Microservice A:

The following screenshot shows how to receive data from the Microservice A, specifically recieving output data in the Microservice_tester.py terminal.
Building off from "1) How to request data from Microservice A:", once you enter a valid input, you will then receive the requested data which will be
outputted in your terminal.

Microservice_tester.py:
![image](https://github.com/user-attachments/assets/c0aac271-03cc-4905-adc4-e15d2d8f3446)

Example code:
![image](https://github.com/user-attachments/assets/5fed4b78-9e0e-4657-8487-3158aad46859)

Example code description: 
This code recieves the response request and checks if the user input is within the mock database and returns either the requested information or an error.


3) UML sequence diagram:
![image](https://github.com/user-attachments/assets/7a79b032-60ab-42d2-afea-43577b1cfa1e)
