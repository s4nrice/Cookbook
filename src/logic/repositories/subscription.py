from logic.models.postgres import Subscription

from logic.utils.BaseRepository import BaseRepository


class SubscriptionRepository(BaseRepository):
    model = Subscription
