FROM 0x7c/chuthe_lib:latest

COPY . /app
WORKDIR /app
RUN chmod +x entrypoint.sh
CMD ["/bin/bash", "entrypoint.sh"]