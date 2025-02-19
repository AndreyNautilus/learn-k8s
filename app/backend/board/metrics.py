from flask import request
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics.for_app_factory()

metric_count_by_path = metrics.counter(
    "flask_http_request_by_path_total",
    "Request count by request paths",
    labels={"path": lambda: request.path},
)
