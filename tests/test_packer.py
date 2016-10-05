import os

import packer


PACKER_PATH = '/usr/bin/packer'
TEST_RESOURCES_DIR = 'tests/resources'
TEST_PACKERFILE = os.path.join(TEST_RESOURCES_DIR, 'packerfile.json')
TEST_BAD_PACKERFILE = os.path.join(TEST_RESOURCES_DIR, 'badpackerfile.json')


class TestBase():

    def test_build(self):
        p = packer.Packer(TEST_PACKERFILE)
        p.build()

    def test_fix(self):
        p = packer.Packer(TEST_PACKERFILE)
        p.fix()

    def test_inspect(self):
        p = packer.Packer(TEST_PACKERFILE)
        p.inspect()

    def test_validate(self):
        p = packer.Packer(TEST_PACKERFILE)
        p.validate()

    def test_version(self):
        p = packer.Packer(TEST_PACKERFILE)
        p.version()
