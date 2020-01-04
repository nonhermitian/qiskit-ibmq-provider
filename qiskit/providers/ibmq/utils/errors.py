# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Error handling routines"""
import sys

try:
    from theia.notifications import exception_widget
except ImportError:
    HAS_THEIA = False
else:
    HAS_THEIA = True

#pylint: disable=simplifiable-if-statement
if ('ipykernel' in sys.modules) and ('spyder' not in sys.modules):
    HAS_JUPYTER = True
else:
    HAS_JUPYTER = False

def exception_handler(err):
    """A custom handler of exceptions.
    Allows for pretty formatting of exceptions
    in Jupyter notebooks if Theia is installed.
    """
    if HAS_JUPYTER and HAS_THEIA:
        exception_widget(err)
    else:
        raise err
