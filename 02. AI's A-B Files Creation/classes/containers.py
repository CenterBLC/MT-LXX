"""Containers module."""

from dependency_injector import containers, providers
import classes.services as services
import classes.Tester13 as Tester13
import classes.DataProcessor as DataProcessor

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

    IDataProcessorFactory = providers.Dependency(instance_of=DataProcessor.IDataProcessor)
    DataProcessorFactory = providers.Singleton(DataProcessor.DataProcessor)
    IDataProcessorFactory.override(DataProcessorFactory)

    MTLXXServiceFactory = providers.Singleton(
        services.MTLXXService
    )

    # A Singleton lazily creates the object once and then always returns the same instance on every call.
    KapkaFactory = providers.Singleton(
        Tester13.Kapka
    )

    # A Factory lazily creates a new instance of the class each time the factory is called
    Tester13Factory = providers.Factory(
        Tester13.Tester13
    )