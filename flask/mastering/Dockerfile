FROM python:3.6.5
# Set working dir
WORKDIR /app
# Copy local contents into container
ADD . /app
# Install dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
