from app.schemas.schema import Match, Score, Stage, Team, Tournament

def get_tournament(t_id: str):
    return {"id": t_id}

def gen_tournament():
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

def put_tournament(id: int, match_id: int, score: Score):
    return {
        "is_finished" : True
    }