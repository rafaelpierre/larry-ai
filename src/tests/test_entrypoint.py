from unittest import mock

@mock.patch("larry.entrypoint.main", mock.MagicMock())
def test_entrypoint():

    from larry.entrypoint import main

    main()
    main.assert_called_once()