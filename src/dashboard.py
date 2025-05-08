import dash
from dash import dcc, html
import dash_table
import plotly.express as px

def create_dashboard(alerts_df):
    app = dash.Dash(__name__)
    # Create an example chart: histogram of risk scores
    fig = px.histogram(alerts_df, x="risk_score", title="Risk Score Distribution")

    app.layout = html.Div(children=[
        html.H1(children='Threat Intelligence Dashboard'),
        html.Div(children='Aggregated and correlated threat data visualization.'),
        dash_table.DataTable(
            id='alerts-table',
            columns=[{"name": col, "id": col} for col in alerts_df.columns],
            data=alerts_df.to_dict('records'),
            page_size=10,
        ),
        dcc.Graph(figure=fig)
    ])

    return app

if __name__ == '__main__':
    from alert_scoring import score_alerts
    from correlation_engine import correlate_data
    from threat_feed_collector import fetch_threat_feeds
    from log_collector import load_logs

    logs = load_logs("data/simulated_logs.csv")
    threat_data = fetch_threat_feeds()
    correlated = correlate_data(threat_data, logs)
    scored_alerts = score_alerts(correlated)
    app = create_dashboard(scored_alerts)
    app.run_server(debug=True)
