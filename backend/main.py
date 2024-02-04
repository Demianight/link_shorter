from typing import Sequence

from database import SessionLocal, engine, models
from database.crud import Link
from database.schemas import LinkCreateSchema, LinkSchema
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/links')
def links_list(db: Session = Depends(get_db)) -> Sequence[LinkSchema]:
    return Link.all(db)


@app.post('/links')
def links_create(link: LinkCreateSchema, db: Session = Depends(get_db)):
    link = Link.create(db, link)
    return link


@app.get('/links/{slug}', response_class=RedirectResponse)
def redirect_to_origin(slug: str, db: Session = Depends(get_db)):
    link = Link.get_by_slug(db, slug)
    return link.original_url
