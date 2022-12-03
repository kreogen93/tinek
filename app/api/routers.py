from fastapi import APIRouter


from app.services import tournament

router = APIRouter(
    prefix="/api",
)


@router.get("/tournaments/{t_id}")
async def get_tournament(t_id: str):
    return tournament.get_tournament(t_id)


@router.post("/tournaments")
def generate_tournament():
    return tournament.gen_tournament()

@router.put("/tournaments/{id}/matches/{match_id}")
def put_tournament_info(id: int, match_id: int, score: Score):
    return tournament.put_tournament()

