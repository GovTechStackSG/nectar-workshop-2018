# Using official python runtime base image
FROM python:2.7-alpine

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
ENV FLASK_APP="/app/app.py"
RUN easy_install `cat requirements.txt`

# Copy our code from the current folder to /app inside the container
ADD . /app

RUN chown -Rf root:root /app
RUN chmod -Rf g+rwx /app

# Make port 80 available for links and/or publish
# This EXPOSE port will automatically be captured on Nectar portal portal when adding 'route'
EXPOSE 5000

# Define our command to be run when launching the container
CMD flask run --host=0.0.0.0
