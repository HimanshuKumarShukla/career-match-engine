from fastapi import FastAPI


app = FastAPI(
    title="Career Match Engine",
    description="Early FastAPI foundation. In Active Development.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return the service's basic readiness state."""
    return {"status": "ok", "service": "career-match-engine"}
