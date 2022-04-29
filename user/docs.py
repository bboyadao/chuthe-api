from drf_spectacular.utils import extend_schema, OpenApiExample
from django.utils.translation import ugettext_lazy as _


TAG = "User View"
user_docs = {
    # "destroy": extend_schema(
    #     tags=[VACCINE],
    #     operation_id=_("destroy Animal VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    # ),
    # "update": extend_schema(
    #     tags=[VACCINE],
    #     operation_id=_("update Animal VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    #
    # ),
    # "partial_update": extend_schema(
    #     tags=[VACCINE],
    #     operation_id=_("partial_update partial VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    #
    # ),
    # "list": extend_schema(
    #     tags=[VACCINE],
    #     operation_id=_("list Animal VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    # ),
    # "retrieve": extend_schema(
    #     tags=[VACCINE],
    #     operation_id=_("retrieve Animal VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    # ),
    "create": extend_schema(
        tags=[TAG],
        operation_id=_("create User".title()),
        description="User Dess"
    ),
    # "chart": extend_schema(
    #     tags=[CHART],
    #     operation_id=_("Animal Vaccine Chart".title()),
    #     description="Animal Vaccine Chart",
    #     responses={200: [{"return_by": "date", "avg": 100}],
    #                400: OpenApiTypes.OBJECT},
    #     examples=[
    #         OpenApiExample(
    #             "OK",
    #             value=[{"day": "2021-07-16",
    #                     "avg": 3.0}],
    #             response_only=True,
    #             status_codes=["200"],
    #         ),
    #         OpenApiExample(
    #             "ERROR",
    #             response_only=True,
    #             status_codes=["400"],
    #             value={
    #                 "error": {
    #                     "start": "timestamp",
    #                     "end": "timestamp",
    #                     "return_by": [
    #                         "day",
    #                         "month",
    #                         "year"
    #                     ]
    #                 },
    #                 "exp": "?start=2222222&end=34333&return_by=day"
    #             }
    #         )
    #     ],
    # ),
}

