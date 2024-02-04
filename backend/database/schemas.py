from pydantic import BaseModel, HttpUrl


class LinkBase(BaseModel):
    original_url: HttpUrl
    name: str


class LinkSchema(LinkBase):
    id: int
    fake_url: HttpUrl
    slug: str


class LinkCreateSchema(LinkBase):
    class Config:
        orm_mode = True
