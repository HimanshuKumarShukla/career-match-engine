from pydantic import BaseModel, Field


class UserPreference(BaseModel):
    """Initial user criteria for future job matching."""

    target_roles: list[str] = Field(default_factory=list)
    preferred_locations: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    remote_only: bool = False
    minimum_salary: int | None = Field(default=None, ge=0)
