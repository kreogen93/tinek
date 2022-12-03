from fastapi import APIRouter

from app.schemas.schema import Match, Score, Stage, Team, Tournament

router = APIRouter(
    prefix="/api",
)



@router.get("/tournaments/{t_id}")
async def get_tournament(t_id: str):
    return {"t_id": t_id}





@router.post("/tournaments")
def generate_tournament():
    return Tournament(
        id=1,
        name="name",
        status="ACTIVE",
        stages=[
            Stage(
                level=1,
                matches=[
                    Match(
                        id=1,
                        team1=Team(id=1, name="name1"),
                        team2=Team(id=2, name="name2"),
                        score1=1,
                        score2=10,
                    )
                ],
            )
        ],
    )

@router.put("/tournaments/{id}/matches/{match_id}")
def put_tournament_info(id, match_id, score: Score):
    print(score)
    return {
        "is_finished" : True
    }

