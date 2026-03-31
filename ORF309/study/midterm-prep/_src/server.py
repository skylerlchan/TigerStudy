#!/usr/bin/env python3
"""
Simple HTTP server with auto-save functionality for midterm tracker.
Run this and access http://localhost:8002/midterm_tracker.html
Changes will auto-save to midterm_tracker_progress.json
"""

import http.server
import json
import os
from pathlib import Path
from urllib.parse import unquote

class TrackerServer(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                # Remove tracker_id if present
                data.pop('tracker_id', None)

                # Write to midterm_tracker_progress.json
                with open('midterm_tracker_progress.json', 'w') as f:
                    json.dump(data, f, indent=2)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
                print(f"Auto-saved progress to midterm_tracker_progress.json ({len(data)} questions)")
            except Exception as e:
                print(f"Error saving: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        # Add CORS headers to all responses
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == '__main__':
    PORT = 8002
    os.chdir(Path(__file__).parent)
    print(f"\nORF309 Midterm Tracker Server")
    print(f"Serving from: {os.getcwd()}")
    print(f"Open: http://localhost:{PORT}/midterm_tracker.html")
    print(f"Auto-save enabled to: midterm_tracker_progress.json\n")

    server = http.server.HTTPServer(('', PORT), TrackerServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped")
