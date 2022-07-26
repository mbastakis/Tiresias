#!/bin/bash

gunicorn --workers=$1 app:app --timeout 120 --daemon;
