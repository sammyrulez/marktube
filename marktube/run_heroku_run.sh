#!/bin/bash
. bin/activate
pip -E . install --upgrade gunicorn
cd marktube
../bin/gunicorn_django -b 0.0.0.0: -w 1
