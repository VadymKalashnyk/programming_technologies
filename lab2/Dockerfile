FROM alpine:latest
RUN apk add --update python3 py3-pip
RUN pip3 install --break-system-packages flask
WORKDIR /app
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]