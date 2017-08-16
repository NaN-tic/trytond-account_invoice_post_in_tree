# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class TestAccountInvoicePostInTreeCase(ModuleTestCase):
    'Test Account Invoice Post in Tree module'
    module = 'account_invoice_post_in_tree'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestAccountInvoicePostInTreeCase))
    return suite
