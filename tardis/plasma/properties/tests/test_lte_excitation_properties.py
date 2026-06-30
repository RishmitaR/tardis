import pandas.testing as pdt


def test_level_boltzmann_factor_lte(level_boltzmann_factor_lte, regression_data):
    expected_level_boltzmann_factor = regression_data.sync_dataframe(
        level_boltzmann_factor_lte, key="general_level_boltzmann_factor"
    )
    pdt.assert_frame_equal(
        level_boltzmann_factor_lte, expected_level_boltzmann_factor
    )