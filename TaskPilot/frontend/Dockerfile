# Stage 1: Build the React application
FROM node:18-alpine as build

WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application's source code
COPY . .

# Build the application for production
RUN npm run build

# Stage 2: Serve the built application with Nginx
FROM nginx:1.23-alpine

# Copy the build output from the build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# The command to start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]