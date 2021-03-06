from datetime import datetime

import pytest
import pandas as pd

from iexfinance import get_historical_data
from iexfinance import Stock
from iexfinance.utils.exceptions import IEXSymbolError, IEXEndpointError


class TestBase(object):

    def test_wrong_iex_input_type(self):
        with pytest.raises(ValueError):
            Stock(34)
        with pytest.raises(ValueError):
            Stock("")
        with pytest.raises(ValueError):
            ls = []
            Stock(ls)

    def test_symbol_list_too_long(self):
        with pytest.raises(ValueError):
            x = ["tsla"] * 102
            Stock(x)

    def test_wrong_option_values(self):
        with pytest.raises(ValueError):
            Stock("aapl", last=555)

        with pytest.raises(TypeError):
            Stock("aapl", displayPercent=4)

        with pytest.raises(ValueError):
            Stock("aapl", _range='1yy')

    # def test_invalid_option_values(self):
    #   with pytest.raises(TypeError):
    #       Stock("aapl", displayPercent=4)
    #   with pytest.raises(ValueError):
    #       Stock("aapl", last=68)
    #   with pytest.raises(ValueError):
    #       Stock("aapl", chartRange='6y')
    #   with pytest.raises(ValueError):
    #       Stock("aapl", )


# class ShareIntegrityTester(object):

#   def setup_class(self):
#       self.mshare = mocker.get_mock_share()
#       self.cshare = Share(self.mshare.get_symbol())

#   def test_endpoints(self):
#       mendpoints = list(self.mshare.get_all().keys())
#       cendpoints = list(self.cshare.get_all().keys())
#       mendpoints.sort()
#       cendpoints.sort()
#       self.assertListEqual(mendpoints, cendpoints)


#   def test_datapoints(self):
#       table = self.mshare.get_all()
#       for endpoint in table.keys():
#           mmod = self.mshare.get_select_endpoints(endpoint)
#           cmod = self.cshare.get_select_endpoints(endpoint)
#           assert type(mmod), type(cmod))
#           if type(mmod) is dict:
#               mdatapoints = list(mmod.keys())
#               cdatapoints = list(cmod.keys())
#               mdatapoints.sort()
#               cdatapoints.sort()
#               self.assertListEqual(mdatapoints, cdatapoints)
#           else:
#               print("Skipping endpoint " + endpoint)
#       self.assertListEqual(mdatapoints, cdatapoints)

class TestShare(object):

    def setup_class(self):
        self.cshare = Stock("aapl")

    def test_get_all_format(self):
        data = self.cshare.get_all()
        assert isinstance(data, dict,)

    def test_get_chart_format(self):
        data = self.cshare.get_chart()
        assert isinstance(data, list)

    def test_get_book_format(self):
        data = self.cshare.get_book()
        assert isinstance(data, dict)

    def test_get_open_close_format(self):
        data = self.cshare.get_open_close()
        assert isinstance(data, dict)

    def test_get_previous_format(self):
        data = self.cshare.get_previous()
        assert isinstance(data, dict)

    def test_get_company_format(self):
        data = self.cshare.get_company()
        assert isinstance(data, dict)

    def test_get_key_stats_format(self):
        data = self.cshare.get_key_stats()
        assert isinstance(data, dict)

    def test_get_relevant_format(self):
        data = self.cshare.get_relevant()
        assert isinstance(data, dict)

    def test_get_news_format(self):
        data = self.cshare.get_news()
        assert isinstance(data, list)

    def test_get_financials_format(self):
        data = self.cshare.get_financials()
        assert isinstance(data, dict)

    def test_get_earnings_format(self):
        data = self.cshare.get_earnings()
        assert isinstance(data, dict)

    def test_get_logo_format(self):
        data = self.cshare.get_logo()
        assert isinstance(data, dict)

    def test_get_price_format(self):
        data = self.cshare.get_price()
        assert isinstance(data, float)

    def test_get_delayed_quote_format(self):
        data = self.cshare.get_delayed_quote()
        assert isinstance(data, dict)

    def test_get_effective_spread_format(self):
        data = self.cshare.get_effective_spread()
        assert isinstance(data, list)

    def test_get_volume_by_venue_format(self):
        data = self.cshare.get_volume_by_venue()
        assert isinstance(data, list)

    def test_ohlc(self):
        data = self.cshare.get_ohlc()
        assert isinstance(data, dict)

    def test_time_series(self):
        data = self.cshare.get_time_series()
        data2 = self.cshare.get_chart()
        assert data == data2

    def test_nondefault_params_1(self):
        aapl = Stock("AAPL", _range='5y')
        aapl2 = Stock("AAPL")
        assert len(aapl.get_chart()) > len(aapl2.get_chart())

    def test_nondefault_params_2(self):
        aapl = Stock("AAPL", last=37)
        assert len(aapl.get_news()) == 37


