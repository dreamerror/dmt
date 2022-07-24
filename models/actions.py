from datetime import timedelta

from pydantic import BaseModel

from .events import Event


class Action(BaseModel):
    """
    Модель варианта ответа в событии
    """
    description: str  # краткое описание варианта
    message: str   # сообщение, выводящееся при выборе варианта
    time_cost: timedelta = timedelta(0)
    triggered_event: Event | None = None

