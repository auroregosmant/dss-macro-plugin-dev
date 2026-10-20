import html
import time

from dataiku.runnables import Runnable


class DummyMacro(Runnable):
    """A macro that does nothing useful: it echoes a message back."""

    def __init__(self, project_key, config, plugin_config):
        self.project_key = project_key
        self.config = config
        self.plugin_config = plugin_config

    def get_progress_target(self):
        # (target, unit) lets DSS display a progress bar
        return (int(self.config.get("repeat", 1)), "NONE")

    def run(self, progress_callback):
        message = self.config.get("message", "Hello!")
        repeat = int(self.config.get("repeat", 1))

        lines = []
        for i in range(repeat):
            lines.append("<li>{}</li>".format(html.escape(message)))
            progress_callback(i + 1)
            time.sleep(0.2)

        return (
            "<h4>Dummy macro ran successfully</h4>"
            "<p>Project: <code>{}</code></p>"
            "<ul>{}</ul>"
        ).format(html.escape(str(self.project_key)), "".join(lines))