class TestBatch(object):

    def setup_class(self):
        self.cbatch = Stock(["aapl", "tsla"])

    def test_invalid_symbol_or_symbols(self):
        with pytest.raises(IEXSymbolError):
            Stock(["TSLA", "AAAPLPL", "fwoeiwf"])

    def test_get_all_format(self):
        data = self.cbatch.get_all()
        assert isinstance(data, dict)

    def test_get_chart_format(self):
        data = self.cbatch.get_chart()
        assert isinstance(data, dict)

    def test_get_book_format(self):
        data = self.cbatch.get_book()
        assert isinstance(data, dict)

    def test_get_open_close_format(self):
        data = self.cbatch.get_open_close()
        assert isinstance(data, dict)

    def test_get_previous_format(self):
        data = self.cbatch.get_previous()
        assert isinstance(data, dict)

    def test_get_company_format(self):
        data = self.cbatch.get_company()
        assert isinstance(data, dict)

    def test_get_key_stats_format(self):
        data = self.cbatch.get_key_stats()
        assert isinstance(data, dict)

    def test_get_relevant_format(self):
        data = self.cbatch.get_relevant()
        assert isinstance(data, dict)

    def test_get_news_format(self):
        data = self.cbatch.get_news()
        assert isinstance(data, dict)

    def test_get_financials_format(self):
        data = self.cbatch.get_financials()
        assert isinstance(data, dict)

    def test_get_earnings_format(self):
        data = self.cbatch.get_earnings()
        assert isinstance(data, dict)

    def test_get_logo_format(self):
        data = self.cbatch.get_logo()
        assert isinstance(data, dict)

    def test_get_price_format(self):
        data = self.cbatch.get_price()
        assert isinstance(data, dict)

    def test_get_delayed_quote_format(self):
        data = self.cbatch.get_delayed_quote()
        assert isinstance(data, dict)

    def test_get_effective_spread_format(self):
        data = self.cbatch.get_effective_spread()
        assert isinstance(data, dict)

    def test_get_volume_by_venue_format(self):
        data = self.cbatch.get_volume_by_venue()
        assert isinstance(data, dict)

    def test_get_select_ep_bad_params(self):
        with pytest.raises(ValueError):
            self.cbatch.get_select_endpoints()

        with pytest.raises(IEXEndpointError):
            self.cbatch.get_select_endpoints("BADENDPOINT")

    def test_ohlc(self):
        data = self.cbatch.get_ohlc()
        assert isinstance(data, dict)

    def test_time_series(self):
        data = self.cbatch.get_time_series()
        data2 = self.cbatch.get_chart()
        assert data == data2

    def test_nondefault_params_1(self):
        data = Stock(["AAPL", "TSLA"], _range='5y')
        data2 = Stock(["AAPL", "TSLA"])
        assert len(data.get_chart()["AAPL"]) > len(data2.get_chart()["AAPL"])
        assert len(data.get_chart()["TSLA"]) > len(data2.get_chart()["TSLA"])

    def test_nondefault_params_2(self):
        data = Stock(["AAPL", "TSLA"], last=37)
        assert len(data.get_news()["AAPL"]) == 37
        assert len(data.get_news()["TSLA"]) == 37


