"""Compatibilidade: python ocr/extrair.py [--visao] [--reprocessar]."""
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo.extract import extract, inventory

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--visao', action='store_true')
    parser.add_argument('--reprocessar', action='store_true')
    args = parser.parse_args()
    inventory()
    extract(vision=args.visao, retry=args.reprocessar)
