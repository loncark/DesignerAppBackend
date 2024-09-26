from abc import ABC, abstractmethod

class Config(ABC):
    USE_DUMMY_FIREBASE_REPO = None
    USE_DUMMY_ETSY_REPO = None
    USE_DUMMY_GEMINI_REPO = None
    USE_DUMMY_TRADEMARK_REPO = None
    USE_DUMMY_SD_REPO = None
    USE_DUMMY_GOOGLETRENDS_REPO = None

    @abstractmethod
    def __init__(self):
        pass

class DevelopmentConfig(Config):
    USE_DUMMY_FIREBASE_REPO = True
    USE_DUMMY_ETSY_REPO = False
    USE_DUMMY_GEMINI_REPO = True
    USE_DUMMY_TRADEMARK_REPO = True
    USE_DUMMY_SD_REPO = False
    USE_DUMMY_GOOGLETRENDS_REPO = True

    def __init__(self):
        super().__init__()

class TestingConfig(Config):
    USE_DUMMY_FIREBASE_REPO = True
    USE_DUMMY_ETSY_REPO = True
    USE_DUMMY_GEMINI_REPO = True
    USE_DUMMY_TRADEMARK_REPO = True
    USE_DUMMY_SD_REPO = True
    USE_DUMMY_GOOGLETRENDS_REPO = True

    def __init__(self):
        super().__init__()

class ProductionConfig(Config):
    USE_DUMMY_FIREBASE_REPO = False
    USE_DUMMY_ETSY_REPO = False
    USE_DUMMY_GEMINI_REPO = False
    USE_DUMMY_TRADEMARK_REPO = False
    USE_DUMMY_SD_REPO = False
    USE_DUMMY_GOOGLETRENDS_REPO = False

    def __init__(self):
        super().__init__()