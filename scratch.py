from selenium import webdriver
from axe_selenium_python import Axe
import json


def test_google():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    input('press enter...')
    results = axe.run(
        options={
            'runOnly': {
                'type': 'rule',
                'values': ['color-contrast']
            }
        }
    )
    input('press enter...')
    #results = axe.run()
    # Write results to file
    axe.write_results(results, 'a11y.json')
    driver.close()
    # Assert no violations are found
    print(json.dumps(results, indent=4, sort_keys=True))
    assert len(results["violations"]) == 0, axe.report(results["violations"])


if __name__ == "__main__":
    test_google()
