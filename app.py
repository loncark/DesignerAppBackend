from DesignerApp import DesignerApp
import importlib

def createApp(providerConfigName, repositoryConfigName):

    repositoryConfigClassName = repositoryConfigName + 'RepositoryConfig'
    repositoryConfigModule = importlib.import_module('config.repositoryConfig.' + repositoryConfigClassName)
    repositoryConfigClass = getattr(repositoryConfigModule, repositoryConfigClassName)
    repositoryConfig = repositoryConfigClass()

    providerConfigClassName = providerConfigName + 'ProviderConfig'
    providerConfigModule = importlib.import_module('config.providerConfig.' + providerConfigClassName)
    providerConfigClass = getattr(providerConfigModule, providerConfigClassName)
    providerConfig = providerConfigClass()

    app = DesignerApp(providerConfig, repositoryConfig)

    return app

if __name__ == '__main__':
    app = createApp(providerConfigName = 'Primary', repositoryConfigName='Development')
    app.run()
