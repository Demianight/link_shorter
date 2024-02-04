from fastapi import FastAPI


app = FastAPI()


links = [
    {
        "id": 1,
        "original_url": "http://example.com",
        "fake_url": "http://example.com",
        "slug": "string",
        "name": "string"
    },
    {
        "id": 2,
        "original_url": "http://example.com",
        "fake_url": "http://example.com",
        "slug": "string",
        "name": "string"
    }
]


@app.get('/links')
def links_list() -> list[dict]:
    return links
