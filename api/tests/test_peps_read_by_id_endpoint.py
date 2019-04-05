import pytest
from api.tests.apiclient import ApiClient


@pytest.fixture
def given_a_peps_read_by_id_endpoint():
    url = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/peps"
    headers = {'content-type': 'application/json'}
    session = ApiClient(url)
    yield url, headers, session


def test_when_peps_data_added(given_a_peps_read_by_id_endpoint):
    url, headers, session = given_a_peps_read_by_id_endpoint

    r = session.get(url='/5ca77bbf17b9b5041b7737d5', headers=headers)

    assert r.status_code == 200
    assert len(r.json()) == 6
    assert r.json()['country'] == 'UK'


