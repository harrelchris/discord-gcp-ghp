# Discord GCP GHP

Discord app hosted on Google Cloud and GitHub Pages

## Requires

- Python 3+
- GCloud CLI

## Develop

### Set up dev environment

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
```

### Serve locally

```shell
(cd backend && functions-framework --target=discord --port=80 --debug)
```

## Deploy 

### Deploy to GCP

```shell
gcloud functions deploy discord \
--source ./backend \
--runtime python312 \
--allow-unauthenticated \
--trigger-http
```

### Update URL in `index.html`

Copy the URL displayed in the terminal and paste into `frontend/index.html`

```javascript
// SET GCP FUNCTION URL
const url = "https://YOUR-PROJECT.cloudfunctions.net/discord"
```
