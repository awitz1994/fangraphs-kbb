from flask import request, jsonify
from flask.views import MethodView
from .models.pitcher_data import YearQueryType
from .services.pitcher_data import PitcherDataService
from datetime import datetime


class KBBView(MethodView):
    @staticmethod
    def get():
        print(request.args.items)
        year_query = YearQueryType(**{
            k: datetime.strptime(v, "%m-%d-%Y").date() for k, v in request.args.items() if v is not None
        })
        result = PitcherDataService.get_best_kbb_differentials(query=year_query)

        response = jsonify(result)
        status = 200

        return response, status
