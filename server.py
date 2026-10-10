
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import datetime


class CloudHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        container_id = socket.gethostname()
        server_time = datetime.datetime.now(
            datetime.timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S UTC")

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>My First Cloud Microservice</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #0b0f19;
                    color: #f8fafc;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                }}
                .card {{
                    background: #111827;
                    border: 1px solid #1f2937;
                    border-radius: 12px;
                    padding: 36px 48px;
                    text-align: center;
                    max-width: 500px;
                }}
                h1 {{ color: #38bdf8; }}
                .badge {{
                    background: #0284c7;
                    color: white;
                    padding: 6px 12px;
                    border-radius: 9999px;
                    font-size: 13px;
                    display: inline-block;
                }}
                .info-box {{
                    background: #1e293b;
                    border-radius: 8px;
                    padding: 16px;
                    text-align: left;
                    font-family: monospace;
                    line-height: 2;
                    color: #cbd5e1;
                }}
                .highlight {{ color: #4ade80; }}
            </style>
        </head>
        <body>
            <div class="card">
                <span class="badge">CCD LEVEL 6 · WEEK 1</span>
                <h1>🚀 Containerized Microservice</h1>
                <p style="color: #94a3b8;">
                    Running inside a Linux container
                </p>
                <div class="info-box">
                    <div>📦 <b>Container Hostname:</b>
                        <span class="highlight">{container_id}</span>
                    </div>
                    <div>⏰ <b>Server Timestamp:</b> {server_time}</div>
                    <div>🌐 <b>Port:</b> 8080</div>
                    <div>🎯 <b>Target:</b> Ready for AWS Cloud Deployment!</div>
                </div>
            </div>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        print(
            f"[{self.log_date_time_string()}] "
            f"{self.address_string()} - {format % args}"
        )


if __name__ == "__main__":
    port = 8080
    print(f"Starting microservice on port {port}...")
    server = HTTPServer(("0.0.0.0", port), CloudHandler)
    server.serve_forever()