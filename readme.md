# Finding-Similarities-between-the-textual-content-of-the-documents
Cleansing of data for text mining and finding similarities between documents using Jacard and cosine similarities. And computed similarity in two document samples.

### TABLE OF CONTENTS
* [Objective](#objective)
* [Technologies](#technologies)
* [Algorithms](#algorithms)
* [Data](#data)
* [Implementation](#implementation)
* [Results](#results)
* [Instructions](#instructions)

## OBJECTIVE 
Finding the closeness between document samples using basics of NLP. Implementing basics of text similarity on multiple files and presenting the analysis.

## TECHNOLOGIES
Project is created with:

* Python
* Flask API
* Docker

## ALGORITHMS
* Jacard Similarity 
* Cosine Similarity

## IMPLEMENTATION

**Cosine Similarity**: Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. Any document can be represented by thousands of attributes, each recording the frequency of a particular word (such as a keyword) or phrase in the document. Thus, each document is an object represented by what is called a term-frequency vector.
I have tried implementing similar logic by using dictionary key:value pair as word as key and its frequency as value. if the key is same in two document samples, then multiply the values and add all of them to get the final dot product. Divide this summation by dot products of both the documnets to get the final percentage.  


## RESULTS

I have used python function to calculate the text similarity rather and deployed it as docker image using flask. The Docurhub repository is publicaly accessible and can be used by anyone to fetch and run the docker image (app) on their system

## INSTRUCTIONS
Follow the instructions to successfully run the created app:

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
