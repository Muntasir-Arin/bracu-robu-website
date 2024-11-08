# Use a Node base image
FROM node:20.18.0-alpine

# Set working directory
WORKDIR /web

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the Next.js application
RUN npm run build

# Expose the port Next.js will run on
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
