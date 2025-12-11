#!/usr/bin/env python3
"""
간단한 HTTP 서버 실행 스크립트
Python 3가 설치되어 있어야 합니다.

사용 방법:
    python server.py

또는

    python3 server.py

브라우저에서 http://localhost:8000 으로 접속하세요.
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS 헤더 추가
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"서버가 http://localhost:{PORT} 에서 실행 중입니다.")
        print("브라우저에서 위 주소로 접속하세요.")
        print("종료하려면 Ctrl+C를 누르세요.\n")
        
        # 브라우저 자동 열기
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")

if __name__ == "__main__":
    main()

