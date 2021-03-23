FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE hospital
COPY ./hospital_db.sql /docker-entrypoint-initdb.d/
