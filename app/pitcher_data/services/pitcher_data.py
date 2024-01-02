from app.pitcher_data.models.pitcher_data import YearQueryType

class PitcherDataService:

    @staticmethod
    def get_best_kbb_differentials(query: YearQueryType):
        res = [{
            "data": []
        }]

        return res
