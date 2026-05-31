#!/bin/bash
docker compose exec -w /app/backend django python manage.py shell
