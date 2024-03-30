# Use the official Python 3.12 image from Docker Hub
FROM python:3.12

RUN  apt-get update -y       && \
     apt-get upgrade -y      && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove   && \
     apt-get clean
RUN apt-get install -y p7zip \
                  p7zip-full \
                       unace \
                         zip \
                       unzip \
                    xz-utils \
                   sharutils \
                    uudeview \
                       mpack \
                         arj \
                  cabextract \
                 file-roller \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./awslambda /app

# Copy the requirements file into the container at /app
COPY ./awslambda/awsrequirements.txt /app

RUN find /app -name '*.py' -exec sed -i 's/awslambda.helpers/helpers/g' {} \;

# Install any needed packages specified in awsrequirements.txt
RUN pip install -r awsrequirements.txt --platform manylinux2014_x86_64 --target /app --only-binary=:all:

# docker build -t lambda-bando-app . && docker run --rm -v $(pwd):/tmp lambda-bando-app zip -r /tmp/lambda_package.zip .
