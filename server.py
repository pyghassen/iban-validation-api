from app.views import http_server


if __name__ == "__main__":
    http_server.run(host="0.0.0.0", port=8000)
