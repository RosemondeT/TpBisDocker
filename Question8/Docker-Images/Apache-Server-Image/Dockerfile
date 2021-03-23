FROM ubuntu:latest
MAINTAINER rosemondetraore <benedicte.rosemonde.traoregmail.com>
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get clean
RUN mv /var/lib/apt/lists /tmp
RUN mkdir -p /var/lib/apt/lists/partial
RUN apt-get clean
RUN apt-get update

RUN apt-get -y install apache2
RUN apt-get -y install git
RUN apt-get -y install nano
RUN git config --global user.name "RosemondeT"
RUN git config --global user.email traore.rose.benedicte@gmail.com
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

RUN mkdir /var/www/html/AppliWeb
RUN git clone https://github.com/shehryarkn/PHP-MySQL-CRUD-Web-Application.git /var/www/html/AppliWeb
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND
