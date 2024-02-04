import os
import uuid

from sqlalchemy.orm import Session

from . import models, schemas


class Link:
    host = os.getenv('HOST', 'http://127.0.0.1:8000/%s')

    @classmethod
    def get(cls, db: Session, link_id: int):
        return db.query(models.Link).filter(models.Link.id == link_id).first()

    @classmethod
    def get_by_slug(cls, db: Session, slug: str):
        return db.query(
            models.Link
        ).filter(
            models.Link.slug == slug
        ).first()

    @classmethod
    def all(cls, db: Session):
        return db.query(models.Link).order_by(-models.Link.id).all()

    @classmethod
    def create(cls, db: Session, link: schemas.LinkCreateSchema):
        slug = str(uuid.uuid4())
        fake_url = cls.host % slug

        db_link = models.Link(
            original_url=str(link.original_url),
            fake_url=fake_url,
            name=link.name,
            slug=slug
        )

        db.add(db_link)
        db.commit()
        db.refresh(db_link)
        return db_link
