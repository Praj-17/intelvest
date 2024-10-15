# Intelvest 
## A portfolio Management System by jnanamarga

### Setup instructions

1. Install python == `3.12.3`

2. Create a Virtual envirnoment in the root folder - `intelvest`

```
sudo apt install python3-venv # Install venv package if not installed earlier

python3 -m venv env
```

3. Activate the virtual env

```
source venv_name/bin/activate
```


4. Install dependencies 

```
pip install -r requirements.txt
```

5. Start the server 

```
uvicorn app:app --reload
```


### Documentation

The documentation is been taken care by the swagger UI that comes in-built with Fastapi. Simply visit the following page to view the documentation

```
HOSTED_SERVER_ADDRESS/docs

for localhost

http://127.0.0.1/docs
```

### Thanks and regards
