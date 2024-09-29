from DesignerApp import DesignerApp
from RepositoryConfig import *
from ProviderConfig import *

def createApp(providerConfigName, repositoryConfigName):
    if repositoryConfigName == 'prod':
        repositoryConfig = ProductionConfig()
    elif repositoryConfigName == 'test':
        repositoryConfig = TestingConfig()
    else:
        repositoryConfig = DevelopmentConfig()

    if providerConfigName == 'Primary':
        providerConfig = PrimaryProviderConfig()

    app = DesignerApp(providerConfig, repositoryConfig)

    return app

if __name__ == '__main__':
    app = createApp(providerConfigName = 'Primary', repositoryConfigName='dev')
    app.run()
