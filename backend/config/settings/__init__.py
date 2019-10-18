# settings/__init__.py
# 開発環境では local モジュールが呼び出され、
# 本番環境では production モジュールのみ呼び出されるようになります。

from .production import *

try:
    from .development import *
except:
    pass
