from abc import ABC, abstractmethod
from typing import Any
import aiohttp


class BaseCollector(ABC):
    """Base class for all yield data collectors."""
    
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
    
    @abstractmethod
    async def collect(self) -> list[dict[str, Any]]:
        """Collect yield data from the source."""
        pass
    
    @property
    @abstractmethod
    def source_name(self) -> str:
        """Return the name of the data source."""
        pass

