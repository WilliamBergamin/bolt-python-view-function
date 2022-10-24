from slack_bolt import App
from slack_bolt.slack_function import SlackFunction

from .sample_view import sample_view, sample_view_submission, sample_view_closed


def register(app: App):
    sample_view_func: SlackFunction = app.function("sample_view_function")(sample_view)
    sample_view_func.view_submission("func_sample_view_id")(sample_view_submission)
    sample_view_func.view_closed("func_sample_view_id")(sample_view_closed)
