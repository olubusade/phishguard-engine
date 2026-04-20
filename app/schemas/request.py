from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    """
    Input schema for URL prediction.
    Keeps validation strict but simple.
    """

    url: HttpUrl