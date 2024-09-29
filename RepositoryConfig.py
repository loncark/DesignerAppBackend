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

class DevelopmentConfig(RepositoryConfig):
    USE_DUMMY_DATABASE_REPO = False
    USE_DUMMY_PRODUCT_RESEARCH_REPO = True
    USE_DUMMY_TEXT_GENERATION_REPO = True
    USE_DUMMY_TRADEMARK_CHECK_REPO = False
    USE_DUMMY_IMAGE_GENERATION_REPO = True
    USE_DUMMY_TREND_RESEARCH_REPO = True

    def __init__(self):
        super().__init__()

class TestingConfig(RepositoryConfig):
    USE_DUMMY_DATABASE_REPO = True
    USE_DUMMY_PRODUCT_RESEARCH_REPO = True
    USE_DUMMY_TEXT_GENERATION_REPO = True
    USE_DUMMY_TRADEMARK_CHECK_REPO = True
    USE_DUMMY_IMAGE_GENERATION_REPO = True
    USE_DUMMY_TREND_RESEARCH_REPO = True

    def __init__(self):
        super().__init__()

class ProductionConfig(RepositoryConfig):
    USE_DUMMY_DATABASE_REPO = False
    USE_DUMMY_PRODUCT_RESEARCH_REPO = False
    USE_DUMMY_TEXT_GENERATION_REPO = False
    USE_DUMMY_TRADEMARK_CHECK_REPO = False
    USE_DUMMY_IMAGE_GENERATION_REPO = False
    USE_DUMMY_TREND_RESEARCH_REPO = False

    def __init__(self):
        super().__init__()