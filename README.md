# compose-pushpin
An example of pushpin in docker-compose

# run 

    virtualenv venv
    . venv/bin/activate

    pip install docker-compose

    docker-compose up -d
    docker-compose scale backend=3

    pip install -r requirements.txt
    pip install locust

    locust  --host=http://127.0.0.1:33649  --print-stats -c 10000 -r 100 --no-web

