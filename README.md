Build the container image

docker build -t agentic-ai-k8s .

Run the image

docker run -p 8080:8080 agentic-ai-k8s
