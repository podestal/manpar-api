FROM python:3.10
WORKDIR /django
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python3", 'manage.py', 'runserver', '0.0.0.0:8000' ]