from config.providerConfig.ProviderConfig import ProviderConfig

class PrimaryProviderConfig(ProviderConfig):
    DATABASE_PROVIDER = 'Firebase'
    TEXT_GENERATION_PROVIDER = 'Gemini'
    IMAGE_GENERATION_PROVIDER = 'StableDiffusion'
    PRODUCT_RESEARCH_PROVIDER = 'Etsy'
    TREND_RESEARCH_PROVIDER = 'GoogleTrends'
    TRADEMARK_CHECK_PROVIDER = 'USTrademark'

    def __init__(self):
        super().__init__()