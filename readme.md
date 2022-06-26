# Airport Arrivals Departures Scraper

## Build and run

```bash
sudo docker build -t airport-arrivals-departures-scraper .
sudo docker run -d \
    --name airport-arrivals-departures-scraper \
    -p 5000:5000 \
    --restart on-failure \
    airport-arrivals-departures-scraper
```