build notebooks docs in main folder


jupytext --set-formats ipynb,../docs/notebooks//py:percent --sync notebooks/*.ipynb
