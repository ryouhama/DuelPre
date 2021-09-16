# DuelPre
DuelPre


## library

### Enviroment Setup

#### 1.Create env
```shell
cat << EOS > .env
DEBUG=True
DJANGO_SECRET_KEY=[Your Secret Key]
EOS
```

#### 2.Run server in docker
```shell
docker-compose up -d
```

### Commonly used

#### poetry update
```shell
p update
```

#### flake8
```shell
p run flake8
```

#### pytest
```shell
pytest
```
