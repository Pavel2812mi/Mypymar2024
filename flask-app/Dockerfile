FROM python:3.8
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
COPY templates /usr/src/app/templates
EXPOSE 5001
CMD ["python", "/usr/src/app/app.py"]