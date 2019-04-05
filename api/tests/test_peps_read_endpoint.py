import pytest
from api.tests.apiclient import ApiClient


@pytest.fixture
def given_a_peps_read_endpoint():
    url = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/peps"
    headers = {'content-type': 'application/json'}
    session = ApiClient(url)
    yield url, headers, session


def test_when_peps_data_added(given_a_peps_read_endpoint):
    url, headers, session = given_a_peps_read_endpoint

    r = session.get(headers=headers)

    assert r.status_code == 200
    assert r.json()[3]['country'] == 'UK'
    assert len(r.json()) == 5


