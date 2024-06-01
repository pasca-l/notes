FROM node:20

ENV HOME /home/local/app/
WORKDIR /home/local/app/

# project should be already initialized with `npm init`
# to create `package.json` file
COPY */package.json ./

RUN apt-get update && apt-get upgrade -y
# returns 0 status even if package.json does not exist (not initialized)
RUN npm install; exit 0
