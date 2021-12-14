#Use Python 3.7 as a base image
FROM python:3.7
#Create a work directory
WORKDIR /app
#Copy contents into image
COPY . .
#install pip dependencies from requirements file
RUN pip3 install -r requirements.txt
#Create an entrypoint
ENTRYPOINT ["gunicorn", "--workers=2", "-b", "0.0.0.0:5000", "app:app"]
COPY . .