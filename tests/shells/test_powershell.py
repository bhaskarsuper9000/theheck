# -*- coding: utf-8 -*-

import pytest
from theheck.shells import Powershell


@pytest.mark.usefixtures('isfile', 'no_memoize', 'no_cache')
class TestPowershell(object):
    @pytest.fixture
    def shell(self):
        return Powershell()

    def test_and_(self, shell):
        assert shell.and_('ls', 'cd') == '(ls) -and (cd)'

    def test_app_alias(self, shell):
        assert 'function heck' in shell.app_alias('heck')
        assert 'function FUCK' in shell.app_alias('FUCK')
        assert 'theheck' in shell.app_alias('heck')

    def test_how_to_configure(self, shell):
        assert not shell.how_to_configure().can_configure_automatically
