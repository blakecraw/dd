"""Interface specification as abstract base classes.

This specification is implemented by the modules:

- `dd.autoref`
- `dd.cudd`
- `dd.sylvan`
- `dd.buddy`
"""
# Copyright 2017 by California Institute of Technology
# All rights reserved. Licensed under BSD-3.
#


class BDD(object):
    """Shared reduced ordered binary decision diagram."""

    def __init__(self, levels=None):
        self.vars

    def __eq__(self, other):
        pass

    def __len__(self):
        pass

    def __contains__(self, u):
        pass

    def __str__(self):
        pass

    def configure(self, **kw):
        pass

    def statistics(self):
        pass

    def succ(self, u):
        i, v, w = self._bdd.succ(u)
        v = self._wrap(v)
        w = self._wrap(w)
        return i, v, w

    # TODO: perhaps declare ?
    def add_var(self, var, level=None):
        return self._bdd.add_var(var, level=level)

    def var(self, var):
        r = self._bdd.var(var)
        return self._wrap(r)

    def var_at_level(self, level):
        pass

    def level_of_var(self, var):
        pass

    def copy(self, u, other):
        pass

    def support(self, u, as_levels=False):
        pass

    def replace(self, u, dvars):
        pass

    def ite(self, g, u, v):
        pass

    def quantify(self, u, qvars, forall=False):
        pass

    def forall(self, qvars, u):
        pass

    def exist(self, qvars, u):
        pass

    def count(self, u, n=None):
        pass

    def pick_iter(self, u, care_bits=None):
        pass

    def add_expr(self, e):
        pass

    def to_expr(self, u):
        pass

    def apply(self, op, u, v=None, w=None):
        pass

    def _add_int(self, i):
        pass

    def cube(self, dvars):
        pass

    # TODO: homogeneize API
    def dump(self, filename, roots=None,
             filetype=None, **kw):
        pass

    def load(self, filename, levels=True):
        pass

    @property
    def false(self):
        pass

    @property
    def true(self):
        pass


def rename(u, bdd, dvars):
    r = _bdd.rename(u.node, u.bdd, dvars)
    return u.bdd._wrap(r)


def reorder(bdd, order=None):
    """Apply Rudell's sifting algorithm to `bdd`."""
    _bdd.reorder(bdd._bdd, order=order)


def copy_vars(source, target):
    _bdd.copy_vars(source._bdd, target._bdd)


def copy_bdd(u, source, target):
    r = _bdd.copy_bdd(u.node, source._bdd, target._bdd)
    return target._wrap(r)


# could be called `Operator` too
class Function(object):
    """Convenience wrapper for edges returned by `BDD`."""

    def __init__(self, node, bdd):
        assert node in bdd._bdd, node
        self.bdd = bdd
        self.manager = bdd._bdd
        self.node = node
        self.manager.incref(node)

    def __hash__(self):
        return self.node

    def to_expr(self):
        pass

    def __int__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __del__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __invert__(self):
        pass

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    # def __xor__(self, other):
    #     pass

    # unsure about this
    def implies(self, other):
        pass

    # usure about this
    def equiv(self, other):
        pass

    @property
    def level(self):
        pass

    @property
    def var(self):
        pass

    @property
    def low(self):
        pass

    @property
    def high(self):
        pass

    @property
    def ref(self):
        pass

    @property
    def negated(self):
        pass

    @property
    def support(self):
        pass
