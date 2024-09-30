from abc import ABC, abstractmethod

class RepositoryConfig(ABC):
    USE_DUMMY_DATABASE_REPO = None
    USE_DUMMY_PRODUCT_RESEARCH_REPO = None
    USE_DUMMY_TEXT_GENERATION_REPO = None
    USE_DUMMY_TRADEMARK_CHECK_REPO = None
    USE_DUMMY_IMAGE_GENERATION_REPO = None
    USE_DUMMY_TREND_RESEARCH_REPO = None

    @abstractmethod
    def __init__(self):
        pass
