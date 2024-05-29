from fastapi_filter.contrib.sqlalchemy import Filter

from logic.models.postgres import Subscription
from logic.utils.BaseSchemas import BaseSchema, BaseModelWithValidation


class SubscriptionCreate(BaseSchema):
    publisher_id: str
    subscriber_id: str


class SubscriptionUpdate(BaseModelWithValidation):
    id: str
    publisher_id: str | None = None
    subscriber_id: str | None = None


class SubscriptionFilter(Filter):
    publisher_id: str | None = None
    subscriber_id: str | None = None

    class Constants(Filter.Constants):
        model = Subscription
