#!/usr/bin/env python3
"""
Simple local server for midterm tracker with auto-save capability.
Run: python server.py
Then open: http://localhost:8000/midterm_tracker.html
"""

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class TrackerHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                with open('midterm_tracker_progress.json', 'w') as f:
                    json.dump(data, f, indent=2)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"status": "saved"}')
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f'{{"error": "{str(e)}"}}'.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    PORT = 8001
    server = HTTPServer(('localhost', PORT), TrackerHandler)
    print(f'\nECO310 Midterm Tracker Server')
    print(f'Open: http://localhost:{PORT}/midterm_tracker.html')
    print(f'Auto-save enabled to: midterm_tracker_progress.json')
    print('Press Ctrl+C to stop\n')
    server.serve_forever()
