build notebooks docs
jupytext --set-formats ipynb,../docs/notebooks//py:percent --sync notebooks/*.ipynb
