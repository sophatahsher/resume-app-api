FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="sophatchhay.tech"

# copy current file location into docker image path
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

# set environment variables
ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    # create empty file
    touch /etc/nginx/conf.d/default.conf && \
    # set file owner user:group
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

# switching from root to nginx
USER nginx

CMD ["/run.sh"]