from drf_spectacular.utils import extend_schema, OpenApiExample
from django.utils.translation import gettext as _

TAG = "Apps"
app_docs = {
    # "destroy": extend_schema(
    #     tags=[TAG],
    #     operation_id=_("destroy Animal VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    # ),
    # "update": extend_schema(
    #     tags=[TAG],
    #     operation_id=_("update Animal VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    #
    # ),
    # "partial_update": extend_schema(
    #     tags=[TAG],
    #     operation_id=_("partial_update partial VACCINE attrs".title()),
    #     description="Animal Vaccine attrs"
    # )
}
from drf_spectacular.openapi import AutoSchema