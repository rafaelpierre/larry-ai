from unittest import mock
from larry.entrypoint import run


@mock.patch("larry.entrypoint.main", mock.MagicMock())
def test_entrypoint():

    from larry.entrypoint import main, run
    main()
    main.assert_called_once()

def test_run():

    run(command = ["bash", "-c", "echo", "12345678910", "&&", "sleep 3", "&&", "echo 12345678910"])
    pass
