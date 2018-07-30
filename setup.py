#!/usr/bin/env python
from setuptools import setup

with open('VERSION.txt') as f:
    version = f.read().strip().split('\n')[0]

setup(
    name='umccrise',
    version=version,
    author='Vlad Saveliev',
    description='UMCCRisation of bcbio-nextgen analysis results',
    keywords='bioinformatics',
    license='GPLv3',
    packages=[
        'umccrise',
    ],
    scripts=[
        'vendor/vcfToBedpe',
        'scripts/umccrise',
        'scripts/pcgr',
    ],
    include_package_data=True,
    
    # For MultiQC_umccr
    entry_points = {
        'multiqc.templates.v1': [
            'umccr = umccrise.multiqc.templates.umccr',
        ],
        'multiqc.hooks.v1': [
            'config_loaded            = umccrise.multiqc.multiqc_umccr:config_loaded',
            'execution_start          = umccrise.multiqc.multiqc_umccr:execution_start',
            'after_modules            = umccrise.multiqc.multiqc_umccr:before_set_general_stats_html',
            'before_report_generation = umccrise.multiqc.multiqc_umccr:after_set_general_stats_html',
        ]
    },
)
