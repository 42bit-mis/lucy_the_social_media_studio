"""Lucy REST API launcher.

Usage:
    python lucy_api.py
    python lucy_api.py --host 0.0.0.0 --port 8765
    python lucy_api.py --reload          # auto-reload on code changes (dev)

Environment variables:
    LUCY_API_KEY        Protect all endpoints with this key (X-Lucy-API-Key header)
    LUCY_CORS_ORIGINS   Comma-separated allowed origins (default: *)
"""
from __future__ import annotations
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(prog="lucy_api", description="Lucy REST API server")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8765, help="Bind port (default: 8765)")
    parser.add_argument("--reload", action="store_true", help="Auto-reload on code changes (dev mode)")
    parser.add_argument("--workers", type=int, default=1, help="Number of worker processes")
    args = parser.parse_args()

    try:
        import uvicorn
    except ImportError:
        print("uvicorn not installed. Run:  pip install -r requirements-api.txt")
        sys.exit(1)

    print(f"""
╔══════════════════════════════════════════════════════╗
║         Lucy Media Studio — REST API Server          ║
╠══════════════════════════════════════════════════════╣
║  URL      http://{args.host}:{args.port}
║  Docs     http://localhost:{args.port}/docs
║  Status   http://localhost:{args.port}/api/status
╚══════════════════════════════════════════════════════╝
    """)

    uvicorn.run(
        "social_media_studio.api:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        workers=args.workers if not args.reload else 1,
    )


if __name__ == "__main__":
    main()