class TestHistorical(object):

    def setup_class(self):
        self.good_start = datetime(2017, 2, 9)
        self.good_end = datetime(2017, 5, 24)

    def test_single_historical_json(self):

        f = get_historical_data("AAPL", self.good_start, self.good_end)
        assert isinstance(f, dict)
        assert len(f["AAPL"]) == 73

        expected1 = f["AAPL"]["2017-02-09"]
        assert expected1["close"] == 132.42
        assert expected1["high"] == 132.445

        expected2 = f["AAPL"]["2017-05-24"]
        assert expected2["close"] == 153.34
        assert expected2["high"] == 154.17

    def test_single_historical_pandas(self):

        f = get_historical_data("AAPL", self.good_start, self.good_end,
                                output_format="pandas")

        assert isinstance(f, pd.DataFrame)
        assert len(f) == 73

        expected1 = f.loc["2017-02-09"]
        assert expected1["close"] == 132.42
        assert expected1["high"] == 132.445

        expected2 = f.loc["2017-05-24"]
        assert expected2["close"] == 153.34
        assert expected2["high"] == 154.17

    def test_batch_historical_json(self):

        f = get_historical_data(["AAPL", "TSLA"], self.good_start,
                                self.good_end, output_format="json")

        assert isinstance(f, dict)
        assert len(f) == 2
        assert sorted(list(f)) == ["AAPL", "TSLA"]

        a = f["AAPL"]
        t = f["TSLA"]

        assert len(a) == 73
        assert len(t) == 73

        expected1 = a["2017-02-09"]
        assert expected1["close"] == 132.42
        assert expected1["high"] == 132.445

        expected2 = a["2017-05-24"]
        assert expected2["close"] == 153.34
        assert expected2["high"] == 154.17

        expected1 = t["2017-02-09"]
        assert expected1["close"] == 269.20
        assert expected1["high"] == 271.18

        expected2 = t["2017-05-24"]
        assert expected2["close"] == 310.22
        assert expected2["high"] == 311.0

    def test_batch_historical_pandas(self):

        f = get_historical_data(["AAPL", "TSLA"], self.good_start,
                                self.good_end, output_format="pandas")

        assert isinstance(f, dict)
        assert len(f) == 2
        assert sorted(list(f)) == ["AAPL", "TSLA"]

        a = f["AAPL"]
        t = f["TSLA"]

        assert len(a) == 73
        assert len(t) == 73

        expected1 = a.loc["2017-02-09"]
        assert expected1["close"] == 132.42
        assert expected1["high"] == 132.445

        expected2 = a.loc["2017-05-24"]
        assert expected2["close"] == 153.34
        assert expected2["high"] == 154.17

        expected1 = t.loc["2017-02-09"]
        assert expected1["close"] == 269.20
        assert expected1["high"] == 271.18

        expected2 = t.loc["2017-05-24"]
        assert expected2["close"] == 310.22
        assert expected2["high"] == 311.0

    def test_invalid_dates(self):
        start = datetime(2010, 5, 9)
        end = datetime(2017, 5, 9)
        with pytest.raises(ValueError):
            get_historical_data("AAPL", start, end)

    def test_invalid_dates_batch(self):
        start = datetime(2010, 5, 9)
        end = datetime(2017, 5, 9)
        with pytest.raises(ValueError):
            get_historical_data(["AAPL", "TSLA"], start, end)

    def test_invalid_symbol_single(self):
        start = datetime(2017, 2, 9)
        end = datetime(2017, 5, 24)
        with pytest.raises(IEXSymbolError):
            get_historical_data("BADSYMBOL", start, end)

    def test_invalid_symbol_batch(self):
        start = datetime(2017, 2, 9)
        end = datetime(2017, 5, 24)
        with pytest.raises(IEXSymbolError):
            get_historical_data(["BADSYMBOL", "TSLA"], start, end)
