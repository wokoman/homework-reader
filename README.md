# Homework Reader 🔎 🐙

This is a simple Python script that does one thing - connects to provided MySQL database and blurs the content of `keboola` table.

It needs these OS environment variables to be set:

- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

It's a Flask app, so it exposes standard 5000 port.

Docker image is available directly from this repo's packages: `ghcr.io/keboola/homework-reader:latest`
