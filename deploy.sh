#!/bin/bash
set -x
set -e

python="/srv/venv/acronomy/bin/python"

manage="sudo -u acronomy $python manage.py"

git pull

$manage scss
$manage collectstatic --noinput
$manage migrate

sudo systemctl reload acronomy.service
