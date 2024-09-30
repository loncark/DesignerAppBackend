from config.repositoryConfig.RepositoryConfig import RepositoryConfig

class TestingRepositoryConfig(RepositoryConfig):
    USE_DUMMY_DATABASE_REPO = True
    USE_DUMMY_PRODUCT_RESEARCH_REPO = True
    USE_DUMMY_TEXT_GENERATION_REPO = True
    USE_DUMMY_TRADEMARK_CHECK_REPO = True
    USE_DUMMY_IMAGE_GENERATION_REPO = True
    USE_DUMMY_TREND_RESEARCH_REPO = True

    def __init__(self):
        super().__init__()