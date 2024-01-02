from pydantic import BaseModel, condate
from datetime import datetime


class YearQueryType(BaseModel):
    start_year: condate()
    end_year: condate(le=datetime.today().date())

    def as_dict(self):
        return {
            "start_year": self.start_year,
            "end_year": self.end_year
        }
