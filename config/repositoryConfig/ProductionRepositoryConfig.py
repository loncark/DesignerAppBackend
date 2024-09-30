from config.repositoryConfig.RepositoryConfig import RepositoryConfig

class ProductionRepositoryConfig(RepositoryConfig):
    USE_DUMMY_DATABASE_REPO = False
    USE_DUMMY_PRODUCT_RESEARCH_REPO = False
    USE_DUMMY_TEXT_GENERATION_REPO = False
    USE_DUMMY_TRADEMARK_CHECK_REPO = False
    USE_DUMMY_IMAGE_GENERATION_REPO = False
    USE_DUMMY_TREND_RESEARCH_REPO = False

    def __init__(self):
        super().__init__()