# Modern namespace package implementation (PEP 420)
# Fallback para compatibilidade com versões antigas do Python
import sys

if sys.version_info >= (3, 3):
    # PEP 420 - implicit namespace package (Python 3.3+)
    # No code needed - implicit namespace package
    pass
else:
    # Fallback para versões antigas (Python < 3.3)
    try:
        from pkgutil import extend_path
        __path__ = extend_path(__path__, __name__)
    except ImportError:
        # Último recurso - definir __path__ manualmente
        import os
        __path__ = [os.path.dirname(__file__)]
