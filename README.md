Docker Microservices Calculator
A demonstration of Docker microservices architecture using three containers that work together to process numerical data. The first container accepts two numbers as input, the second container performs addition, and the third container stores the result.
Project Overview
This project showcases:

Basic microservices architecture
Container communication using Docker volumes
Service orchestration with Docker Compose
Sequential processing pipeline in containerized environments

Components
The system consists of three containers:

Input Container: Accepts two numbers as command-line arguments and saves them to a shared volume
Calculator Container: Reads the numbers from the shared volume, adds them together, and writes the result
Storage Container: Reads the result and stores it (prints confirmation)

Prerequisites

Docker and Docker Compose installed on your system
Basic understanding of Docker concepts

How to Use

Clone this repository:

bashgit clone https://github.com/yourusername/docker-microservices-calculator.git
cd docker-microservices-calculator

Build the Docker images:

bashdocker-compose build

Run the application with your desired numbers (e.g., 5 and 7):

bashdocker-compose run --rm input 5 7

Check the results:

bashdocker-compose logs calculator
docker-compose logs storage
File Structure
docker-microservices-calculator/
├── input.py                # Script for the input container
├── calculator.py           # Script for the calculator container
├── storage.py              # Script for the storage container
├── Dockerfile.input        # Dockerfile for the input container
├── Dockerfile.calculator   # Dockerfile for the calculator container
├── Dockerfile.storage      # Dockerfile for the storage container
└── docker-compose.yml      # Orchestration configuration
How It Works

The containers communicate through a shared Docker volume mounted at /data
The input container writes numbers to /data/numbers.txt
The calculator container reads the numbers, computes the sum, and writes it to /data/result.txt
The storage container reads the result and "stores" it (prints confirmation)

Learning Objectives
This project demonstrates several key Docker concepts:

Building custom Docker images
Container orchestration with Docker Compose
Data sharing between containers
Designing a simple microservices architecture

License
MIT
Contributing
Feel free to submit issues or pull requests with improvements or suggestions!
