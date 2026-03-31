#!/usr/bin/env python3
"""
Unified server for multiple midterm trackers with auto-save capability.
Run: python unified_midterm_server.py
Then open:
  - http://localhost:8000/ECO310/Midterm%20Review%20Materials/midterm_tracker.html
  - http://localhost:8000/ORF309/Midterm%201%20Practice/midterm_tracker.html
"""

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import unquote

class UnifiedTrackerHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path.startswith('/save'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))

                # Get the tracker identifier from the data
                tracker_path = data.get('tracker_id', 'unknown')

                # Determine save location based on tracker_id
                if 'ECO310' in tracker_path:
                    save_path = 'ECO310/Midterm Review Materials/midterm_tracker_progress.json'
                elif 'ORF309' in tracker_path:
                    save_path = 'ORF309/Midterm 1 Practice/midterm_tracker_progress.json'
                else:
                    raise ValueError(f"Unknown tracker: {tracker_path}")

                # Remove tracker_id from data before saving
                save_data = {k: v for k, v in data.items() if k != 'tracker_id'}

                # Save to the appropriate location
                with open(save_path, 'w') as f:
                    json.dump(save_data, f, indent=2)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"status": "saved"}')
                print(f"Saved progress to {save_path}")
            except Exception as e:
                print(f"Error saving: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
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
    PORT = 8000
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('localhost', PORT), UnifiedTrackerHandler)
    print(f'Unified Midterm Tracker Server running at http://localhost:{PORT}/')
    print(f'ECO310: http://localhost:{PORT}/ECO310/Midterm%20Review%20Materials/midterm_tracker.html')
    print(f'ORF309: http://localhost:{PORT}/ORF309/Midterm%201%20Practice/midterm_tracker.html')
    print('Press Ctrl+C to stop')
    server.serve_forever()
