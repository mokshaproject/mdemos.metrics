try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="mdemos.metrics",
    version="1.0.0",
    url="http://moksha.fedorahosted.org",
    description="Moksha Metrics App",
    long_description="",
    author="Luke Macken",
    author_email="lmacken@redhat.com",
    license="ASL 2.0",
    packages=[
        'mdemos',
        'mdemos.metrics',
        'mdemos.metrics.consumers',
        'mdemos.metrics.producers',
        'mdemos.metrics.widgets',
        'mdemos.metrics.widgets.templates',
    ],
    namespace_packages=['mdemos'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "moksha.hub",
        "moksha.wsgi",
    ],
    entry_points={
        'moksha.producer': (
            'moksha_metrics = mdemos.metrics.producers:MokshaMetricsProducer',
        ),
        'moksha.consumer': (
            'moksha_message_metrics = mdemos.metrics.consumers:MokshaMessageMetricsConsumer',
        ),
        'moksha.widget': (
            'MokshaMemoryUsageWidget = mdemos.metrics.widgets:MokshaMemoryUsageWidget',
            'MokshaCPUUsageWidget = mdemos.metrics.widgets:MokshaCPUUsageWidget',
            'MokshaMessageMetricsWidget = mdemos.metrics.widgets:MokshaMessageMetricsWidget',
        ),
        'moksha.global': (
            'moksha_socket = moksha.wsgi.widgets.api:get_moksha_socket',
        ),
    }
)
