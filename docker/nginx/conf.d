upstream backend {
    server web:8000;
}

server {

    listen 80;

    location / {
        proxy_pass http://backend;
    }

    location /static/ {
        alias /home/app/web/static/;
    }

    location /media/ {
        alias /home/app/web/media/;
    }
}