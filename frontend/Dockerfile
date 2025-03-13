FROM node:latest

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Build the frontend
RUN npm run build

# Expose port 5173 (default for Vite)
EXPOSE 5173

# Start the frontend in production mode
CMD ["npm", "run", "preview"]
