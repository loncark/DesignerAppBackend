from abc import ABC, abstractmethod

class ProviderConfig(ABC):
    DATABASE_PROVIDER = None
    TEXT_GENERATION_PROVIDER = None
    IMAGE_GENERATION_PROVIDER = None
    PRODUCT_RESEARCH_PROVIDER = None
    TREND_RESEARCH_PROVIDER = None
    TRADEMARK_CHECK_PROVIDER = None

    @abstractmethod
    def __init__(self):
        pass

class PrimaryProviderConfig(ProviderConfig):
    DATABASE_PROVIDER = 'Firebase'
    TEXT_GENERATION_PROVIDER = 'Gemini'
    IMAGE_GENERATION_PROVIDER = 'StableDiffusion'
    PRODUCT_RESEARCH_PROVIDER = 'Etsy'
    TREND_RESEARCH_PROVIDER = 'GoogleTrends'
    TRADEMARK_CHECK_PROVIDER = 'Trademark'

    def __init__(self):
        super().__init__()