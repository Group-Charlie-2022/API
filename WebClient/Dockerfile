FROM node:16.13.0

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci --only=production

COPY . ./

CMD ["npm", "start"]