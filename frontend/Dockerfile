# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Build the frontend
RUN npm run build

# Expose port 5173 (Vite default) or 3000 if using React scripts
EXPOSE 5173

# Start the frontend in production mode
CMD ["npm", "run", "preview"]