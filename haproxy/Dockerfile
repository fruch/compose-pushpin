FROM asteris/consul-template:latest

# Alpine Linux didn't publish HAProxy 1.5.x in main repos yet
RUN echo http://dl-4.alpinelinux.org/alpine/edge/main > /tmp/new_repo
RUN apk update --repositories-file /tmp/new_repo
RUN apk add --repositories-file /tmp/new_repo haproxy openssl-dev

WORKDIR /consul-template
ADD haproxy.cfg.tmpl ./
ADD run.sh /tmp/
RUN chmod +x /tmp/run.sh

EXPOSE 80

ENTRYPOINT ["/tmp/run.sh"]
