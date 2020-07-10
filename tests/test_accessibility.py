import logging
from selenium import webdriver
from axe_selenium_python import Axe
import json


def test_contrast(driver: webdriver.Chrome):
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run(
        options={
            'runOnly': {
                'type': 'rule',
                'values': ['color-contrast']
            }
        }
    )
    # Write results to file
    axe.write_results(results, 'a11y.json')
    # Assert no violations are found
    logging.info('results:\n%s', json.dumps(results, indent=4, sort_keys=True))
    assert len(results["violations"]) == 0, axe.report(results["violations"])
