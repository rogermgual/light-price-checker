FROM python:3-alpine

#stablish workind directory
WORKDIR /app

#copies files to be build inside the image
COPY start.sh /app
COPY bin/main.py /app
COPY requirements.txt /app

#install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#runs script
CMD ["sh", "start.sh"]