=========
PySignals
=========
:Info: PySignals is a signal dispatcher for Python, extracted from the Django framework.

About
=====
PySignals is a signal dispatcher for Python, extracted from "django.dispatch"
in the Django framework so it can be used in applications without requiring
the entire Django framework to be installed.

Installation
============
If you have `setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_
you can use ``easy_install -U pysignals``. Otherwise, you can download the
source from `GitHub <https://github.com/theojulienne/PySignals>`_ and run
``python setup.py install``.

Documentation
=============
PySignals is directly extracted from the Django framework, therefore the best
place to get documentation is from the 
`Django Signals Documentation <http://docs.djangoproject.com/en/dev/topics/signals/>`_.

The only difference is that all occurrences of ``django.dispatch`` should be
replaced by ``pysignals``.