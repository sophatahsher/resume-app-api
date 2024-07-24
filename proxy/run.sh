#!/bin/sh

set -e

# copy and replace
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

# Output the resulting file for debugging purposes
#cat /etc/nginx/conf.d/default.conf

# start Nginx in Forground
nginx -g 'daemon off;'