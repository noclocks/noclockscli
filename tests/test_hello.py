from click.testing import CliRunner
from noclockscli.__main__ import cli


class TestHello:
    def test_hello(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["hello"])
        assert result.exit_code == 0
        assert result.output == "Hello, World!\n"
