# tracker
Productivity tracker

to run, please use Python 3 and above

start Server.py first and then use Client.py

---To deploy and run with docker---

Server
1. Change to server subdirectory of the project
2. View the dockerfile, copy each .py file listed after COPY into the server subdirectory (they will be in the parent directory)
3. create the image by entering:"docker image build -t server ." without quotation marks
4. to create and run the container: enter "docker container run --rm -it --name server -p 7654:7654 server"

Client
1. change to client subdirectory of the project
2. View the dockerfile, you should only have to copy newClient.py into the client subdirectory
3. run "docker image build -t client ."
4. run "docker container run --rm -it --name TaskImage client"
