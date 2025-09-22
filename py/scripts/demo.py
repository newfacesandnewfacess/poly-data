# 브라우저에서 실행될 데모 스크립트 (PyScript/pyodide 환경)
def main():
    import sys, platform
    return f"Hello from demo.py! Python {sys.version.split()[0]} · {platform.platform()}"
