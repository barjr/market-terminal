from fastapi import FastAPI

app = FastAPI(title='Market Terminal')


@app.get('/health')
def health():
    return {"status": 'ok'}
