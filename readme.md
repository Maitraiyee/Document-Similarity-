<b>COPY all the above file into one single folder before running the python
file.</b>

<b>TO RUN PYTHON FILE LOCALY AND CHECK THE RESULT:</b>

1.  Run app.py with templates subfolder containing index.html file in
    the same project folder. 
    Document\_similarity --\>app.py, templates
    -\>\> index.html
2.  The link to run app locally on web browser is "0.0.0.0:5000" for
    linux/ubuntu. For windows, type "localhost:5000" on web browser to
    run the app.

Alternative:

1.  Run Document\_Similarity.py on windows and check the link in console
    to run the app.

<b> RUNNING DOCKER IMAGE LOCALLY:</b>

1.  Build docker image : docker build -t flaskapp:version1 .
2.  Run the images : docker run -it -p 5000:5000 flaskapp:version1
3.  (Optional) Check if the container is running: sudo docker ps
4.  Open browser and hit http://localhost:5000/ or "0.0.0.0:5000" for
    linux/ubuntu.
5.  To stop the container: docker kill <container-id>

<b>RUNNING DOCKER IMAGE FROM DOCKERHUB:</b>

Pushing the image:

1.  Create Docker hub account.
2.  Create a repository in dockerhub.
3.  Add a tag to the local docker image : docker tag flaskapp:version1
    maitraiyee/flaskapp:version1
4.  Push the image to dockerhub : docker push
    maitraiyee/flaskapp:version1

Fetching and Running the image:

1.  Pull the image : docker pull maitraiyee/flaskapp:version1
2.  Run the downloaded image : docker run -it -p 5000:5000
    maitraiyee/flaskapp:version1

Note : The above instructions are to run the docker on windows, in app.py localhost-0.0.0.0 has been used so as to make the app version compatible with linux; ubuntu. please use "localhost:5000" in the web browser to run the same app on windows.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
