from pydantic import BaseModel, Field


class Job(BaseModel):
    """Initial normalized representation of a job listing."""

    title: str = Field(min_length=1, max_length=200)
    company: str = Field(min_length=1, max_length=200)
    location: str | None = Field(default=None, max_length=200)
    description: str | None = None
    employment_type: str | None = Field(default=None, max_length=100)
    skills: list[str] = Field(default_factory=list)
