# Import node v16 from DockerHub
FROM node:16-buster

# Define the application directory
WORKDIR /web

# Copy the file to the Docker image
COPY package.json .

# Run the command to install node modules
RUN npm install

# Copy the application repository in the Docker image
COPY / .