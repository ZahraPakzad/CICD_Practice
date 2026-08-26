# FastAPI CI/CD Practice — Level 1

A minimal FastAPI app with tests and a GitHub Actions CI workflow.

## What's here
- `app/main.py` — three endpoints: `/`, `/health`, `/add/{a}/{b}`
- `tests/test_main.py` — pytest tests using FastAPI's `TestClient`
- `.github/workflows/ci.yml` — runs on every push/PR to `main`: checkout → install → test

## Run it locally
```bash
pip install -r requirements-dev.txt
python -m pytest -v
uvicorn app.main:app --reload   # then visit http://127.0.0.1:8000/docs
```

## Push it to GitHub
```bash
git init
git add .
git commit -m "Level 1: basic CI pipeline"
git branch -M main
git remote add origin <your-empty-github-repo-url>
git push -u origin main
```

Then go to the "Actions" tab on GitHub — you should see the workflow run and pass.

## Try breaking it on purpose
Edit `tests/test_main.py` so `test_add` expects the wrong result (e.g. `{"result": 999}`),
commit, and push. Watch the Actions tab turn red. Then fix it and push again to watch it
go green. This is the whole feedback loop CI exists to give you — fast, automatic,
visible on every push.
