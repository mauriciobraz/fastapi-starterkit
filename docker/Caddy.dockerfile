FROM caddy/caddy:2.7.5-alpine

WORKDIR /app
COPY Caddyfile /etc/caddy/Caddyfile

ENV CADDY_DOMAIN=localhost

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
