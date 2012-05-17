try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="mdemos.metrics",
    version="0.1.2",
    release="1",
    url="http://moksha.fedorahosted.org",
    description="Moksha Metrics App",
    long_description="",
    author="Luke Macken",
    author_email="lmacken@redhat.com",
    license="ASL 2.0",
    packages=['mdemos', 'mdemos.metrics'],
    namespace_packages=['mdemos'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "moksha>=0.7",
    ],
    entry_points={
        'moksha.stream': (
            'moksha_metrics = mdemos.metrics.streams:MokshaMetricsProducer',
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
            'moksha_socket = moksha.api.widgets:get_moksha_socket',
        ),
    }
)
