import re
from pathlib import Path
import unittest

import gatk2ascat


ROOT = Path(__file__).resolve().parents[1]


class TestVersionSync(unittest.TestCase):

    def test_versions_are_synchronized(self):
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        conda_recipe = (ROOT / "conda-recipe" / "meta.yaml").read_text(encoding="utf-8")

        pyproject_version = re.search(
            r'^version\s*=\s*"([^"]+)"$',
            pyproject,
            flags=re.MULTILINE,
        )
        conda_version = re.search(
            r'^\{\%\s*set\s+version\s*=\s*"([^"]+)"\s*\%\}$',
            conda_recipe,
            flags=re.MULTILINE,
        )

        self.assertIsNotNone(pyproject_version)
        self.assertIsNotNone(conda_version)
        self.assertEqual(pyproject_version.group(1), gatk2ascat.__version__)
        self.assertEqual(conda_version.group(1), gatk2ascat.__version__)
