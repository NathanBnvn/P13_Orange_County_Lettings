FROM --platform=linux/arm64 python:3.7-alpine
ADD . /PYTHON-OC-LETTINGS-FR/
WORKDIR /PYTHON-OC-LETTINGS-FR/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]