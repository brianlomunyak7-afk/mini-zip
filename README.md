

![CI](https://github.com/<your-username>/mini-zip/actions/workflows/ci.yml/badge.svg)
## Run with Docker

```bash
docker build -t mini-zip .
docker run --rm --user "$(id -u):$(id -g)" -v "$(pwd)":/data -w /data mini-zip compress notes.txt
```
