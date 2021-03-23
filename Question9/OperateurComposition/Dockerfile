
FROM ubuntu:latest
MAINTAINER rosemondetraore <benedicte.rosemonde.traore@gmail.com>

ENV TZ=Europe/Paris

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update

RUN apt-get -y upgrade

RUN apt-get install -y git

RUN apt-get -y install apache2

RUN mkdir /var/www/html/medibed

RUN git clone https://github.com/shehryarkn/PHP-MySQL-CRUD-Web-Application.git /var/www/html/medibed

ENV APACHE_RUN_USER www-data

ENV APACHE_RUN_GROUP www-data

ENV APACHE_LOG_DIR /var/log/apache2

ENV APACHE_LOCK_DIR /var/lock/apache2

ENV APACHE_PID_FILE /var/run/apache2.pid

EXPOSE 80

CMD /usr/sbin/apache2ctl -D FOREGROUND