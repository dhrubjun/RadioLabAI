from unittest.mock import MagicMock, patch

from radiolab_ai.app.main import main


@patch("radiolab_ai.app.main.create_main_window")
def test_main_starts_gui(mock_create_main_window):
    mock_window = MagicMock()
    mock_create_main_window.return_value = mock_window

    main()

    mock_create_main_window.assert_called_once_with()
    mock_window.mainloop.assert_called_once_with()