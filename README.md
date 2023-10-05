# Chatbox Sandbox local setup tutorial
### ***note: this project is still very work in progress***

---
#### Follow these steps to set up and run the chatbot sandbox on your local environment using Docker Desktop:

### 1. **Download the Repository**

### 2. **Configure Environment Variables**
   - Copy the provided `.env.example` file and rename it to `.env`.
   - Open the `.env` file and set the HuggingFace API KEY.
   

### 3. **Start the Container with Docker Compose**
   - Open a terminal.
   - Navigate to the project's root directory.
   - Run the following command to start Docker Compose.

```bash
docker-compose up -d
```

### 4. **Get the ID of the Chatbox Sandbox Container**
   - Find the CONTAINER ID of the container you've just built using `docker ps`. 
```bash
docker ps
```

### 5. **Enter the Container**
   - Use the container ID to enter into the container
```bash
docker exec -it {container id} /bin/sh
```