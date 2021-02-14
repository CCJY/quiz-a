import mock
import unittest
import json
from unittest.mock import patch
from quiz.offers import getOffers, exportOffersToCsv
from quiz.export_json import jsonToCsv
from requests import HTTPError, RequestException

api_endpoint = ''
auth_token = ''


class TestOffers(unittest.TestCase):
    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    # if status code (200), export json data into csv
    def test_offers_429(self):
        with patch("quiz.offers.requests.get") as mock_get:
            with open('data.json', encoding="utf-8-sig") as json_file:
                json_data = json.load(json_file)
            mock_resp_429 = self._mock_response(
                status=429, raise_for_status=RequestException())
            mock_resp_200 = self._mock_response(
                status=200, json_data=json_data)
            mock_get.side_effect = [mock_resp_429, mock_resp_200]
            response = getOffers(api_endpoint=api_endpoint,
                                 auth_token=auth_token, sleep=60)
        print(response)
        exported = exportOffersToCsv(response)
        self.assertIsNotNone(response)
        self.assertEqual(exported, True)

    def test_offers_500(self):
        with patch("quiz.offers.requests.get") as mock_get:
            mock_resp_500 = self._mock_response(
                status=500, raise_for_status=RequestException("I'm dead. GoodBye"))
            mock_get.side_effect = [mock_resp_500]
            with self.assertRaises(SystemExit) as cm:
                getOffers(api_endpoint=api_endpoint,
                          auth_token=auth_token)
            exception = cm.exception
            print(exception)


if __name__ == "__main__":
    unittest.main()
