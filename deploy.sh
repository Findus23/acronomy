#!/bin/bash
set -x
set -e

python="/srv/venv/acronomy/bin/python"

manage="sudo -u acronomy $python manage.py"

git pull

$manage scss
npm run build
$manage collectstatic --noinput
$manage migrate
$manage clearcache

sudo systemctl reload acronomy.service
