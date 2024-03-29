# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

# Copyright (C) 2003-2007, 2009-2011 Nominum, Inc.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose with or without fee is hereby granted,
# provided that the above copyright notice and this permission notice
# appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND NOMINUM DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL NOMINUM BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import unittest

import dns.rdataclass
import dns.rdatatype


class RdTypeAndClassTestCase(unittest.TestCase):

    # Classes

    def test_class_meta1(self):
        self.assertTrue(dns.rdataclass.is_metaclass(dns.rdataclass.ANY))

    def test_class_meta2(self):
        self.assertFalse(dns.rdataclass.is_metaclass(dns.rdataclass.IN))

    def test_class_bytext1(self):
        self.assertEqual(dns.rdataclass.from_text("IN"), dns.rdataclass.IN)

    def test_class_bytext2(self):
        self.assertEqual(dns.rdataclass.from_text("CLASS1"), dns.rdataclass.IN)

    def test_class_bytext_bounds1(self):
        self.assertEqual(dns.rdataclass.from_text("CLASS0"), 0)
        self.assertEqual(dns.rdataclass.from_text("CLASS65535"), 65535)

    def test_class_bytext_bounds2(self):
        def bad():
            dns.rdataclass.from_text("CLASS65536")

        self.assertRaises(ValueError, bad)

    def test_class_bytext_unknown(self):
        def bad():
            dns.rdataclass.from_text("XXX")

        self.assertRaises(dns.rdataclass.UnknownRdataclass, bad)

    def test_class_totext1(self):
        self.assertEqual(dns.rdataclass.to_text(dns.rdataclass.IN), "IN")

    def test_class_totext2(self):
        self.assertEqual(dns.rdataclass.to_text(999), "CLASS999")

    def test_class_totext_bounds1(self):
        def bad():
            dns.rdataclass.to_text(-1)

        self.assertRaises(ValueError, bad)

    def test_class_totext_bounds2(self):
        def bad():
            dns.rdataclass.to_text(65536)

        self.assertRaises(ValueError, bad)

    # Types

    def test_type_meta1(self):
        self.assertTrue(dns.rdatatype.is_metatype(dns.rdatatype.ANY))

    def test_type_meta2(self):
        self.assertTrue(dns.rdatatype.is_metatype(dns.rdatatype.OPT))

    def test_type_meta3(self):
        self.assertFalse(dns.rdatatype.is_metatype(dns.rdatatype.A))

    def test_type_singleton1(self):
        self.assertTrue(dns.rdatatype.is_singleton(dns.rdatatype.SOA))

    def test_type_singleton2(self):
        self.assertFalse(dns.rdatatype.is_singleton(dns.rdatatype.A))

    def test_type_bytext1(self):
        self.assertEqual(dns.rdatatype.from_text("A"), dns.rdatatype.A)

    def test_type_bytext2(self):
        self.assertEqual(dns.rdatatype.from_text("TYPE1"), dns.rdatatype.A)

    def test_type_bytext_bounds1(self):
        self.assertEqual(dns.rdatatype.from_text("TYPE0"), 0)
        self.assertEqual(dns.rdatatype.from_text("TYPE65535"), 65535)

    def test_type_bytext_bounds2(self):
        def bad():
            dns.rdatatype.from_text("TYPE65536")

        self.assertRaises(ValueError, bad)

    def test_type_bytext_unknown(self):
        def bad():
            dns.rdatatype.from_text("XXX")

        self.assertRaises(dns.rdatatype.UnknownRdatatype, bad)

    def test_type_totext1(self):
        self.assertEqual(dns.rdatatype.to_text(dns.rdatatype.A), "A")

    def test_type_totext2(self):
        self.assertEqual(dns.rdatatype.to_text(999), "TYPE999")

    def test_type_totext_bounds1(self):
        def bad():
            dns.rdatatype.to_text(-1)

        self.assertRaises(ValueError, bad)

    def test_type_totext_bounds2(self):
        def bad():
            dns.rdatatype.to_text(65536)

        self.assertRaises(ValueError, bad)

    def test_type0_totext(self):
        self.assertEqual(dns.rdatatype.to_text(0), "TYPE0")


if __name__ == "__main__":
    unittest.main()
