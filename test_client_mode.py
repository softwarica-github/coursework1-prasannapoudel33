import unittest
from unittest.mock import patch, MagicMock
from src.client_mode import SOCKETS, ClientDialogBox


class TestClientDialogBox(unittest.TestCase):
    @patch("src.client_mode.SOCKETS")
    @patch("src.client_mode.ask_ip.ask_ip_dialog")
    def test_socket_connection_and_dialog(self, mock_ask_ip_dialog, mock_sockets):
        # Mock user input for IP address and port
        mock_ask_ip_dialog.return_value = ("127.0.0.1", 5000)

        # Mock SOCKETS instance
        mock_socket_instance = MagicMock()
        mock_sockets.return_value = mock_socket_instance

        # Initialize ClientDialogBox
        app = ClientDialogBox()
        app.ip_address.set("127.0.0.1")
        app.port.set(5000)

