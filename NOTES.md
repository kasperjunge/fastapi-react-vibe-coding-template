# Run Local Postgres db in Docker Container
docker run --name local-postgres \
  -e POSTGRES_DB=db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres

# Access Local Postgres db in Docker Container
docker exec -it local-postgres psql -U postgres -d db