from click.testing import CliRunner
from noclockscli.__main__ import cli


class TestHelp:
    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Usage: cli [OPTIONS] COMMAND [ARGS]..." in result.output
