FROM python:3
ADD . /PYTHON-OC-LETTINGS-FR/
WORKDIR /PYTHON-OC-LETTINGS-FR/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
&& pip install python-decouple
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]