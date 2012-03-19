from paver.easy import *
from paver.setuputils import setup, find_package_data, find_packages
from paver.setuputils import install_distutils_tasks
from moksha.lib.paver_tasks import *

install_distutils_tasks()

options(
    setup=Bunch(
        name="mdemos.metrics",
        version="0.1",
        release="1",
        url="http://moksha.fedorahosted.org",
        description="Moksha Metrics App",
        long_description="",
        author="Luke Macken",
        author_email="lmacken@redhat.com",
        license="ASL 2.0",
        rpm_name='moksha-metrics',
        packages=find_packages(),
        package_data=find_package_data(),
        namespace_packages=['mdemos'],
        install_requires=[
            "moksha>=0.7.0a",
        ],
        entry_points={
            'moksha.stream': (
                'moksha_metrics = mdemos.metrics.streams:MokshaMetricsProducer',
            ),
            'moksha.consumer': (
                'moksha_message_metrics = mdemos.metrics.consumers:MokshaMessageMetricsConsumer',
            ),
            'moksha.widget': (
                ### Commented out from the tw1/tw2 config conversion
                #'MokshaTW2CPUUsageWidget = mdemos.metrics.widgets:MokshaTW2CPUUsageWidget',
                'MokshaMemoryUsageWidget = mdemos.metrics.widgets:MokshaMemoryUsageWidget',
                'MokshaCPUUsageWidget = mdemos.metrics.widgets:MokshaCPUUsageWidget',
                'MokshaMessageMetricsWidget = mdemos.metrics.widgets:MokshaMessageMetricsWidget',
            ),
            'moksha.global': (
                'moksha_socket = moksha.api.widgets:moksha_socket',
            ),
        }
    ),
)
