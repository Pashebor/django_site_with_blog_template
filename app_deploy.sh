#!/bin/bash
cd /opt && source env/bin/activate
echo 'Starting building an application'
echo 'Getting an app from git'
cd /opt/popup_maker_application && git pull origin develope
echo 'App fetched'
echo 'Stopping an Nginx server'
service nginx stop
echo 'Nginx server stopped'
echo 'Stopping a supervisor for gunicorn'
supervisorctl stop popupmaker
echo 'Gunicorn supervisor stopped'
echo 'Installing new packages for backend and frontend'
pip3 install -r requirements.txt && yarn install
echo 'Packages installed'
echo 'Perfoming a build bundle of an application'
yarn run build_prod && deactivate
echo 'Application successfuly builded'
echo 'Starting Nginx server'
service nginx start
echo 'Nginx server started'
echo 'Starting Gunicorn supervisor'
supervisorctl start popupmaker
echo 'Gunicorn supervisor started'
