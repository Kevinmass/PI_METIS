"""Módulo de demostración del quality gate (B13). NO MERGEAR.

Código sin ningún test, a propósito: el PR que lo agrega tiene que quedar bloqueado por
`diff-cover` (cobertura del código nuevo < 80 %) y por el quality gate de SonarCloud.
"""


def clasificar_longitud(n: int) -> str:
    """Clasifica la longitud de una serie según la regla de n del contrato de datos."""
    if n < 0:
        raise ValueError("n no puede ser negativo")
    if n < 10:
        return "bloqueante"
    if n < 30:
        return "warning"
    return "recomendable"


def resumen_rango(serie: list[float]) -> dict[str, float | None]:
    """Mínimo, máximo y rango de una serie, ignorando los None."""
    valores = [v for v in serie if v is not None]
    if not valores:
        return {"minimo": None, "maximo": None, "rango": None}
    minimo = min(valores)
    maximo = max(valores)
    return {"minimo": minimo, "maximo": maximo, "rango": maximo - minimo}


def proporcion_sobre_media(serie: list[float]) -> float:
    """Proporción de valores por encima de la media."""
    if not serie:
        return 0.0
    media = sum(serie) / len(serie)
    sobre = [v for v in serie if v > media]
    return len(sobre) / len(serie)
