
### Redis Docker
```bash
docker run --name rq-redis -d redis
```

## Prepare environment 🐧
1 - Install all dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - Execute Worker
```bash
python3 worker.py
```

3 - Execute App
```bash
python3 app.py
```
