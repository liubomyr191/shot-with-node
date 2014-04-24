server {
    listen   443; ## listen for ipv4; this line is default and implied
    #listen   [::]:443 default ipv6only=on; ## listen for ipv6

    root /var/www/nodeshot/public_html;
    index index.html index.htm;

    # error log
    error_log /var/www/nodeshot/projects/ninux/log/nginx.error.log error;

    # Make site accessible from hostanme
    # change this according to your domain/hostanme
    server_name nodeshot.yourdomain.com;

    # set client body size #
    client_max_body_size 5M;

    ssl on;
    ssl_certificate ssl/server.crt;
    ssl_certificate_key ssl/server.key;

    ssl_session_timeout 5m;

    ssl_protocols SSLv3 TLSv1;
    ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv3:+EXP;
    ssl_prefer_server_ciphers on;

    location / {
        uwsgi_pass 127.0.0.1:3031;
        include uwsgi_params;
        uwsgi_param HTTP_X_FORWARDED_PROTO https;
    }

    location /static/ {
        alias /var/www/nodeshot/projects/ninux/ninux/static/;
    }

    location /media/ {
        alias /var/www/nodeshot/projects/ninux/ninux/media/;
    }

    #error_page 404 /404.html;

    # redirect server error pages to the static page /50x.html
    #
    #error_page 500 502 503 504 /50x.html;
    #location = /50x.html {
    #       root /usr/share/nginx/www;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #       deny all;
    #}
}

server {
    listen   80; ## listen for ipv4; this line is default and implied
    listen   [::]:80 default ipv6only=on; ## listen for ipv6

    # Make site accessible from hostanme on port 80
    # change this according to your domain/hostanme
    server_name nodeshot.yourdomain.com;

    # redirect all requests to https
    return 301 https://$host$request_uri;
}
