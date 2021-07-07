#!/usr/bin/env bash
echo "testing 1 2 3..."
curl "etportfolio.duckdns.org/health/"
curl -X POST -d "username=testUsername" "etportfolio.duckdns.org/register"
curl -X POST -d "username=testPassword" "etportfolio.duckdns.org/register"
curl -X POST -d "username=testUsername&password=testPassword" "etportfolio.duckdns.org/register"
curl -X POST -d "username=testUsername" "etportfolio.duckdns.org/login"
curl -X POST -d "password=testPassword" "etportfolio.duckdns.org/login"
curl -X POST -d "username=testUsername&password=testPassword" "etportfolio.duckdns.org/login"