FROM postgres:latest
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=admin
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql