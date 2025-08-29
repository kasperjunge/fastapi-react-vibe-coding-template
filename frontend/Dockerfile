# Use official Node 20 base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm ci

# Copy the rest of your code
COPY . .

# Build the Vite app
RUN npm run build

# Use a lightweight web server to serve the app
RUN npm install -g serve
CMD ["serve", "-s", "dist"]