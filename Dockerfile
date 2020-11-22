# pull from python 3 official docker image which includes ubuntu OS as well with it.
FROM python:3 

LABEL Maintainer="Andrew Pappas <andrewpap1997@gmail.com>"

# create the working directory inside the docker image. 
WORKDIR /shorty

# copy the requirements.txt file to the current working directory that we created above.
COPY ./requirements.txt .

# install the dependencies and make sure there's no cache
RUN pip install --no-cache-dir -r requirements.txt

# copy all the files of our local directory inside the docker's current working directory
COPY . /shorty

# run the application
CMD ["python", "run.py"]