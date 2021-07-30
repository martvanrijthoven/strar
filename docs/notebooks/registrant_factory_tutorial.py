# ---
# jupyter:
#   jupytext:
#     cell_markers: '"""'
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
"""
# Registrant Factory Tutorial
"""

# %%
from strar.factory import RegistrantFactory
from strar.utils import Text, chain_functions


# %%
class Mode(RegistrantFactory):
    ...

@Mode.register(('training', ))
class Training(Mode):
    pass


# %%
Mode.create('training')
