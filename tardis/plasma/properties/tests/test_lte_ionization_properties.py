import pandas.testing as pdt


def test_phi_saha_lte(phi, regression_data):
    expected_phi = regression_data.sync_dataframe(phi, key="phi")
    pdt.assert_frame_equal(phi, expected_phi)
