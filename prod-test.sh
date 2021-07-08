#!/usr/bin/env bash
echo "testing 1 2 3..."
curl "etportfolio.duckdns.org/health/"
curl -X POST -d "username=testUsername" "https://etportfolio.duckdns.org/register" -L
curl -X POST -d "username=testPassword" "https://etportfolio.duckdns.org/register" -L
curl -X POST -d "username=testUsername&password=testPassword" "https://etportfolio.duckdns.org/register" -L
curl -X POST -d "username=testUsername" "https://etportfolio.duckdns.org/login" -L
curl -X POST -d "password=testPassword" "https://etportfolio.duckdns.org/login" -L
curl -X POST -d "username=testUsername&password=testPassword" "https://etportfolio.duckdns.org/login" -L