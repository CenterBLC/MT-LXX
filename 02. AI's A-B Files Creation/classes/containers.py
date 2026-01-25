"""Containers module."""

import importlib
from typing import TYPE_CHECKING
from dependency_injector import containers, providers
from . import services
# from . import Tester13

from . import Tester13
importlib.reload(Tester13)

# if TYPE_CHECKING:
#     from . import Kapka
#     # from . import IDataProcessor, DataProcessor

class Container(containers.DeclarativeContainer):

    # config = providers.Configuration(ini_files=["config.ini"])

    # logging = providers.Resource(
    #     # logging.config.fileConfig,
    #     # fname="logging.ini",
    # )

    # Gateways. Gateways handle communication with the outside world
    # Gateways are adapters between your domain and the outside world. They:
    # Talk to databases, APIs, message brokers, files, etc.
    # Implement interfaces defined by the domain
    # Translate between domain objects and external formats
    # Characteristics:
    # Infrastructure-specific
    # Swappable implementations
    # Should NOT contain business rules
    # Gateways never depend on Services



    # Services. Services implement business logic. They:
    # Coordinate domain objects
    # Enforce business rules
    # Are independent of infrastructure
    # Depend only on interfaces, not implementations
    # Services depend on Gateways

    # fileWriter = providers.Singleton(

    # )

    # dataProcessorFactory = providers.Singleton(
    #     IDataProcessor,
    #     DataProcessor()
    # )

    

    mtlxxServiceFactory = providers.Singleton(
        services.MTLXXService
    )

    kapkaFactory = providers.Singleton(
        Tester13.Kapka
    )

    # dataProcessorFactory = providers.Singleton(
    #     DataProcessor.DataProcessor
    # )

    tester13Factory = providers.Factory(
        Tester13.Tester13
    )